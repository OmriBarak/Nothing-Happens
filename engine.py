import os
import zipfile
import json

import files
import room
from config import config

# Init stuff
print "Loading game data..."
rooms, items, npcs = files.load_game_data()

print "Checking for save file..."
if not os.path.isfile(config['saveFile'] + '.zip'):
    print "Save file not found. Creating new save file..."
    # Save default state
    with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
        files.save_game(
            gameFile.read(config['gameFile'] + '/default-states/playerState.json'),
            gameFile.read(config['gameFile'] + '/default-states/roomStates.json'),
            gameFile.read(config['gameFile'] + '/default-states/itemStates.json'),
            gameFile.read(config['gameFile'] + '/default-states/npcStates.json')
        )
else: print "Save file found."

playerState, roomStates, itemStates, npcStates = load_game()

def determine_valid_commands():
    # Commands that are always valid
    validCommands = ["go", "move", "walk", "look", "l", "inventory", "i", "take", "get"]

    # Determind valid movement commands
    movementCommands = {
        'n': ["north", "n"],
        's': ["south", "s"],
        'e': ["east", "e"],
        'w': ["west", "w"],

        'ne': ["northeast", "ne"],
        'nw': ["northwest", "nw"],
        'se': ["southeast", "se"],
        'sw': ["southwest", "sw"],

        'u': ["up", "u"],
        'd': ["down", "d"],
        'i': ["in"],
        'o': ["out", "o"]
    }
    # Find details about the room we're in, see what directions it connects to other rooms in, and append them to the valid command list
    for room in rooms:
        if room['roomID'] == playerState['location']:
            for connection in room['connections']: validCommands.extend(movementCommands[connection['direction']])

    # Find valid special commands enabled by items
    itemCommands = []
    for itemID in playerState['inventory']:
        for gameItem in items:
            if gameItem['itemID'] == itemID:
                for action in gameItem['actions']: validCommands.append(' '.split(action['command']))

    return validCommands

def player_turn(command):
    validCommands = determine_valid_commands()
    command = ' '.split(command.lower())

def engine_turn():
    pass

while True:
    # Main game loop
    roomDescription = room.make_room_description(playerState['location']) # todo: write that function

    command = raw_input(":: ")
    player_turn(command)
    engine_turn()

    # todo: don't save every turn, allow "save" command to prompt save
    save_game(playerState, roomStates, itemStates, npcStates)