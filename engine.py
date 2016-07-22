import ioutil
import infoutil
import player
import room
import item
import npc

def engine_turn():
    pass

while True:
    ## Main game loop
    # Get the player's location
    playerState = infoutil.player_state()
    playerLocation = playerState['location']

    # Describe the room
    print room.describe(playerLocation)

    # Get the player's command
    command = ' '.split(raw_input(":: "))
    print player.do(command)
    engine_turn()