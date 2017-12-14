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

class Model():
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
        if os.path.exists(self.file_name):  # optional check if file exists
            with open(self.file_path, 'a') as file:
                file.write("\n")

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