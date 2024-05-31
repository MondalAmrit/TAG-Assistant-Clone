import os
def create_notes(name):
    """ Creates a new notes """
    try:
        with open(name) as f:
            pass
        return 'File Already Exists'
    except:
        with open(name,'w') as f:
            pass
        return 'Created new Notes with name as ' + name

def delete_notes(name):
    """ Deletes a notes """
    try:
        with open(name) as f:
            pass
        os.remove(name)
        return 'Deleted Notes with name as ' + name
    except:
        return 'No Such Notes Exists'
    
def read_notes(name):
    """ Shows the notes content """
    try:
        with open(name) as f:
            return f.read()
    except:
        return 'No Such Notes Exists'

def update_notes(name,prev_value = "",new_value = ""):
    """ Just Changes the value in a notes """
    try:
        with open(name) as f:
            pass
    except:
        return 'No Such Notes Exists'
    
    if prev_value == "" and new_value != "":
        with open(name,'a+') as f:
            f.write(new_value)
        return 'Added the ' + new_value + ' to the ' + name + ' Notes' 
    else:
        content = ''
        with open(name) as f:
            for line in f.readlines():
                if line == prev_value:
                    content += (new_value if new_value == "" else "\n" + new_value)
                else:
                    content += "\n" + line
        with open(name,'w') as f:
            f.write(content)

    if new_value == "":
        return 'Removed the '+prev_value+' of the '+name+' Notes'
    else:
        return 'Updated the '+prev_value+' to '+new_value+' in '+name+' Notes'