import sys

class Controller():


    pass


class Model():
    def print_file(self):
        file_name = "todo.txt"
        with open(file_name) as file_open:
            line = file_open.readline()
            count= 1
            while line:
                print("{}: {}".format(count, line.strip()))
                line = file_open.readline()
                count += 1

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
model = Model()
model.print_file()