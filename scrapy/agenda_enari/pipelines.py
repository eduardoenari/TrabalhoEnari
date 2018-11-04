# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

import logging



class AgendaEnariPipeline(object):
    collection_name = 'empresas'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        #self.db[self.collection_name].insert_one(dict(item))
        print("---------------------------------------------------------------------------")
        #print(item['nome'])
        
        a = self.db[self.collection_name].find_one({ "$or": [{"nome": item['nome']}, {"endereco": item['endereco']}, {"telefone": item['telefone']} ]})
        if(a is None):
            self.db[self.collection_name].insert_one(dict(item))
        else:
            self.db[self.collection_name].update_one(
                {
                    "nome": a['nome'],
                    "endereco": a['endereco'],
                    "telefone": a['telefone']
                }, 
                {
               "$set":{
                    "nome": item['nome'],
                    "endereco": item['endereco'],
                    "telefone": item['telefone']
               }
            })
        print(a)
        print("-----------------------------------------------------------------------------")

        return item
