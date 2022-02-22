import pandas as pd
import json


class Dictionary:
    """ A class that represents the dictionary functionalities.

    Method:
        Dict(self, one_code=False, three_code=False): Return the full dictionary with all data regards aminoacids on the database.
    """

    def dict_csv(self, one_code=False, three_code=False):
        """Return the full dictionary with all data regards aminoacids on the database.

        Arguments:
            one_code=False: Default is False. If true returns the one letter code of aminoacids
            three_code=False: Default is False. If true returns the three letter code of aminoacids
        """

        if one_code is True:
            dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], 
                        usecols= ['smiles', '1lcode'], index_col=0, header=None, squeeze=True).to_dict()
        
        elif three_code is True:
            dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], 
                        usecols= ['smiles', '3lcode'], index_col=0, header=None, squeeze=True).to_dict()           

        return dictio

    def dict_json(self, three_code=True):
        """Return the full dictionary with all data regards aminoacids on norineDB database.

        Arguments:
            one_code=False: IN DEVELOPMENT 
            three_code=False: Default is False. If true returns the three letter code of aminoacids
        """

        if three_code is True:
            with open("resources/norineDB.json", "r") as r:
                data = json.load(r)

                canonicalSmiles = []
                isomericSmiles = []
                codeCan = []
                codeIso = []
                n = 0

                while n < 544:
                    dataCodeCan = data[n]['code']
                    dataCanonical = data[n]['smiles']

                    codeCan.append(dataCodeCan)
                    canonicalSmiles.append(dataCanonical)

                    if 'isomeric' in data[n]:
                        dataCodeIso = data[n]['code']
                        dataIsomeric = data[n]['isomeric']
                        
                        codeIso.append(dataCodeIso)
                        isomericSmiles.append(dataIsomeric)
                    
                    n += 1
                
                smilesCanonical = dict(zip(canonicalSmiles, codeCan))
                smilesIsomeric = dict(zip(codeIso, isomericSmiles))

                dictio = {**smilesCanonical, **smilesIsomeric}

        
        elif one_code is True:
            
            dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], 
                        usecols= ['smiles', '3lcode'], index_col=0, header=None, squeeze=True).to_dict()           

        return dictio

# dictio = Dictionary()

# c = dictio.dict_json(True)
# print(c)
# print(f'Canonical: {smilesCanonical}')
# print(f'Isomeric: {smilesIsomeric}')

