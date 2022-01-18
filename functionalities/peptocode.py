class PeptoCode:
    """A class that represents peptide to code functionalities.
    
    Arguments:
        smiles(str): smiles strings to convert to peptide code.
        peptide_data(dict): data used to transform smiles code to peptide code.
        
    Methods:
        count_and_change(self): Return a string with the aminoacid code."""

    def __init__(self, smiles, peptide_data):
        """Initialize the instance of a class.
        
        Arguments:
            smiles(str): smiles strings to convert to peptide code.
            peptide_data(dict): data used to transform smiles code to peptide code."""
        self.smiles = smiles
        self._peptide_data = peptide_data

    @property
    def peptide_data(self):
        """Data used to transform smiles code to peptide code."""
        return self._peptide_data
        
    def count_and_change(self):
        """Return a string with the aminoacid code."""

        aacode = []
        i = 0
        
        while i < len(self.smiles):
            keys = list(self.peptide_data.keys())
            # To add a * in not found, find a way to get j not in the range of the dictionary,  
            # using for or other statements
            for j in range(len(keys)):
                key = keys[j]

                sub = self.smiles[i:i+len(key)]
                if sub in self.peptide_data:
                    i = i + len(key)
                    aacode.append(self.peptide_data[sub])

                if j == len(self.peptide_data.keys())-1:
                    i = i+1

                code = ''.join(aacode)
        
        return code