#Task Manager / To-Do App (CLI)
from datetime import datetime
import time
import json

current_time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")

class Tasks:
    def __init__(self, filter):
        self.filter = filter
    def display():
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
def main():
    print(current_time, '\n')
    print('Welcome to the Task Manager.')
    print('What are your plans today?', '\n')
    print('1 Add/Remove tasks')
    print('2 Display all your tasks')
    print('3 Apply filter (done/to do)')
    try:
        option = int(input('Select: '))
    except ValueError:
        print("You must only use numbers identified above!")
        time.sleep(.9)
        return main()
    if option == 1:
        print('1')
    elif option == 2:
        # print('2')
        Tasks.display()
    elif option == 3:
        print('3')
    elif option > 3 or option < 1:
        print("You must only use numbers identified above!")
        time.sleep(.9)
        return main()
main()