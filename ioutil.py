# I/O Utility
# For interacting with .zip files and the filesystem
import shutil
import zipfile

from config import cfg

def load_save():
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

def load_game_data():
    with zipfile.ZipFile(config['gameFile'] + '.zip') as gameFile:
        rooms = json.loads(gameFile.read(config['gameFile'] + '/rooms.json'))
        items = json.loads(gameFile.read(config['gameFile'] + '/items.json'))
        npcs = json.loads(gameFile.read(config['gameFile'] + '/npcs.json'))

    return rooms, items, npcs