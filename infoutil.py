# Game Variable & State Information Utility
# Stores and updates game vars and states for other modules to access and use
import os
import zipfile
import json

import ioutil
from config import filecfg

def fetch(dataType, objectType, thingID=""):
    ## Returns the state of or info for (as specified in args) a thing (room, item, or NPC) of type and ID specified in args
    #  Note that 'player' objectTypes don't require a thingID
    thingList = []
    if dataType == 'state':
        # Find states of things
        if objectType == 'item': thingList = itemStates
        elif objectType == 'npc': thingList = npcStates
        elif objectType == 'room': thingList = roomStates

        elif objectType == 'player': return playerState

    elif dataType == 'info':
        # Find game info about things
        if objectType == 'item': thingList = gameItems
        elif objectType == 'npc': thingList = gameNpcs
        elif objectType == 'room': thingList = gameRooms

    for thing in thingList:
        if thing["ID"] == thingID:
            return thing

def update_state(objectType, state, status, thingID=""):
    # Updates the state of the given object
    # todo: Make this work without extra code for 'player' objectType
    if objectType == 'player': playerState[state] = status
    elif objectType == 'room': 
        for count, room in enumerate(roomStates):
            if room["ID"] == thingID: room[state] = status

def add_item():
    # todo: write add_item()
    pass

def remove_item(holderObjectType, itemID, holderID=""):
    # Removes item with ID itemID from its holder with ID holderID
    heldItems = fetch('state', holderObjectType, holderID)['inventory']
    update_state(holderObjectType, 'inventory', roomItems.remove(itemID), holderID)

def name(objectType, thingID):
    # Returns as string the name of whatever the thingID specified in args
    return fetch('info', objectType, thingID)['name']

def save():
    ioutil.save_game(playerState, roomStates, itemStates, npcStates)

print "Loading game data..."
# Load game data
gameRooms, gameItems, gameNpcs, playerState, roomStates, itemStates, npcStates =  ioutil.load_game_data()

print "Checking for save file..."
if not os.path.isfile(filecfg['saveFile'] + '.zip'):
    print "Save file not found. Creating a new save file..."
    save()
else: print "Save file found."

# Load save data
playerState, roomStates, itemStates, npcStates = ioutil.load_save()