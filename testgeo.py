# =============================================================================
# Packages to import
# =============================================================================
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
    
    # This is the place where we hook our functionality to menus
    # ----------------------------------------------------------
    add_menu('File')
    add_function_to_menu('File', exit)
    add_menu('Draw')
    add_function_to_menu('Draw', draw_sphere_1)
    add_function_to_menu('Draw', draw_sphere_2)
    add_menu('Erase')
    add_function_to_menu('Erase', erase_all)

# =============================================================================
# Packages to import
# =============================================================================
import sys
from OCC.Display.SimpleGui import *
from OCC.gp import *
from OCC.BRepPrimAPI import *
# =============================================================================
# Functions called from some menu-items
# =============================================================================
def draw_sphere_1(event=None):
# create sphere
    Radius = 50.0
    # The sphere center
    X1 = 0.0
    Y1 = 0.0
    Z1 = 0.0
    # create OCC.gp.gp_Pnt-Point from vector
    Point = gp_Pnt( X1, Y1, Z1 )
    MySphere = BRepPrimAPI_MakeSphere( Point, Radius )
    MySphereShape = MySphere.Shape()
    display.DisplayColoredShape( MySphereShape , 'RED' )
def draw_sphere_2(event=None):
# create sphere
    Radius = 50.0
    # The sphere center
    X1 = 25.0
    
    Y1 = 50.0
    Z1 = 50.0
    # create OCC.gp.gp_Pnt-Point from vector
    Point = gp_Pnt( X1, Y1, Z1 )
    MySphere = BRepPrimAPI_MakeSphere( Point, Radius )
    MySphereShape = MySphere.Shape()
    display.DisplayColoredShape( MySphereShape , 'YELLOW' )
def erase_all(event=None):
    display.EraseAll()
