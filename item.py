import infoutil

def name(itemID):
    return infoutil.fetch('info', 'item', itemID)['name']