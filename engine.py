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
    print "Save file not found. Creating new save file..."
    # Save default state
    with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
        saveGame(
            gameFile.read(config['gameFile'] + '/default-states/playerState.json'),
            gameFile.read(config['gameFile'] + '/default-states/roomStates.json'),
            gameFile.read(config['gameFile'] + '/default-states/itemStates.json'),
            gameFile.read(config['gameFile'] + '/default-states/npcStates.json')
        )
else: print "Save file found."

def loadGame():
    pass

def saveGame(playerState, roomStates, itemStates, npcStates):
    print "Saving..."
    # Create a temporary save folder
    os.makedirs('_SAVE')

    # Put our save data in the folder
    with open('_SAVE/playerState.json', 'w') as statesFile: statesFile.write(playerState)
    with open('_SAVE/roomStates.json', 'w') as statesFile: statesFile.write(roomStates)
    with open('_SAVE/itemStates.json', 'w') as statesFile: statesFile.write(itemStates)
    with open('_SAVE/npcStates.json', 'w') as statesFile: statesFile.write(npcStates)

    # Create a zip archive and add our save data
    saveFile = zipfile.ZipFile(config['saveFile'] + '.zip', 'w')
    saveFile.write('_SAVE/playerState.json')
    saveFile.write('_SAVE/roomStates.json')
    saveFile.write('_SAVE/itemStates.json')
    saveFile.write('_SAVE/npcStates.json')

    # Close the zip file and delete the temporary save folder
    saveFile.close()
    shutil.rmtree('_SAVE')
    print "Saved."

def playerTurn(command):
    pass

def engineTurn():
    pass

while True:
    # Main game loop
    command = raw_input(":: ")
    playerTurn(command)
    engineTurn()