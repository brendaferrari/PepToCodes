import pandas as pd

class Dataframe:
    """A class that represents dataframe manipulation
    
    Methods:
        create_dataframe(self, columns): Return a formated dataframe"""

    def __init__(self, data):
        """Initialize the instance of a class.
        
        Arguments:
            data(dict): data used to transform smiles code to peptide code."""
        self._data = data

    @property
    def data(self):
        """Data used to manipulate dataframe."""
        return self._data

    def create_dataframe(self, columns):
        """Return a formated dataframe.
        
        Arguments:
            columns(list): list of strings with column names."""
        result = pd.DataFrame.from_dict(self.data, orient='index', columns=columns)
        return result