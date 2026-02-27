def get_todos(filepath):
    """ Returns a list of todos from the file """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    """ Writes todos to the file """
    with open(filepath, "w") as file:
         file.writelines(todos_arg)