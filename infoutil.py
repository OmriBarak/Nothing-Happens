# Game Variable & State Information Utility
# Stores and updates game vars and states for other modules to access and use
import zipfile
import json

import ioutil

print "Loading game data..."
# Load game data
gameRooms, gameNpcs, gameItems =  ioutil.load_game_data()

# Load save data
playerState, roomStates, itemStates, npcStates = ioutil.load_save()

def player_state():
    # Returns player state dict
    return playerState

def fetch(thingType, objectType, thingID):
    ## Returns as dict the state of or info for (as specified in args) a thing (room, item, or NPC) of type and ID specified in args
    if thingType == 'state':
        # Find states of things
        if thingType == 'item': thingList = itemStates
        elif thingType == 'npc': thingList = npcStates
        elif thingType == 'room': thingList = roomStates

    elif thingType == 'info':
        # Find game info about things
        if thingType == 'item': thingList = gameItems
        elif thingType == 'npc': thingList = gameItems
        elif thingType == 'room': thingList = gameRooms

    for thing in stateList:
        if thing["ID"] == thingID:
            return thing

def name(objectType, thingID):
    ## Returns as string the name/title of whatever the thingID specified in args
    return infoutil.fetch('info', 'room', roomID)['title']

def save():
    ioutil.save_game(playerState, roomStates, itemStates, npcStates)