import zipfile
import json

from config import config

gameFile = zipfile.ZipFile(config['gameFile'] + '.zip')

rooms = json.loads(gameFile.read(config['gameFile'] + '/rooms.json'))
items = json.loads(gameFile.read(config['gameFile'] + '/items.json'))
npcs = json.loads(gameFile.read(config['gameFile'] + '/npcs.json'))

print rooms, items, npcs