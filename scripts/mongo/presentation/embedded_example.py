import pymongo

def embedded_query(db):
    yield db.collectionInventory.find({'size': { 'h': 14, 'w': 21, 'uom': "cm" }})
    #({ "size.uom": "in" }) //nested
count = 0
if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.get_database('inventory')
    for i in embedded_query(db):
        for doc in i:
            print(doc)
            count += 1
        print('Encontrados : {0}'.format(count))
        print('--------------------')
