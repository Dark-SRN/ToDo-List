counter = 1

print('\nWhat would you like to do?')
print('a: Add an item to the list')
print('v: View the list')
print('q: Quit The Program')
print('c: Clear the list')
print('r: Remove an item from the list')
print('h: View the task with the highest priority')
while True:
    func = input('(a/v/q/c/r/h): ')

    if func.lower() == 'a':
        with open('list.txt', 'a') as f:
            while True:
                task = input('\nEnter a item to add to the list (or type "q" to finish): ')
                if task.lower() == 'q':
                    break
                priority = input('Enter the priority of the task: ')
                if not priority.isdigit() or int(priority) < 1:
                    print('Invalid priority. Please enter a positive integer.')
                    continue
                f.write(f'{counter}. [{priority}] {task}\n')
                counter += 1
    elif func.lower() == 'v':
        try:
            with open('list.txt', 'r') as f:
                print('\nYour To-Do List:')
                print(f.read())
        except FileNotFoundError:
            print('\nNo tasks found. Your list is empty.')
            print('You can add tasks by selecting "a" to add items to your list.')
    elif func.lower() == 'c':
        with open('list.txt', 'w') as f:
            f.write('')
        counter = 1
        print('\nThe list has been cleared.')
    elif func.lower() == 'r':
        while True:
            remove = input('\nEnter the item you want to remove(or press q to quit): ')
            if remove.lower() == 'q':
                break
            with open('list.txt', 'r') as f:
                lines = f.readlines()
            with open('list.txt', 'w') as f:
                for line in lines:
                    if f'{remove}' not in line:
                        f.write(line)
            print(f'Item "{remove}" has been removed from the list.')
    elif func.lower() == 'h':
        try:
            with open('list.txt', 'r') as f:
                lines = f.readlines()
                if not lines:
                    print('\nYour list is empty.')
                    print('You can add tasks by selecting "a" to add items to your list.')
                else:
                    highest_priority_task = max(lines, key=lambda x: int(x.split(']')[0].split('[')[1]))
                    print(f'\nThe task with the highest priority is:\n{highest_priority_task}')
        except FileNotFoundError:
            print('\nNo tasks found. Your list is empty.')
            print('You can add tasks by selecting "a" to add items to your list.')
    elif func.lower() == 'q':
        print('\nExiting the program. Goodbye!')
        break
    else:
        print('\nInvalid input. Please enter "a" to add tasks or "v" to view the list.')

        