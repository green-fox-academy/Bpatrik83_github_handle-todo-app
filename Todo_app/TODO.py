import os
import sys

class Controller():
    def controll_argv(self):
        display = Display()
        model = Model()
        if len(sys.argv) == 1:
            display.show_menu()
        elif sys.argv[1] == "-l":
            model.print_file()
        elif sys.argv[1] == "-a":
            if sys.argv[2:] == []:
                print("You did not enter anything")
            else:
                model.add_new_task()

class Model():
    def __init__(self):
        self.file_name = "todo.txt"

    def print_file(self):
        self.file_name = "todo.txt"
        with open(self.file_name) as file_open:
            line = file_open.readline()
            count= 1
            while line:
                print("{} - {}".format(count, line.strip()))
                line = file_open.readline()
                count += 1

    def add_new_task(self):
        self.text_append = " ".join(sys.argv[2:])
        if os.path.exists(self.file_name):
            with open(self.file_name, 'a') as file:
                file.write("\n" + self.text_append)

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

controller = Controller()
controller.controll_argv()