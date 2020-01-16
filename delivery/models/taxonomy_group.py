from delivery.models.taxonomy_term import TaxonomyTerm

class TaxonomyGroup:
    def __init__(self, delivery_taxonomy_response):
        taxonomy = delivery_taxonomy_response
        self.system = taxonomy['system']          
        self.id = self.system['id']
        self.name = self.system['name']
        self.codename = self.system['codename']
        self.terms = self.get_terms(taxonomy['terms'])
        

    def get_terms(self, terms):                       
        typed_terms = []
        for term in terms:
            typed_term = self.cast_to_taxonomy_term(term)
            nested_terms = self.iterate_nested_terms(typed_term.terms)
            typed_term.terms = nested_terms
            typed_terms.append(typed_term)            

        return typed_terms

    def cast_to_taxonomy_term(self, term):
        typed_term = TaxonomyTerm(term)
        
        return typed_term

    def iterate_nested_terms(self, nested_terms):
        typed_nested_list = []
        if nested_terms:
            for term in nested_terms:
                typed_term = self.cast_to_taxonomy_term(term)                              
                if typed_term.terms:
                    typed_term.terms = self.iterate_nested_terms(typed_term.terms)
                typed_nested_list.append(typed_term)

        return typed_nested_list
            



                


