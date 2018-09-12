import pymongo

def find_query(db):
    yield db.collectionContatos.find({})

count = 0
if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.get_database('contatos')
    for i in find_query(db):
        for doc in i:
            print(doc)
            count += 1
        print('Encontrados : {0}'.format(count))
        print('--------------------')
