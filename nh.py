import ioutil
import infoutil
import player
import room
import item
import npc

def engine_turn():
    # Move npcs, increment timers
    pass

while True:
    ## Main game loop
    # Get the player's location
    playerState = infoutil.player_state()
    playerLocation = playerState['location']

    # Get the player's command
    command = raw_input(infoutil.name('room', playerLocation).upper() + " :: ").lower().split(' ')
    print player.do(command)
    engine_turn()