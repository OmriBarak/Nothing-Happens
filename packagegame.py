# Game Package Builder
# Basically takes game src and stuffs it into a .zip so we don't have to. Very similar to ioutil but only has build-related stuff
import zipfile

from config import buildcfg

print "Building game from " + buildcfg['srcFolder'] + "..."
# Create a zip archive and add the game data
with zipfile.ZipFile(buildcfg['buildFile'] + '.zip', 'w') as buildFile:
    buildFile.write(buildcfg['srcFolder'] + '/items.json')
    buildFile.write(buildcfg['srcFolder'] + '/npcs.json')
    buildFile.write(buildcfg['srcFolder'] + '/rooms.json')
    buildFile.write(buildcfg['srcFolder'] + '/states/itemStates.json')
    buildFile.write(buildcfg['srcFolder'] + '/states/npcStates.json')
    buildFile.write(buildcfg['srcFolder'] + '/states/roomStates.json')
    buildFile.write(buildcfg['srcFolder'] + '/states/playerState.json')
print "Done."