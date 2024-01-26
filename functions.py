FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as files_local:
        todos_local = files_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as files:
        files.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())