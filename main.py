#Task Manager / To-Do App (CLI)
from datetime import datetime
import time
import json

current_time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")

class Tasks:
    def __init__(self, maintain_option, filter):
        self.filter = filter
        self.maintain_option = maintain_option
    def display(self):
        # Opening JSON (tasks.json) file
        with open('tasks.json', 'r') as openfile:
            saved_tasks = json.load(openfile)
            print('Time of the requested output:', '\n', current_time, '\n')
            print('Your saved tasks:')
            print('Num / Done? / Task')
            for x in saved_tasks['data']:
                if x['completed'] == True:
                    print(x['id'], '    Yes     ', x['task'])
                elif x['completed'] == False:
                    print(x['id'], '    No     ', x['task'])
            input("Hit enter to go back to the menu")
            main()
    def maintain(self):
        if self.maintain_option == 1:
            print('\n', 'Task adding process...')
            print('What do you want to save? Enter your task details.')
            task_name = input("Task: ")
            if len(task_name) < 1:
                print('Please provide a valid task name. Just give it some details.')
                time.sleep(.9)
                return self.maintain()
            print('\n', 'Task adding process...')
            # JSON interaction
            with open('tasks.json', 'r+') as openfile:
                file_data = json.load(openfile)
                current_id = max(file_data['data'], key=lambda ev: ev['id'])
                task_data = {
                "id": int(current_id['id'])+1,
                "task": task_name,
                "completed": False,
                }
                file_data['data'].append(task_data)
                openfile.seek(0)
                json_object = json.dump(file_data, openfile, indent=4)
            print('Successfully added!')
            time.sleep(.4)
            self.display()
        if self.maintain_option == 2:
            print('\n', 'Task removing process...')
            print('What task do you wish to remove? Enter your task number')
            try:
                task_name = int(input("Task number: "))
            except ValueError:
                print("You must only use numbers!")
                time.sleep(.9)
                return self.maintain()
            print('\n', 'Task removing process...')
            print('Successfully removed!')
            time.sleep(.4)
            self.display()
        if self.maintain_option == 3:
            print('\n', 'Change task status')
            print('What task you wish to maintain? Please provide the number')
            try:
                task_name = int(input("Task number: "))
            except ValueError:
                print("You must only use numbers identified above!")
                time.sleep(.9)
                return self.maintain()
            print('\n', 'Enter the new status', '\n')
            print('1 Done')
            print('2 Undone')
            try:
                set_status = int(input("New status: "))
            except ValueError:
                print("You must only use numbers identified above!")
                time.sleep(.9)
                return self.maintain()
            if set_status == 1:
                print('Successfully changed the status to Done!')
                time.sleep(.4)
                self.display()
            elif set_status == 2:
                print('Successfully changed the status to Undone!')
                time.sleep(.4)
                self.display()
            else:
                print("You must only use numbers identified above!")
                time.sleep(.9)
                return self.maintain()
def main():
    print(current_time, '\n')
    print('Welcome to the Task Manager.')
    print('What are your plans today?', '\n')
    print('1 Add task/Remove task/Maintain tasks')
    print('2 Display all your tasks')
    print('3 Apply filter (done/to do)')
    try:
        option = int(input('Select: '))
    except ValueError:
        print("You must only use numbers identified above!")
        time.sleep(.9)
        return main()
    if option == 1:
        print(current_time, '\n')
        print('Choose one of the options below.', '\n')
        print('1 Add task')
        print('2 Remove task')
        print('3 Maintain status')
        try:
            maintain_option = int(input('Select: '))
        except ValueError:
            print("You must only use numbers identified above!")
            time.sleep(.9)
            return main()
        if maintain_option == 1 or maintain_option == 2 or maintain_option == 3:
            tasks = Tasks(maintain_option, None)
            tasks.maintain()
        else:
            print("You must only use numbers identified above!")
            time.sleep(.9)
            return main()
    elif option == 2:
        tasks = Tasks(None, None)
        tasks.display()
    elif option == 3:
        print('3')
    elif option > 3 or option < 1:
        print("You must only use numbers identified above!")
        time.sleep(.9)
        return main()
main()