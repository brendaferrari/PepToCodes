from functionalities.peptocode import PeptoCode

import pandas as pd


print('Do you wish to transform one aminoacid of a file? Type a to one aminoacid or b for a file.')
answer = input()
if answer.lower() == "a":
    print()
    smiles = input('Type your peptide smiles: ')

    dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], usecols= ['smiles', '1lcode'], index_col=0, header=None, squeeze=True).to_dict()

    peptocode = PeptoCode(smiles, dictio)
    aacode = peptocode.count_and_change()

    print(f"Your code is: {aacode}")

elif answer.lower() == "b":
    smiles = input('Type your file name with path: ')

    #do a dictionary instead of list
    #https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file
    dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], usecols= ['smiles', '1lcode'], index_col=0, header=None, squeeze=True).to_dict()
    
    df = pd.read_csv('smiles.txt')
    code = {}
    count = 0
    for row in df.itertuples():
        print(row)
        print()
        peptocode = PeptoCode(row[1], dictio)
        aacode = peptocode.count_and_change()
        print(aacode)
        print()
        code[row[1]] = []
        code[row[1]].append(aacode)
        print(code)
        count += 1
        print(count)
        

        # df = pd.DataFrame.from_dict(code, orient='index')
        # print(df)

# with open('smiles_output.txt','w') as data:
#     data.write(str(code))
# data.close()

# import json


# with open('file.txt', 'w') as file:
#     for element in code:
#         file.write(json.dumps(element))

# with open("smiles_output.txt", "w") as textfile:
#     for element in code:
#         textfile.write(element)
#     textfile.close()
