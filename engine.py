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
    ## Main game loop
    # Get the player's location
    playerLocation = infoutil.player_state()['location']

    # Describe the room
    print room.describe(playerLocation)

    # Get the player's command
    command = ' '.split(raw_input(":: "))
    print player.do(command)
    engine_turn()