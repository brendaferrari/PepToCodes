#Add the smiles in here
smiles = 'N[C@@]([H])(CCCNC(=N)N)C(=O)N[C@@]([H])([C@]([H])(O)C)C(=O)N[C@@]([H])(CCCCN)C(=O)N[C@@]([H])(CCCNC(=N)N)C(=O)O'

#Here is the dictionary with your smiles and respective code
dictio = {
  "N[C@@]([H])(C)C(=O)": "A",
  "N[C@@]([H])(CC(=O)N)C(=O)": "N",
  "N[C@@]([H])(CC(=O)O)C(=O)": "D",
  "N[C@@]([H])(CS)C(=O": "C",
  "N[C@@]([H])(CCC(=O)N)C(=O)": "Q",
  "NCC(=O)": "G",
  "N[C@@]([H])(CCC(=O)O)C(=O)": "E",
  "N[C@@]([H])(CC1=CN=C-N1)C(=O)": "H",
  "N[C@@]([H])([C@]([H])(CC)C)C(=O)": "I",
  "N[C@@]([H])(CC(C)C)C(=O)": "L",
  "N[C@@]([H])(CCSC)C(=O)": "M",
  "N[C@@]([H])(Cc1ccccc1)C(=O)": "F",
  "N1[C@@]([H])(CCC1)C(=O)": "P",
  "N[C@@]([H])(CO)C(=O)": "S",
  "N[C@@]([H])(CC(=CN2)C1=C2C=CC=C1)C(=O)": "W",
  "N[C@@]([H])(Cc1ccc(O)cc1)C(=O)": "Y",
  "N[C@@]([H])(C(C)C)C(=O)": "V",
  "N[C@@]([H])(CCCCN)C(=O)": "K",
  "N[C@@]([H])(CCCNC(=N)N)C(=O)": "R",
  "N[C@@]([H])([C@]([H])(O)C)C(=O)": "T",
}

#Here is the code
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

#Here is to print the result
# print(aacode)
print(''.join(aacode))