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
    if intent == "MOVE":
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
                direction = connection[3]
                break
        
        if destination == "": return "There is no room in that direction."       # Fail state
        else:
            # Move the player
            infoutil.update_state('player', 'location', destination)
            return "You move " + direction + "..."

    elif intent == "INFO": pass     # todo
    elif intent == "INTERACT": pass     # todo

    return result