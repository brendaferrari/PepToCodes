# PepToMon - Peptides to Monomers

Script developed to transform the amino acid smiles to one letter code for latter analysis

This script was written with Python 

## How to use

* Download the code and unzip it on the desirable directory

To run use the following command:
```
python peptomon.py
```

* Type your peptide smiles as an input

i.e. N[C@@]([H])(CCCNC(=N)N)C(=O)N[C@@]([H])([C@]([H])(O)C)C(=O)N[C@@]([H])(CCCCN)C(=O)N[C@@]([H])(CCCNC(=N)N)C(=O)O

* The answer will pop-up at your terminal screen

i.e. RTKR

## Observations

* In this version you may also obtain the 3 letter code for your smiles, just change line 10 to:
```
dictio = pd.read_csv("resources/codes.csv", sep=' ', names=['name', 'smiles', '3lcode', '1lcode'], usecols= ['smiles', '3lcode'], index_col=0, header=None, squeeze=True).to_dict()
```

* **In this version is only possible to tranform ONE smiles at a time**

## Authorship

* Author: **Brenda Ferrari** ([brendaferrari](https://github.com/brendaferrari))