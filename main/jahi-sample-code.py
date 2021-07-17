global global_container
global_container = {}

def teleop_setup():
    create_global_var("isRotating", False)
    
def teleop_main():
    global global_container
    user_move_robot()
    if(Keyboard.get_value("r")):
        global_container["isRotating"] = True
        rotate_robot("isRotating", (1.06))
        Robot.sleep(1.0)


        
        

############ USER DEFINED FUNCTIONS SECTION ############
def asign_key_function(asign_key={}, callback=None):
    if(Keyboard.get_value(asign_key["input_key"])):
        global_container[asign_key["gc_key"]] = asign_key["gc_val"]
        callback(asign_key["callback_args"])
        Robot.sleep(1.0)
        
def rotate_robot(key, degrees=1.06):
    #90degree = 1.06
    global global_container
    if(global_container[key]):
        system_move_robot(-1, -1, degrees)
        global_container[key] = False

def system_move_robot(x, y, delay):
    Robot.set_value("left_motor", "duty_cycle", x)
    Robot.set_value("right_motor", "duty_cycle", y)
    Robot.sleep(delay)
    Robot.set_value("left_motor", "duty_cycle", 0)
    Robot.set_value("right_motor", "duty_cycle", 0)
    
def user_move_robot():
    Robot.set_value("left_motor", "duty_cycle", -Gamepad.get_value("joystick_left_y"))
    Robot.set_value("right_motor", "duty_cycle", Gamepad.get_value("joystick_right_y"))
        
def create_global_var(g_key, g_val):
    global global_container
    global_container[g_key] = g_val;
    if g_key in global_container.keys():
        print("new key ['{}'] created".format(g_key))
    else:
        print("Error: new key ['{}'] could no be created".format(g_key))
        
def delete_global_var(g_key):
    global global_container
    global_container.pop(g_key, None)
    if g_key not in global_container.keys():
        print("key ['{}'] deleted".format(g_key))
    else:
        print("Error: key ['{}'] could not be deleted".format(g_key))
        
        
        


############ USER DEFINED CLASSES SECTION ############        
class Global_Cont:
    global_vars = {}
    
    def create_global_var(g_key, g_val):
        Global_Cont.global_vars[g_key] = g_val;
        if g_key in Global_Cont.global_vars.keys():
            print("new key ['{}'] created".format(g_key))
        else:
            print("Error: new key ['{}'] could no be created".format(g_key))
            
    def delete_global_var(g_key):
        if g_key in Global_Cont.global_vars.keys():
            Global_Cont.global_vars.pop(g_key, None)
            print("key ['{}'] deleted".format(g_key))
        else:
            print("Error: key ['{}'] could not be deleted".format(g_key))
    
    def update_global_var(g_key, g_val):
        Global_Cont.global_vars[g_key] = g_val
        if g_key in Global_Cont.global_vars.keys():
            print("key ['{}'] updated".format(g_key))
        else:
            print("Error: key ['{}'] could not be updated".format(g_key))



    