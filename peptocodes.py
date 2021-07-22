# TODO: #5 To be able to select more than one peptide
smiles = input("Type your peptide smiles: ")
#N[C@@]([H])(CCCNC(=N)N)C(=O)N[C@@]([H])([C@]([H])(O)C)C(=O)N[C@@]([H])(CCCCN)C(=O)N[C@@]([H])(CCCNC(=N)N)C(=O)O

import csv
import pandas as pd

# TODO: #2 Expand the aminoacid types 
# Here is the dictionary with your smiles and respective code
dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], usecols= ['smiles', '1lcode'], index_col=0, header=None, squeeze=True).to_dict()

#print(dictio)

# Here is the code
## empty code list
aacode = []
i = 0

## loop to count characters and change to code
while i < len(smiles):
  keys = list(dictio.keys())

  for j in range(len(keys)):
    key = keys[j]

    sub = smiles[i:i+len(key)]
    if sub in dictio:
      i = i + len(key)
      aacode.append(dictio[sub])
      break

    if j == len(dictio.keys())-1:
      i = i+1

# TODO: #3 Add error message
# Here is to print the result
# TODO: #4 Show a string in response to no match
#print(aacode)
print("Your code is:", ''.join(aacode))