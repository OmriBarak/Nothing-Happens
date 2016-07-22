import infoutil

def title(roomID):
    ## Get the title of a room and return it as a string
    return infoutil.fetch('info', 'room', roomID)['title']

def describe(roomID):
    ## Create and return a description of the roomID in argument
    # Get room information and state from the game's data files
    roomInfo = infoutil.fetch('info', 'room', roomID)
    roomState = infoutil.fetch('state', 'room', roomID)

    # Get the room's title and description
    title = title(roomID)
    description = room['description'] + describe_item_info(roomStates) + describe_npc_info(npcs, npcStates), describe_connection_info()

    # Get items in the room
    for item in roomState['items']:
        # Get item names



def describe_item_info(roomStates):
    for room in roomStates:
        if room['roomID'] == roomID:
            roomItems = room['items']
            break
    
    itemList = []
    for roomItem in roomItems:
        for item in items:
            if item['itemID'] == roomItem:
                itemList.append(item["name"])
                break

    itemInfo = "There is "
    for room, count in enumerate(itemList):
        if len(itemList) > 1 and count + 1 == len(itemList): itemInfo += "and "
        itemInfo += "a(n) " + room[0]
        if count+1 < len(itemList): itemInfo += ", "
        else: itemInfo += "here. "
    return itemInfo

def describe_npc_info(npcs, npcStates):
    npcIDs = []
    for npc in npcStates:
        if npc['location'] == roomID: npcIDs.append(npc['npcID'])

    npcNames = []
    for npcID in npcIDs:
        for npc in npcs:
            if npc['npcID'] == npcID: 
                npcNames.append(npc['name'])
                break

    npcInfo = ""
    for name, count in enumerate(npcNames):
        if len(npcNames) > 1: 
            if count+1 != len(npcNames): npcInfo += name + ", "
            else: npcInfo += "and " + npcInfo + " are here. "
        else: npcInfo += name + " is here. "
    return npcInfo

directions = {
    "n": "North", "s": "South", "e": "East", "w": "West", 
    "ne": "North-East", "nw": "North-West", "se": "South-East", "sw": "South-West",
    "u": "up", "d": "down", "i": "in", "o": "out"
}
def describe_connection_info():
    connectionInfo = "There is "
    connectionInfoTuples = []
    for direction in get_valid_directions(roomID, rooms):
        for room in rooms:
            if room['roomID'] == direction['roomID']: connectionInfoTuples.append(room['title'], direction)

    for room, count in enumerate(connectionInfoTuples):
        if len(connectionInfoTuples) > 1 and count + 1 == len(connectionInfoTuples): connectionInfo += "and "
        connectionInfo += "a(n) " + room[0] + " to the " + room[1]
        if count+1 < len(connectionInfoTuples): connectionInfo += ", "
        else: connectionInfo += "."
    return connectionInfo

def get_room_name(roomID, rooms):
    for room in rooms:
        if room['roomID'] == roomID:
            return room['title']

def get_valid_directions(roomID, rooms):
    # Takes current roomID and game room data input, returns list of (direction, roomID) tuples
    validDirections = []
    for room in rooms:
        if room['roomID'] == roomID:
            for connection in room['connections']:
                validDirections.append(connection['direction'], connection['room'])
    return validDirections