class TaxonomyTerm:
    def __init__(self, term):  
        self.name = term['name']
        self.codename = term['codename']
        self.terms = self.get_nested_terms(term)

    def get_nested_terms(self, term):
        if term.get('terms'):
            return term['terms']
        else:         
            return list()