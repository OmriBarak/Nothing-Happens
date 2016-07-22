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
    for connection in roomInfo['connections']: connections.append((infoutil.name('room', connection['room']), directionLongcodes[connection['direction']]))

    # Format the room information as a string
    itemSentence = u""
    for count, item in enumerate(items):
        itemSentence += u"a(n) " + item
        if len(items) - 2 == count: itemSentence += u", and "
        elif len(items) - 1 != count: itemSentence += u", "
        elif len(items) - 1 == count: itemSentence += u" are here."

    npcSentence = u""
    for count, npc in enumerate(npcs):
        npcSentence += npc
        if len(npcs) - 2 == count: npcSentence += u", and "
        elif len(npcs) - 1 != count: npcSentence += u", "
        if len(npcs) > 1 and len(npcs) - 1 == count: npcSentence += u" are here."
        elif len(npcs) == 1 and len(npcs) - 1 == count: npcSentence += u" is here."

    connectionSentence = u""
    if len(connections) > 1: connectionSentence += u"There is "
    for connection in connections:
        connectionSentence += u"a(n)" connection[0] + u" to the " + connection[1]
        if len(connections) - 2 == count: connectionSentence += u", and "
        elif len(connections) - 1 != count: connectionSentence += u", "
        elif len(conncetions) - 1 == count: connectionSentence += u"."

    passageList = [description, itemSentenece, npcSentence, connectionSentence]
    passageStr = u""
    for sentence in passageList:
        if sentence != u"": passageStr += sentence[0].upper() + sentence[1:] + u" "
    return title + u"\n\n" + passageStr

def get_valid_directions(roomID):
    ## Takes roomID, returns list of (direction shortcode, room ID) tuples
    validDirections = []
    for connection in infoutil.fetch('info', 'room', roomID)['connections']: validDirections.append(connection['direction'], connection['room'])
    return validDirections