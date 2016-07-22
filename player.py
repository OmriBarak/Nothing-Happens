import infoutil
import room

# Command types
movementCommands = ["go", "move", "walk"]
directionCommands = ["n", "north", "s", "south", "e", "east", "w", "west", "ne", "northeast", "nw", "northwest", "se", "southeast", "sw", "southwest", "u", "up", "d", "down", "in", "o", "out"]

viewCommands = ["look", "l"]
invCommands = ["inventory", "inv", "i"]

retrievalCommands = ["take", "get"]
usageCommands = ["use"]

movementIntents = movementCommands + directionCommands
informationIntents = viewCommands + invCommands
interactionIntents = retrievalCommands + usageCommands

directionMap = {
    'n': ["north", "n"], 's': ["south", "s"], 'e': ["east", "e"], 'w': ["west", "w"],
    'ne': ["northeast", "ne"], 'nw': ["northwest", "nw"], 'se': ["southeast", "se"], 'sw': ["southwest", "sw"],
    'u': ["up", "u"], 'd': ["down", "d"], 'i': ["in"], 'o': ["out", "o"]
}
def do(command):
    ## Attempts to make the player character do the player's command

    # Determine player intent
    if command[0] in movementIntents: intent = "MOVE"
    elif command[0] in informationIntents: intent = "INFO"
    else: intent = "INTERACT"

    # Attempt to execute the command
    if intent = "MOVE":
        # Find the direction part of the command
        direction = ""
        for word in command:
            if word in directionCommands: direction = word
        
        # Get the direction's shortcode
        for shortcode in directionMap.keys():
            if direction in directionMap[shortcode]:
                directionShortcode = shortcode
                break

        # Check to see if there is a room in that direction from the player's room
        destination = ""
        for connection in room.connections(infoutil.player_state()['location']):
            if directionShortcode in connection[2]:
                destination = connection[0]
                break
        
        if destination = "": return "There is no room in that direction."       # Fail state
        else:
            # todo: update location

    elif intent = "INFO": result = get_info(command)
    elif intent = "INTERACT": result = interact(command)

    return result

def move():
    if command[0] in movementCommands:
        if command[1] in directionCommands: directionCommand = command[1]
    elif command[0] in directionCommands: directionCommand = command[0]

    # Translate the command into direction shortcodes
    for shortcode in directionMap.keys():
        if directionCommand in directionMap[shortcode]:
            direction = shortcode
            break

    # Move the player along the chosen direction to their target location
    for room in rooms:
        if room['roomID'] == playerState['location']:
            for connection in connections:
                if connection['direction'] == direction: 
                    playerState['location'] = connection['room']
                    return "Moved player to " + playerState['location']

def get_info(roomStates, items, npcs, npcStates):
    if command[0] in viewCommands:
        inventoryItems = []
        for itemID in playerState['inventory']:
            for item in items:
                if item['itemID'] == itemID:
                    inventoryItems.append((item['name'] + item['synonyms'], itemID))
                    break

        if len(command) = 1 or command[1] in room.get_room_name(playerState['location'], rooms): return room.make_room_description(playerState['location'], rooms, roomStates, items, npcs, npcStates)
        else:
            for invItem in inventoryItems:
                if command[1] in invItem[0]:
                    for item in items:
                        if item['itemID'] == invItem[1]: return item['description']
    
    elif command[0] in invCommands:
        # todo: list items player has

def interact():
    pass