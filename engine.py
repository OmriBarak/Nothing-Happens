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
    gameRooms = json.loads(gameFile.read(config['gameFile'] + '/rooms.json'))
    gameItems = json.loads(gameFile.read(config['gameFile'] + '/items.json'))
    gameNPCs = json.loads(gameFile.read(config['gameFile'] + '/npcs.json'))

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
    for room in gameRooms:
        if room['roomID'] == playerState['location']:
            for connection in room['connections']: validCommands.extend(movementCommands[connection['direction']])

    # Find valid special commands enabled by items
    itemCommands = []
    for itemID in playerState['inventory']:
        for gameItem in gameItems:
            if gameItem['itemID'] == itemID:
                for action in gameItem['actions']: validCommands.append(' '.split(action['command']))

    return validCommands

def player_turn(command):
    command = ' '.split(command.lower())

def engine_turn():
    pass

while True:
    # Main game loop
    command = raw_input(":: ")
    player_turn(command)
    engine_turn()