from Model.get_model import model

#####################################
# Works like a CMD from chat UI

def check_cmd(query: str):
    # Check for calculation
    try:
        return eval(query.replace('x','*').replace('X','*'))
    except:
        pass

    # Check for the function Command
    cmd = query.split()[0]
    if (cmd[0] != '@'):
        return model.generate(query)
    else:
        # Execute the function.
        return f'{query.split()[0][0:]} is called'