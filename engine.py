import os
import zipfile
import json

import ioutil
import infoutil
import player
import room
import item
import npc
from config import config

print "Checking for save file..."
if not os.path.isfile(config['saveFile'] + '.zip'):
    print "Save file not found. Creating a new save file...",
    infoutil.save()
    print "[Done]"
else: print "Save file found."

def engine_turn():
    pass

while True:
    # Main game loop
    roomDescription = room.make_room_description(playerState['location'], rooms, roomStates, items, npcs, npcStates) # todo: write that function

    command = ' '.split(raw_input(":: "))
    print player.do(command, rooms, playerState, roomStates, items, npcs, npcStates)
    engine_turn()

    # todo: don't save every turn, allow "save" command to prompt save
    save_game(playerState, roomStates, itemStates, npcStates)