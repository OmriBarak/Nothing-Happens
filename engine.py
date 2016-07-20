import os
import shutil
import zipfile
import json

from config import config

# Prepare game data and save file
print "Loading game data..."
with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
    rooms = json.loads(gameFile.read(config['gameFile'] + '/rooms.json'))
    items = json.loads(gameFile.read(config['gameFile'] + '/items.json'))
    npcs = json.loads(gameFile.read(config['gameFile'] + '/npcs.json'))

print "Checking for save file..."
if not os.path.isfile(config['saveFile'] + '.zip'):
    print "Creating new save file...",
    # Create a temporary save folder
    os.makedirs('_SAVE')

    # Copy the over game's default states
    with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
        with open('_SAVE/roomStates.json', 'w') as roomStatesFile: roomStatesFile.write(gameFile.read(config['gameFile'] + '/roomStates.json'))
        with open('_SAVE/itemStates.json', 'w') as itemStatesFile: itemStatesFile.write(gameFile.read(config['gameFile'] + '/itemStates.json'))
        with open('_SAVE/npcStates.json', 'w') as npcStatesFile: npcStatesFile.write(gameFile.read(config['gameFile'] + '/npcStates.json'))

    # Create a zip archive and add our save data
    saveFile = zipfile.ZipFile(config['saveFile'] + '.zip', 'w')
    saveFile.write('_SAVE/roomStates.json')
    saveFile.write('_SAVE/itemStates.json')
    saveFile.write('_SAVE/npcStates.json')

    # Close the zip file and delete the temporary save folder
    saveFile.close()
    shutil.rmtree('_SAVE')
    print "[Done]"
else: print "Save file exists. Continuing..."