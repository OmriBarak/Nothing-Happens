import infoutil

def name(npcID):
    return infoutil.fetch('info', 'npc', itemID)['name']
    
def describe(npcID):
    return infoutil.fetch('info', 'npc', itemID)['description']
