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
    # Returns as dict the state of a thing (room, item, or NPC) of type and ID specified in args
    if thingType == 'item': stateList = itemStates
    elif thingType == 'npc': stateList = npcStates
    elif thingType == 'room': stateList = roomStates

    for thing in stateList:
        if thing["ID"] == thingID:
            return thing

def thing(thingType, thingID):
    # Returns as dict the game object of a thing (room, item, or NPC) of type and ID specified in args
    if thingType == 'item': thingList = gameItems
    elif thingType == 'npc': thingList = gameNpcs
    elif thingType == 'room': thingList = gameRooms

    for thing in thingList:
        if thing["ID"] == thingID:
            return thing