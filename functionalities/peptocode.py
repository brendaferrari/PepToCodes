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
        notaaCode = []
        i = 0
        
        while i < len(self.smiles):
            keys = list(self.peptide_data.keys())

            for j in range(len(keys)):
                key = keys[j]
                
                sub = self.smiles[i:i+len(key)]
                if sub in self.peptide_data:
                    i = i + len(key)
                    aacode.append(self.peptide_data[sub])
                    break

                if j == len(self.peptide_data.keys())-1:
                    notaaCode.append(sub)
                    i = i + 1
                    i = i + len(key)
                    aacode.append('*')

        code = ''.join(aacode)

        return code, notaaCode