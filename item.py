import infoutil

def name(itemID):
    return infoutil.fetch('info', 'item', itemID)['name']
    
def describe(itemID):
    return infoutil.fetch('info', 'item', itemID)['description']

def synonyms(itemID):
    return infoutil.fetch('info', 'item', itemID)['synonyms'].split(', ')