import pymongo
from random import randint

#Connect to MongoDB - Note: Change connection string as needed
client = pymongo.MongoClient()
db = client.get_database('contatos')

#Create sample data
nomes = ['Victor','Rodrigo','João','Ricardo','José','Jonathan','Lucas','Guilherme', 'Felipe',
         'Gustavo','Marcelo','Igor','Fred','Ronaldo','Maria','Jéssica','Antonia','Mariana',
         'Isabela','Vanessa','Nathalia','Andreza','Luciana','Fabiana','Karina','Carol','Sara']

locais = ['Belo Horizonte','Bahia','Rio de Janeiro','São Paulo','Minas Gerais',
          'Rio Grande do Sul','Distrito Federal','Recife']

numeros = ['0','1','2','3','4','5','6','7','8','9']

for x in range(1, 1001):
    contatos = {
        'nome' : nomes[randint(0, (len(nomes)-1))],
        'local' : locais[randint(0, (len(locais)-1))],
        'numero' : '9' +
                   numeros[randint(7, (len(numeros)-1))] + '' + numeros[randint(1, (len(numeros)-1))] + '' +
                   numeros[randint(1, (len(numeros)-1))] + '' + numeros[randint(0, (len(numeros)-1))] + '' +
                   numeros[randint(0, (len(numeros)-1))] + '' + numeros[randint(0, (len(numeros)-1))] + '' +
                   numeros[randint(0, (len(numeros)-1))] + '' + numeros[randint(0, (len(numeros)-1))]
    }
    #Insert business object directly into MongoDB via insert_one
    result=db.collectionContatos.insert_one(contatos)
    #Print to the console the ObjectID of the new document
    print('Created {0} of 1000 as {1}'.format(x,result.inserted_id))

#Tell us that you are done
print('finished creating 1000 Contatos collectionContatos')