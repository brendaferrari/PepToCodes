import pandas as pd


class Dictionary:
    """ A class that represents the dictionary functionalities.

    Method:
        Dict(self, one_code=False, three_code=False): Return the full dictionary with all data regards aminoacids on the database.
    """

    def Dict(self, one_code=False, three_code=False):
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
