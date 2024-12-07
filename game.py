from modules.classes import *
import modules.lootbox_functions as lootbox
import json
import readline

current_save_file = 'savedata.dat'
player = None

def process_input(input_string):

    
    split_string = input_string.split()
    command = split_string[0]

    try:
        arg = split_string[1]
    except:
        arg = None

    if command == 'help':
        print('this is the help text')
        return

    if command == 'open':
        open_box(player)
        return

    if command == 'quit':
        quit_game(player)
        return

    if command == 'inventory':
        player.print_inventory()
        return

    if command == 'load':
        if arg is not None:
            player = load_file(arg)
        else:
            print('filename not provided')
        return

    if command == 'save':
        player.save(current_save_file)
        return

    if command == 'saveto':
        if arg is not None:
            player.save(arg)
        else:
            print('filename not provided')
        return

    print('invalid command')
            

def open_box():
    player.add_item(lootbox.common())

def quit_game():
    player.save()
    print('goodbye')
    quit()

def load_file(filename = current_save_file):
    try:
        save = open(filename, 'r')
        print('Save data found! Loading save data...')
        save_dict = json.loads(save.read())
        save.close()
        player = Player(save_dict['inventory'], save_dict['currency'])
        player.load_inventory()
    except Exception as e:
        print(e)
        if filename != 'savedata.dat':
            print('Save data not found or corrupted... loading savedata.dat')
            player = load_file()
        else:
            print('No save data found. Creating save data...')
            save = open(filename, 'w')
            player = Player()
            save.write(json.dumps(player.__dict__))
            save.close()

    global current_save_file
    current_save_file = filename
    print(current_save_file)
    

def start_game():
    
    load_file()

    while True:
        command = input('> ')
        process_input(command)

    print('---Code execution successful---')