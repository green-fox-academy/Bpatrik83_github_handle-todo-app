import sys

class Controller():


    pass


class Model():
    def print_file(self):
        read_todo = open("todo.txt", "r")
        read_lines_todo = read_todo.read().split("\n")
        print(read_lines_todo)
    pass

class Display():
    def show_menu(self):
        print(
            "\n"
            "Python Todo application\n"
            "=======================\n"
            "\n"
            "Command line arguments:\n"
            "-l   Lists all the tasks\n"
            "-a   Adds a new task\n"
            "-r   Removes a task\n"
            "-c   Completes a task)\n")
    


display = Display()
display.show_menu()
