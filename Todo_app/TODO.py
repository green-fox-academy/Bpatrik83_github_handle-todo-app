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
                print("Unable to add: no task provided")
            else:
                model.add_new_task()
        elif sys.argv[1] == "-r":
            if sys.argv[2:] == []:
                print("Unable to remove: no index provided")
            else:
                model.remove_task()

class Model():
    def __init__(self):
        self.file_name = "todo.txt"

    def print_file(self):
        with open(self.file_name) as file_open:
            if os.stat(self.file_name).st_size == 0:
                print("No todos for today! :)")
            else:
                line = file_open.readline()
                count= 1
                while line:
                    print("{} - {}".format(count, line.strip()))
                    line = file_open.readline()
                    count += 1

    def add_new_task(self):
        text_append = " ".join(sys.argv[2:])
        if os.path.exists(self.file_name):
            with open(self.file_name, 'a') as file:
                file.write(text_append + "\n")

    def remove_task(self):
        try:
            delete_line_index = int(sys.argv[2])
        except ValueError:
            print("Unable to remove: index is not a number")
        else:
            with open(self.file_name, "r+") as open_file:
                lines = open_file.readlines()
                if len(lines) < delete_line_index:
                    print("Unable to remove: index is out of bound")
                else:
                    del lines[delete_line_index - 1]
                    open_file.seek(0)
                    open_file.truncate()
                    open_file.writelines(lines)

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