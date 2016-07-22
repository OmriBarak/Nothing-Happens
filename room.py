import infoutil

directionsLongcodes = {
    "n": "North", "s": "South", "e": "East", "w": "West", 
    "ne": "North-East", "nw": "North-West", "se": "South-East", "sw": "South-West",
    "u": "up", "d": "down", "i": "in", "o": "out"
}

def describe(roomID):
    ## Create and return a description of the roomID in argument
    # Get room information and state from the game's data files
    roomInfo = infoutil.fetch('info', 'room', roomID)
    roomState = infoutil.fetch('state', 'room', roomID)

    # Get the room's name and description
    name =  infoutil.name('room', roomID)
    description = room['description']

    # Get items in the room
    items = []
    for itemID in roomState['items']: items.append(infoutil.name('item', itemID))
    
    # Get NPCs in the room
    npcs = []
    for npc in infoutil.npcStates:
        if npc['location'] == roomID: npcs.append(infoutil.name('npc', npc['ID']]))

    # Get directions to and information about remote rooms
    connections = []
    for connection in roomInfo['connections']: connections.append((directionLongcodes[connection['direction']], infoutil.name('room', connection['room'])))

def get_valid_directions(roomID):
    ## Takes roomID, returns list of (direction shortcode, room ID) tuples
    validDirections = []
    for connection in infoutil.fetch('info', 'room', roomID)['connections']: validDirections.append(connection['direction'], connection['room'])
    return validDirections