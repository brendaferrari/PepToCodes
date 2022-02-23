# PepToCodes (1.0.0) - Peptides to Codes

Script developed to transform the amino acid smiles to one letter code or three letter code for later analysis.

<img src="resources/images/Peptocodes.png" width="570">

*Illustrative image*

## Requirements

* [pandas](https://pandas.pydata.org/) - a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. 

* [art](https://github.com/sepandhaghighi/art) - ART is a Python lib for text converting to ASCII art fancy. ;-)

Libraries were used in a [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) environment using python 3.6.13

## Instalation

Miniconda3: [Installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

pandas:
```
conda install -c anaconda pandas
```

art:
```
conda install -c sepandhaghighi art
```
## How to use

* Download the code and unzip it on the desirable directory

* It is possible to use two databases to analyze aminoacids. One is the native database which only recognizes [20 aminoacids](resources/codes.csv) (canonical and isomeric). The other is the [Norine Database](https://bioinfo.lifl.fr/norine/) with 544 aminoacids. 

    * To use the native database use the following command:
        ```
        python main.py peptocodes True False
        ```

        To obtain one letter code. And,

        ```
        python main.py peptocodes False True
        ```       

        To obtain three letter code.

    * To use the [Norine Database](https://bioinfo.lifl.fr/norine/) use the following command:

        ```
        python main.py norine
        ```       

        *For now, this database is only available for three letter code analysis.*

* Regarding the analysis for string or file:

    * For one aminoacid analysis:

        * Type your peptide smiles as an input

        i.e. N[C@@]([H])(CCCNC(=N)N)C(=O)N[C@@]([H])([C@]([H])(O)C)C(=O)N[C@@]([H])(CCCCN)C(=O)N[C@@]([H])(CCCNC(=N)N)C(=O)O

        * The answer will pop-up at your terminal screen

        i.e. RTKR

            * This example onyl works with the native database.

    * For more than one aminoacid analysis:

        * Use the file [smiles.txt](resources/smiles.txt) as example on how to format input data


* Asteriscs in your code answer means the software could not recognize the input. Please, keep in mind that the native database only recognizes [20 aminoacids](resources/codes.csv) (canonical and isomeric). If you need a bigger database please use norine option.

## Observations

According to its website, Norine database is freely available to everybody, under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)). No changes were made on its structure or data.

## Authorship

* Author: **Brenda Ferrari** ([brendaferrari](https://github.com/brendaferrari))

Social preview original photo by **Brenda Ferrari** ([brendaferrari](https://github.com/brendaferrari))