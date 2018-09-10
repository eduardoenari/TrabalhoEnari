import pymongo


def and_or_query(db):
    yield db.my_collection.find({
        'status': 'A',
        'qty': {'$lt': 30}
    })

    yield db.my_collection.find({
        '$or': [
            {'status': 'A'},
            {'qty': {'$lt': 30}}
        ]
    })

    yield db.my_collection.find({
        'status': 'A',
        '$or': [
            {"qty": {"$lt": 30}},
            {"item": {"$regex": "^p"}}
        ]
    })


if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.get_database('agendaDB')

    for q in and_or_query(db):
        for doc in q:
            print(doc)
        print('--------------------')