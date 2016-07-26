import infoutil
import room
import item
import npc

# Command types
movementCommands = [u"go", u"move", u"walk"]
directionCommands = [u"n", u"north", u"s", u"south", u"e", u"east", u"w", u"west", u"ne", u"northeast", u"nw", u"northwest", u"se", u"southeast", u"sw", u"southwest", u"u", u"up", u"d", u"down", u"in", u"o", u"out"]

viewCommands = [u"look", u"l"]
invCommands = [u"inventory", u"inv", u"i"]

invManagementCommands = [u"take", u"get", u"drop", u"put", u"place"]
usageCommands = [u"use"]

moveIntents = movementCommands + directionCommands
lookIntents = viewCommands + invCommands
interactIntents = invManagementCommands + usageCommands

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
    if command[0] in moveIntents: intent = "MOVE"
    elif command[0] in lookIntents: intent = "LOOK"
    else: intent = "INTERACT"

    # Attempt to execute the command
    if intent == "MOVE": return move(command)
    elif intent == "LOOK": return look(command)
    elif intent == "INTERACT": return interact(command)

def move(command):
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
        return u"There is no room in that direction."       # Fail state
    else:
        # Move the player
        infoutil.update_state('player', 'location', destination)
        return u"You move " + direction + "..." + room.describe(destination)

def look(command):
    # Find the thing to look at in the command
    lookTarget = ""
    for word in command:
        if word not in viewCommands + [u"at"]:
            lookTarget = word
            break
    if lookTarget == "": lookTarget = u"room"

    # Look inventory, inventory, i, look inv, etc.
    inventoryList = []
    if lookTarget in invCommands:
        for itemID in list_inventory(): inventoryList.append(item.name(itemID)[0].upper() + item.name(itemID)[1:])
        return u"You have:\n" + '\n'.join(inventoryList)

    # Look room
    if lookTarget == u"room": return room.describe(infoutil.player_state()['location'])

    # Look [object]
    else:
        # check if [object] is an npc
        for npci in room.list_npcs(infoutil.player_state()['location']):
            if lookTarget.lower() == npci[1]: return npc.describe(npci[0])
        
        # check if [object] is an item
        # Get the names of held items
        invItems = []
        for invItem in list_inventory(): invItems.append((invItem, infoutil.name('item', invItem)))

        # Look for the item in the command in a list of items in the room and held items
        for itemi in room.list_items(infoutil.player_state()['location']) + invItems:
            if lookTarget.lower() == itemi[1] or lookTarget in item.synonyms(itemi[0]): return item.describe(itemi[0])
        
        # if the item/npc isn't found
        return u"You can\'t see that here!"

def interact(command):
    # Take/get [object]
    if command[0] in [u"take", u"get"]:
        pass

    # Drop [object], put (down) [object], etc.
    elif command[0] in [u"drop", u"put", u"place"]:
        pass

    # todo: use [x] on [y]
    # todo: item commands