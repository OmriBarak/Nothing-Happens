import os
import zipfile
import json

import files
import player
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

def engine_turn():
    pass

while True:
    # Main game loop
    roomDescription = room.make_room_description(playerState['location'], rooms, roomStates, items, npcs, npcStates) # todo: write that function

    command = ' '.split(raw_input(":: "))
    player.do(command, rooms, playerState)
    engine_turn()

    # todo: don't save every turn, allow "save" command to prompt save
    save_game(playerState, roomStates, itemStates, npcStates)