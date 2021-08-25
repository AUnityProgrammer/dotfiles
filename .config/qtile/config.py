#IMPORTS
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List

#VARIABLES
mod = "mod4"
terminal = "alacritty"
browser = "firefox"
filemanager= "pcmanfm"
launcher = "rofi -show drun"
#launcher = "dmenu_run -c"

#AUTOSTART
@hook.subscribe.startup
def autostart():
        home = os.path.expanduser('~/.config/qtile/autostart.sh')
        subprocess.call([home])

#KEYBINDS_START 
keys = [

    #KEY_GROUP Apps
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch Terminal"),

    Key([mod], "w",
        lazy.spawn(browser),
        desc="Launch Browser"),

    Key([mod, "shift"], "f",
        lazy.spawn(filemanager),
        desc="Launch File Manager"),

    Key([mod], "d",
        lazy.spawn(launcher),
        desc="Launch Run Launcher"),

    Key([mod], "p",
        lazy.spawn("bash /home/daffad/.config/rofi/powermenu/powermenu.sh"),
        desc="Launch Powermenu"),

    Key([mod, "shift"], "slash",
        lazy.spawn("./scripts/shell/keybinds-qtile.sh"),
        desc="Launch Help Scripts"),

    Key([mod, "shift"], "a",
        lazy.spawn("flameshot gui"),
        desc="Screenshot"),

    #KB_GROUP Volume

    Key([], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"),
        desc="Mute Volume"),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%- unmute"),
        desc="Lower Volume"),

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+ unmute"),
        desc="Increase Volume"),

    #KEY_GROUP Window Controls
#    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
#    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),

    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),

    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),

    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    Key([mod, "shift"], "Left",
            lazy.layout.shuffle_left(),
        desc="Move window to the left"),

    Key([mod, "shift"], "Right",
            lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod, "shift"], "Down",
            lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "Up",
            lazy.layout.shuffle_up(),
            desc="Move window up"),

    Key([mod], "t",
            lazy.window.toggle_floating(),
            desc="Toggle floating"),

    Key([mod], "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle Fulscreen"),


    Key([mod], "l",
            lazy.layout.shrink(),
            lazy.layout.decrease_nmaster(),
            desc="Grow window to the left"),

    Key([mod], "h",
            lazy.layout.grow(),
            lazy.layout.increase_nmaster(),
            desc="Grow window to the right"),


    Key([mod], "Tab",
            lazy.next_layout(),
            desc="Toggle between layouts"),

    Key([mod, "shift"], "c",
            lazy.window.kill(),
            desc="Kill focused window"),


    Key([mod], "q",
            lazy.restart(),
            desc="Restart Qtile"),

    Key([mod, "shift"], "q",
            lazy.shutdown(),
            desc="Shutdown Qtile"),
]
#KEYBINDS_END

def init_group_names():
       return  [
               ("WWW", {'layout': 'monadtall'}),
               ("MEET", {'layout': 'monadtall'}),
               ("TERM", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("CONF", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'monadtall'})
        ]

def init_groups():
        return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
        group_names = init_group_names()
        groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 3,
                "margin": 20,
                "border_focus": "#5e81ac",
                "border_normal": "#2E3440"
                }

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.MonadTall(
                name = 'XMonad',
                **layout_theme),
    # Try more layouts by unleashing below layouts.
   # layout.Stack(**layout_theme),
   # layout.Bsp(
   #             name = 'BSPWM',
   #             **layout_theme),
   # layout.Tile(**layout_theme),
    layout.Max(),
    layout.Floating(**layout_theme),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#2e3440", "#2e3440"],
          ["#44475a", "#44475a"],
          ["#ffffff", "#ffffff"],
          ["#4c566a", "#4c566a"],
          ["#ffb86c", "#ffb86c"],
          ["#4f76c7", "#4f76c7"],
          ["#74438f", "#74438f"],
          ["#ff79c6", "#ff79c6"],
          ["#a3be8c", "#a3be8c"]]

widget_defaults = dict(
    font='Ubuntu',
    fontsize=15,
    padding=3,
    foreground= colors[2],
    background= colors[0],
)

icon_defaults = {
        "padding":5,
                }
extension_defaults = widget_defaults.copy()

sep = " | "

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(launcher)}

                            ),
                widget.GroupBox(
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[1],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[1],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                                ),
                widget.TextBox(sep),
                widget.WindowName(
                        max_chars = 70,
                                 ),
                widget.TextBox(
                        text='',
                        fontsize=15,
                        background=colors[3],
                        **icon_defaults
                              ),
                widget.CPU(
                        format = '{load_percent}%',
                        core = 'all',
                        background=colors[0],
                        ),
                widget.TextBox(
                        text='',
                        fontsize=15,
                        background=colors[5],
                        **icon_defaults,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                              ),
                widget.Memory(
                        format = '{MemUsed: .0f}{mm}',
                        background=colors[0],
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')}
                        ),
                widget.TextBox(
                        text='',
                        fontsize=15,
                        background=colors[3],
                        **icon_defaults,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e nmtui')}
                              ),
                widget.Net(
                        interface="wlan0",
                        background=colors[0],
                        format = '{down}',
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e nmtui')}

                          ),
                widget.TextBox(
                        text='',
                        fontsize=15,
                        background=colors[5],
                              ),
                widget.Battery(
                        charge_char='+',
                        discharge_char='-',
                        error_message='error',
                        format='{percent:2.0%}{char}',
                        battery_name = 'BAT0',
                        background=colors[0]
                        ),
                widget.TextBox(text=' ', background=colors[0]),
                widget.TextBox(
                              text='',
                              fontsize=15,
                              background=colors[3],
                              ),
                widget.Clock(format='%a %Y/%m/%d %I:%M',
                              background=colors[0],
                            ),
                widget.Systray(background=colors[0],),
            ],
            31,
           opacity = 0.8,
#           margin = 15,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
     Match(wm_class='confirmreset'),  # gitk
     Match(wm_class='makebranch'),  # gitk
     Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Yad'),
    Match(title='zoom'),
    Match(title='Zoom Cloud Meetings'),
    Match(wm_class='tm'),
    Match(wm_class='org-tlauncher-tlauncher-rmo-TLauncher'),
],
**layout_theme,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
