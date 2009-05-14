class ResultsSet():
    """Contains the part of a ResultsContainer for a specific model"""
    
    def __init__(self, name, results):
        self.name = name
        self.results = results

    def count(self):
        counter = 0
        for result in self.results:
            counter += 1
        return counter

class ResultsContainer():
    """Contains the result of the search view for simplicity"""
    
    def __init__(self, results):
        self.sets = []
        for results_pack in results:
            self.sets.append(ResultsSet(results_pack[0], results_pack[1]))
    
    def count(self):
        counter = 0
        for pack in self.sets:
            for result in pack.results:
                counter += 1
        return counter