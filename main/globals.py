global global_container
global_container = {}

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