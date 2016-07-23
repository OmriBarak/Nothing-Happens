import infoutil

def name(itemID):
    return infoutil.fetch('info', 'item', itemID)['name']
    
def describe(itemID):
    return infoutil.fetch('info', 'item', itemID)['description']
