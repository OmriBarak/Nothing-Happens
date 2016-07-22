# Game Variables & States
# Stores and updates game vars and states for other modules to access and use
import zipfile
import json

import ioutil

# Load game data
gameRooms, gameNpcs, gameItems =  ioutil.load_game_data()

# Load save data
playerState, roomStates, itemStates, npcStates = ioutil.load_save()

def player_state():
    # Returns player state dict
    return playerState

def state(thingType, thingID):
    # Returns the state of a thing (room, item, or NPC) of type specified in args as a dict
    if thingType == 'item': stateList = itemStates
    elif thingType == 'npc': stateList = npcStates
    elif thingType == 'room': stateList = roomStates

    for thing in stateList:
        if thing["ID"] == thingID:
            return thing
    return {}       # If no thing with a matching ID is found, return an empty dict