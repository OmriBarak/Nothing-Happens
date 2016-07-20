import os
import shutil
import zipfile
import json

from config import config

def load_game():
    with zipfile.ZipFile(config['saveFile'] + '.zip') as saveFile:
        playerState = saveFile.read('_SAVE/playerState.json')
        roomStates = saveFile.read('_SAVE/roomStates.json')
        itemStates = saveFile.read('_SAVE/itemStates.json')
        npcStates = saveFile.read('_SAVE/npcStates.json')
    return playerState, roomStates, itemStates, npcStates

def save_game(playerState, roomStates, itemStates, npcStates):
    print "Saving..."
    # Create a temporary save folder
    os.makedirs('_SAVE')

    # Put our save data in the folder
    with open('_SAVE/playerState.json', 'w') as statesFile: statesFile.write(playerState)
    with open('_SAVE/roomStates.json', 'w') as statesFile: statesFile.write(roomStates)
    with open('_SAVE/itemStates.json', 'w') as statesFile: statesFile.write(itemStates)
    with open('_SAVE/npcStates.json', 'w') as statesFile: statesFile.write(npcStates)

    # Create a zip archive and add our save data
    with zipfile.ZipFile(config['saveFile'] + '.zip', 'w') as saveFile:
        saveFile.write('_SAVE/playerState.json')
        saveFile.write('_SAVE/roomStates.json')
        saveFile.write('_SAVE/itemStates.json')
        saveFile.write('_SAVE/npcStates.json')

    # Delete the temporary save folder
    shutil.rmtree('_SAVE')
    print "Saved."

# Prepare game data and save file
print "Loading game data..."
with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
    rooms = json.loads(gameFile.read(config['gameFile'] + '/rooms.json'))
    items = json.loads(gameFile.read(config['gameFile'] + '/items.json'))
    npcs = json.loads(gameFile.read(config['gameFile'] + '/npcs.json'))

print "Checking for save file..."
if not os.path.isfile(config['saveFile'] + '.zip'):
    print "Save file not found. Creating new save file..."
    # Save default state
    with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
        save_game(
            gameFile.read(config['gameFile'] + '/default-states/playerState.json'),
            gameFile.read(config['gameFile'] + '/default-states/roomStates.json'),
            gameFile.read(config['gameFile'] + '/default-states/itemStates.json'),
            gameFile.read(config['gameFile'] + '/default-states/npcStates.json')
        )
else: print "Save file found."

playerState, roomStates, itemStates, npcStates = load_game()

def determine_valid_commands():
    # Movement
    goCommands = ["go", "move", "walk"]

    nCommands = ["north", "n"]
    sCommands = ["south", "s"]
    eCommands = ["east", "e"]
    wCommands = ["west", "w"]

    neCommands = ["northeast", "ne"]
    nwCommands = ["northwest", "nw"]
    seCommands = ["southeast", "se"]
    swCommands = ["southwest", "sw"]

    upCommands = ["up", "u"]
    downCommands = ["down", "d"]
    inCommands = ["in"]
    outCommands = ["out", "o"]

    # todo: Special commands enabled by items

    # Commands that are always valid
    validCommands = ["look", "l", "inventory", "i", "take", "get"]

def player_turn(command):
    command = ' '.split(command.lower())

def engine_turn():
    pass

while True:
    # Main game loop
    command = raw_input(":: ")
    player_turn(command)
    engine_turn()