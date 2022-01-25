from functionalities.peptocode import PeptoCode
from functionalities.dataframe import Dataframe
from functionalities.dictionary import Dictionary

import pandas as pd
import sys

if len(sys.argv) <= 1:
    print("One parameter is missing. Please add input file name at following manner: 'python main.py one_code=True/three_code=True'")
    sys.exit()

one_code = sys.argv[1].lower() == 'true'
three_code = sys.argv[2].lower() == 'true'

print('Do you wish to transform one aminoacid of a file? Type a to one aminoacid or b for a file.')
answer = input()
if answer.lower() == "a":
    print()
    smiles = input('Type your peptide smiles: ')

    dictio = Dictionary()

    peptocode = PeptoCode(smiles, dictio.Dict(one_code, three_code))
    aacode, notaaCode = peptocode.count_and_change()

    if aacode != "*":
        print(f"Your code is: {aacode}")
        if notaaCode:
            print(f"Some codes were not recognized: {notaaCode}")
        else:
            print(f"All codes were analyzed and recognized.")
    else:
        print("Unfortunately your code could not be recognized. Please, verify your code or contact the developers.")

elif answer.lower() == "b":
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

        peptocode = PeptoCode(row[1], dictio.Dict(one_code, three_code))
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
