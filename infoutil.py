# Game Variable & State Information Utility
# Stores and updates game vars and states for other modules to access and use
import os
import zipfile
import json

import ioutil
from config import filecfg

def player_state():
    # Returns player state dict
    return playerState

def fetch(dataType, objectType, thingID):
    # Returns as dict the state of or info for (as specified in args) a thing (room, item, or NPC) of type and ID specified in args
    thingList = []
    if dataType == 'state':
        # Find states of things
        if objectType == 'item': thingList = itemStates
        elif objectType == 'npc': thingList = npcStates
        elif objectType == 'room': thingList = roomStates

    elif dataType == 'info':
        # Find game info about things
        if objectType == 'item': thingList = gameItems
        elif objectType == 'npc': thingList = gameNpcs
        elif objectType == 'room': thingList = gameRooms

    for thing in thingList:
        if thing["ID"] == thingID:
            return thing

def update_state(objectType, state, status):
    # Updates the state of the given object
    if objectType == 'player': playerState[state] = status
    # todo: update other object types

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