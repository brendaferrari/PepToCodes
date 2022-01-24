from functionalities.peptocode import PeptoCode
from functionalities.dataframe import Dataframe

import pandas as pd


print('Do you wish to transform one aminoacid of a file? Type a to one aminoacid or b for a file.')
answer = input()
if answer.lower() == "a":
    print()
    smiles = input('Type your peptide smiles: ')

    dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], usecols= ['smiles', '1lcode'], index_col=0, header=None, squeeze=True).to_dict()

    peptocode = PeptoCode(smiles, dictio)
    aacode, notaaCode = peptocode.count_and_change()

    print(f"Your code is: {aacode}")

    if notaaCode:
        print(f"Some codes were not recognized: {notaaCode}")
    else:
        print(f"All codes were analyzed and recognized.")

elif answer.lower() == "b":
    smiles = input('Type your file name with path: ')
    dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], usecols= ['smiles', '1lcode'], index_col=0, header=None, squeeze=True).to_dict()
    
    df = pd.read_csv(smiles)
    aacode = []
    notaaCode = []
    aasmiles = []
    countlen = []
    count = 0
    for row in df.itertuples():
        aasmiles.append(row[1])

        peptocode = PeptoCode(row[1], dictio)
        code, notCode = peptocode.count_and_change()
        aacode.append(code)
        notaaCode.append(notCode)

        count += 1
        countlen.append(count)

    variables = zip(aasmiles, aacode, notaaCode)
    variablesDataframe = dict(zip(countlen, variables))
    print(variablesDataframe)

    dataframe = Dataframe(variablesDataframe)
    data = dataframe.create_dataframe(columns=('smiles', 'code', 'not recognized'))
    data.to_csv('smiles_output.txt')
