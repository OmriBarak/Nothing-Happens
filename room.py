def make_room_description(roomID):
    pass

def get_valid_directions(roomID, rooms):
    # Takes current roomID and game room data input, returns list of (direction, roomID) tuples
    validDirections = []
    for room in rooms:
        if room['roomID'] == roomID:
            for connection in room['connections']:
                validDirections.append(connection['direction'], connection['room'])
    return validDirections