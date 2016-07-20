import room

# Command types
movementCommands = ["go", "move", "walk"]
directionCommands = ["n", "north", "s", "south", "e", "east", "w", "west", "ne", "northeast", "nw", "northwest", "se", "southeast", "sw", "southwest", "u", "up", "d", "down", "in", "o", "out"]

viewCommands = ["look", "l"]
invCommands = ["inventory", "inv", "i"]

retrievalCommands = ["take", "get"]
usageCommands = ["use"]

# Direction map
directionDict = {
    'n': ["north", "n"], 's': ["south", "s"], 'e': ["east", "e"], 'w': ["west", "w"],
    'ne': ["northeast", "ne"], 'nw': ["northwest", "nw"], 'se': ["southeast", "se"], 'sw': ["southwest", "sw"],
    'u': ["up", "u"], 'd': ["down", "d"], 'i': ["in"], 'o': ["out", "o"]
}

def do(command, rooms, playerState):
    global command, rooms, playerState
    validCommands = determine_valid_commands()
    intent = determine_command_intent()

    if command[0] not in validCommands: print "[WARN] Invalid command detected!"
    if intent = "MOVE": result = do_move()
    elif intent = "INFO": result = do_info()
    elif intent = "INTERACT": result = do_interact()

    return result

def determine_valid_commands():
    # Commands that are always valid
    validCommands = movementCommands + viewCommands + invCommands + retrievalCommands + usageCommands

    # Determine valid movement commands
    # Find details about the room we're in, see what directions it connects to other rooms in, and append them to the valid command list
    for direction in room.get_valid_directions(playerState['location'], rooms):
        if direction[0] in movementDict.keys():
            validCommands.extend(movementDict[direction[0]])

    # Find valid special commands enabled by items
    itemCommands = []
    for itemID in playerState['inventory']:
        for gameItem in items:
            if gameItem['itemID'] == itemID:
                for action in gameItem['actions']: validCommands.append(' '.split(action['command']))

    print "[DEBUG] Valid commands: " + str(validCommands)
    return validCommands

def determine_command_intent():
    movementIntents = movementCommands + directionCommands
    informationIntents = viewCommands + invCommands
    interactionIntents = retrievalCommands + usageCommands
    # Try to determine what kind of command we're working with
    if command[0] in movementIntents: intent = "MOVE"
    elif command[0] in informationIntents: intent = "INFO"
    else: intent = "INTERACT"
    return intent

def do_move():
    if command[0] in movementCommands:
        if command[1] in directionCommands: directionCommand = command[1]
    elif command[0] in directionCommands: directionCommand = command[0]

    # Translate the command into direction shortcodes
    for shortcode in directionDict.keys():
        if directionCommand in directionDict[shortcode]:
            direction = shortcode
            break

    # Move the player along the chosen direction to their target location
    for room in rooms:
        if room['roomID'] == playerState['location']:
            for connection in connections:
                if connection['direction'] == direction: 
                    playerState['location'] = connection['room']
                    return "Moved player to " + playerState['location']

def do_info():
    pass

def do_interact():
    pass