

def printMenu():
    print('Options')
    print('    [C]reate new entry')
    print('    [R]replace an entry')
    print('    [U]pdate entry order')
    print('    [D]elete entry')
    print('    [L]ist all entries')
    print('    [Q]uit')

def create_entry():
    new_entry = input('What would you like to add to your todo list? ')
    todo_list.append(new_entry)
    print('New item added to your todo list: ' + new_entry)
    return

def replace_entry():
    list_entries()
    replace_item = int(input('Which item would you like to replace: '))
    new_item = input('What new item would you like to replace ' + todo_list[replace_item] + 'with: ')
    todo_list[replace_item] = new_item
    list_entries()
    return

def update_entry():
    list_entries()
    update_item = int(input('Which item would you like to move: '))
    temp_item = todo_list.pop(update_item)
    list_entries()
    new_location = int(input('Where would you like to insert: ' + temp_item))
    todo_list.insert(new_location, temp_item)
    print('Updated todo list')
    list_entries()
    return

def delete_entry():
    list_entries()
    remove_item = int(input('What number would you like to remove: '))
    remove_item =- 1
    todo_list.pop(remove_item)
    return

def list_entries():
    print('Current todo list items: ')
    print(todo_list)
    return



print('Welcome to the lame TODO app!')
menu_choice = None

# testing entries for quick development
# todo_list = ['Joshua', 'Alice', 'Bob', 'Randal']
todo_list = []

while menu_choice != 'Q':
    printMenu()
    menu_choice = input('Would you like to do:').capitalize()

    if menu_choice == 'C':
        create_entry()
    elif menu_choice == 'R':
        replace_entry()
    elif menu_choice == 'U':
        update_entry()
    elif menu_choice == 'D':
        delete_entry()
    elif menu_choice == 'L':
        list_entries()
    elif menu_choice == 'Q':
        print('Exiting, goodbye!')
        exit(0)
    else:
        unknown_entry_string = 'Sorry the entry provided is not know: ' + menu_choice
        print(unknown_entry_string)
