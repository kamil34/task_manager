# Task Manager / To-Do App (CLI)
from datetime import datetime
import time
import json
from sys import exit

class DisplayTime():
    def __init__(self):
        print(f"{datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")} \n")
class MainMenuRedirect():
    def __init__(self, error_text, redirect_type, option=None, nowait=None):
        if error_text: print(error_text)
        if not nowait: time.sleep(.9)
        tasks = Tasks(None, None)
        if (redirect_type == "main"):   
            tasks.main()
        elif (redirect_type == "maintain" and option):
            tasks.maintain(option)
        elif (redirect_type == "display"):
            tasks.display()
        elif (redirect_type == "option_display" and option):
            tasks.option_display(option)

class Tasks():
    def __init__(self, maintain_option, filter):
        self.filter = filter
        self.maintain_option = maintain_option
    def display(self):
        # Opening JSON (tasks.json) file
        with open('tasks.json', 'r') as openfile:
            saved_tasks = json.load(openfile)
            print('Time of the requested output: \n')
            DisplayTime()
            print('Your saved tasks: \n',
                  'Num / Done? / Task')
            for task in saved_tasks['data']:
                if task['completed'] == True:
                    print(task['id'], '    Yes     ', task['task'])
                elif task['completed'] == False:
                    print(task['id'], '    No     ', task['task'])
            input("Hit enter to go back to the menu")
            MainMenuRedirect(None, "main", nowait=True)
    def maintain(self, maintain_option):
        if (maintain_option == 1):
            print('\n Task adding process... \n',
                  'What do you want to save? Enter your task details.')
            task_name = input("Task: ")
            if task_name:
                print('\n', 'Task adding process...')
                # JSON interaction (adding)
                with open('tasks.json', 'r+') as tasks_file:
                    file_data = json.load(tasks_file)
                    current_id = max(file_data['data'], key=lambda ev: ev['id'])
                    task_data = {
                    "id": int(current_id['id'])+1,
                    "task": task_name,
                    "completed": False,
                    }
                    file_data['data'].append(task_data)
                    tasks_file.seek(0)
                    json.dump(file_data, tasks_file, indent=4)
                print('Successfully added!')
                # time.sleep(.4)
                MainMenuRedirect(None, "display")
            else:
                MainMenuRedirect("Please provide a valid task name. Just give it some details.", "maintain", option=maintain_option)
        elif (maintain_option == 2):
            print('\n Task removal process... \n',
                  'What task do you wish to remove? Enter your task number')
            # try:
            #     task_num = int(input("Task number: "))
            while(task_num := input("Task number: ")).isdigit():
                # with open('tasks.json', 'r+') as open_file:
                #     file_data = json.load(open_file)
                #     for i in file_data['data']:
                #         if i['id'] == task_num:
                #             del file_data['data'][task_num-1]
                #     for item in file_data['data']:
                #         # To do
                #         if item['id'] > 1 and (item['id'] - 1) != item['id'] :
                #             item['id'] -= 1
                #     open_file.seek(0)
                #     open_file.truncate()
                #     json.dump(file_data, open_file, indent=4)
                with open('tasks.json', 'r+') as tasks_file:
                    print('TODO') # (todo)
                print('\n Task removal process... \n',
                      'Successfully removed!')
                MainMenuRedirect(None, "display")
            else:
                MainMenuRedirect("Wrong number! Try again", "maintain", option=maintain_option)
                # To do task removal process (json)
                # + Error handling caused by unknown values after searching the JSON file
                # JSON interaction (removal)
        elif (maintain_option == 3):
            print('\n Change task status \n',
                  'What task you wish to maintain? Please provide the number')
            while(task_num := input("Task number: ")).isdigit():
                # To do task maintaining process
                print("to do")
                MainMenuRedirect(None, "main")
                # print('\n', 'Enter the new status', '\n')
                # print('1 Done')
                # print('2 Undone')
                # try:
                #     set_status = int(input("New status: "))
                # except ValueError:
                #     print("You must only use numbers identified above!")
                #     time.sleep(.9)
                #     return self.maintain()
                # if set_status == 1:
                #     print('Successfully changed the status to Done!')
                #     time.sleep(.4)
                #     self.display()
                # elif set_status == 2:
                #     print('Successfully changed the status to Undone!')
                #     time.sleep(.4)
                #     self.display()
                # else:
                #     print("You must only use numbers identified above!")
                #     time.sleep(.9)
                #     return self.maintain()
            else:
                MainMenuRedirect("You must only use numbers identified above!", "maintain", option=maintain_option)
    def option_display(self, number):
        if (number == 1):
            DisplayTime()
            print('Choose one of the options below. \n',
                  '1 Add task \n',
                  '2 Remove task \n',
                  '3 Maintain status \n')
            while(user_input := input("Select: ")).isdigit():
                user_input = int(user_input)
                if ((user_input <= 1) or (user_input <= 3)):
                    self.maintain(user_input)
                else:
                    MainMenuRedirect("You must only use numbers identified above!", "option_display", option=number)
            else:
                MainMenuRedirect("You must only use numbers identified above!", "main")
        elif number == 2:
            self.display()
        elif number == 3:
            print('3')
        elif number == 4:
            exit()
        elif number > 4 or number < 1:
            MainMenuRedirect("You must only use numbers identified above!", "main")
    def main(self):
        DisplayTime()
        print('Welcome to the Task Manager \n',
              'What are your plans today? \n',
              '1 Add/Remove/Maintain task \n',
              '2 Display all the tasks \n',
              '3 Apply filter (done/to do)')
        while(user_option := input("Select: ")).isdigit():
            self.option_display(int(user_option))
        else:
            MainMenuRedirect("You must only use numbers identified above!", "main")

def main():
    tasks = Tasks(None, None)
    tasks.main()

main()