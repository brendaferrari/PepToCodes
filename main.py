from functionalities.peptocode import PeptoCode
from functionalities.dataframe import Dataframe
from functionalities.dictionary import Dictionary

import pandas as pd
from art import *
import sys

if len(sys.argv) <= 1:
    print("One or more parameter missing. Please add input file name at the following manner: 'python main.py peptocodes True/False True/False' or 'python main.py norine'")
    sys.exit()

database = sys.argv[1].lower()

if database == 'peptocodes'.lower():

    if len(sys.argv) <= 3:
        print("One or more parameter missing. Please add input file name at the following manner: 'python main.py peptocodes True/False True/False'")
        sys.exit()

    one_code = sys.argv[2].lower() == 'true'
    three_code= sys.argv[3].lower() == 'true'

tprint('PepToCodes', font='3d_diagonal')

if database == 'norine'.lower():
    print('You are using Norine database which is freely available to everybody.\n')
    print('\033[1m' + 'Norine: update of the nonribosomal peptide resource. Areski Flissi, Emma Ricart, Clémentine Campart, Mickaël Chevalier, Yoann Dufresne, Juraj Michalik, Philippe Jacques, Christophe Flahaut, Frédéric Lisacek, Valérie Leclère and Maude Pupin. Nucleic Acids Research, Nov. 2019, gkz1000, https://doi.org/10.1093/nar/gkz1000')
    print('\033[0m')

print('\nDo you wish to transform one aminoacid of a file? Type a to one aminoacid or f for a file.')
answer = input()

if answer.lower() == "a":
    print()
    smiles = input('Type your peptide smiles: ')

    dictio = Dictionary()

    if database == 'peptocodes'.lower():
        peptocode = PeptoCode(smiles, dictio.dict_csv(one_code, three_code))
    elif database == 'norine'.lower():
        peptocode = PeptoCode(smiles, dictio.dict_json())
    aacode, notaaCode = peptocode.count_and_change()

    if aacode != "*":
        print(f"Your code is: {aacode}")
        if notaaCode:
            print(f"Some codes were not recognized: {notaaCode}")
        else:
            print(f"All codes were analyzed and recognized.")
    else:
        print("Unfortunately your code could not be recognized. Please, verify your code or contact the developers.")

# BUG ON PATTERN RECONGITION FOR FILE
elif answer.lower() == "f":
    smiles = input('Type your file name with path: ')

    dictio = Dictionary()
    
    df = pd.read_csv(smiles)
    aacode = []
    notaaCode = []
    aasmiles = []
    countlen = []
    count = 0
    for row in df.itertuples():
        aasmiles.append(row[1])

        if database == 'peptocodes'.lower():
            peptocode = PeptoCode(row[1], dictio.dict_csv(one_code, three_code))
        elif database == 'norine'.lower():
            peptocode = PeptoCode(row[1], dictio.dict_json())
        code, notCode = peptocode.count_and_change()
        aacode.append(code)
        notaaCode.append(notCode)

        count += 1
        countlen.append(count)

    variables = zip(aasmiles, aacode, notaaCode)
    variablesDataframe = dict(zip(countlen, variables))

    dataframe = Dataframe(variablesDataframe)
    data = dataframe.create_dataframe(columns=('smiles', 'code', 'not recognized'))
    data.to_csv('smiles_output.txt')

    if aacode != "*":
        print("smiles_output.txt was saved successfully.")
        if notaaCode:
            print(f"Some codes were not recognized: {notaaCode}")
        else:
            print(f"All codes were analyzed and recognized.")
    else:
        print("Unfortunately your code could not be recognized. Please, verify your code or contact the developers.")
