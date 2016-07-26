import infoutil
import room
import item
import npc

# Command types
movementCommands = ["go", "move", "walk"]
directionCommands = ["n", "north", "s", "south", "e", "east", "w", "west", "ne", "northeast", "nw", "northwest", "se", "southeast", "sw", "southwest", "u", "up", "d", "down", "in", "o", "out"]

viewCommands = ["look", "l"]
invCommands = ["inventory", "inv", "i"]

invManagementCommands = ["take", "get", "drop"]
usageCommands = ["use"]

movementIntents = movementCommands + directionCommands
informationIntents = viewCommands + invCommands
interactionIntents = invManagementCommands + usageCommands

directionMap = {
    'n': ["north", "n"], 's': ["south", "s"], 'e': ["east", "e"], 'w': ["west", "w"],
    'ne': ["northeast", "ne"], 'nw': ["northwest", "nw"], 'se': ["southeast", "se"], 'sw': ["southwest", "sw"],
    'u': ["up", "u"], 'd': ["down", "d"], 'i': ["in"], 'o': ["out", "o"]
}

def list_inventory():
    return infoutil.player_state()['inventory']

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
            break
        
        # Get the direction's shortcode
        for shortcode in directionMap.keys():
            if direction in directionMap[shortcode]:
                directionShortcode = shortcode
                break

        # Check to see if there is a room in that direction from the player's room
        destination = ""
        for connection in room.list_connections(infoutil.player_state()['location']):
            if directionShortcode in connection[2]:
                destination = connection[0]
                direction = connection[3]
                break
        
        if destination == "":
            return "There is no room in that direction."       # Fail state
        else:
            # Move the player
            infoutil.update_state('player', 'location', destination)
            return "You move " + direction + "... \n" + room.describe(destination)

    elif intent == "INFO":
        # Catch inventory-related commands right off the bat (inventory, i, look inventory, l inv, etc.)
        inventoryList = []
        for invCommand in invCommands:
            if invCommand in command:
                for itemID in list_inventory():
                    inventoryList.append(item.name(itemID)[0].upper() + item.name(itemID)[1:] + u"\n")
                return u"You have:\n" + ''.join(inventoryList)

        if command[0] in viewCommands:
            if len(command) == 1 or command[1] == "room":       # Look room
                return room.describe(infoutil.player_state()['location'])
            else:       # Look [object]
                #check if [object] is an npc
                for npci in room.list_npcs(infoutil.player_state()['location']):
                    if command[1].lower() == npci[1].lower(): return npc.describe(npci[0])
                
                #check if [object] is an item
                # todo: add inventory items in (itemID, u"item name") format
                for itemi in room.list_items(infoutil.player_state()['location']):
                    if command[1].lower() == itemi[1].lower(): return item.describe(itemi[0])
                
                #else
                return "No such object exists." #TODO: phrase better
            #TODO: test if this works

    elif intent == "INTERACT": pass     # todo
