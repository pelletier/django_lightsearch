"""
Classes are containers for sended and received data. They are also here for 
ease of use.
"""

class ResultsSet():
    """Contains the part of a ResultsContainer for a specific model"""
    
    def __init__(self, name, results):
        self.name = name
        self.results = results

    def count(self):
        """
        Count the number of objects which match the given query for a model
        """
        return len(self.results)

class ResultsContainer():
    """Contains the result of the search view for simplicity"""
    
    def __init__(self, results):
        self.sets = []
        for results_pack in results:
            self.sets.append(ResultsSet(results_pack[0], results_pack[1]))
    
    def count(self):
        """
        Count the number of objects which match the given query
        """
        counter = 0
        for pack in self.sets:
            counter += pack.count()
        return counter