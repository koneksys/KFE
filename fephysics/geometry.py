import sys

from OCC.Display.SimpleGui import *
# =============================================================================
# Functions called from some menu-items
# =============================================================================
def draw_nothing(event=None):
    pass
def exit(event=None):
    sys.exit()
# =============================================================================
# Main-part: If this script is running as a main script, i.e. it
# is directly called by Python the following is executed.
# =============================================================================
if __name__ == '__main__':
# OCC.Display.SimpleGui.init_display() returns multiple
# values which are assigned here
    display, start_display, add_menu, add_function_to_menu = \
    init_display()
# This is the place where we hook our functionality to menus
# ----------------------------------------------------------
    add_menu('File')
    add_function_to_menu('File', exit)
    add_menu('Draw')
    add_function_to_menu('Draw', draw_nothing)
    start_display()