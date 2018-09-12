import pymongo

def find_query_spec(db):
    yield db.collectionContatos.find({'local':'Bahia'})
    #({'local': {'$in' : ['Bahia','São Paulo']}})
    #({'local': {'$type': 10}})
    #({'local': {'$exists': 'false'}})

count = 0
if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.get_database('contatos')
    for i in find_query_spec(db):
        for doc in i:
            print(doc)
            count += 1
        print ('Encontrados : {0}'.format(count))
        print('--------------------')
