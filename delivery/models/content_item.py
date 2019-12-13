from delivery.models.asset import Asset
from delivery.models.multiple_choice_option import MultipleChoiceOption
from delivery.models.taxonomy_term import TaxonomyTerm
import json
import sys

class ContentItem:
    def __init__(self, delivery_item_response, modular_content=None):
        content_item = delivery_item_response
        self.system = content_item['system']
        
        self.id = self.system['id']
        self.name = self.system['name']
        self.codename = self.system['codename']        
        self.language = self.system['language']
        self.type = self.system['type']       
        self.elements = content_item['elements']
        self.modular_content = modular_content
      

    def get_element(self, codename):
        try:
            if codename:
                return self.elements[codename]
        except Exception:
            print('Element with codename: {} does not exist.'.format(codename))
            sys.exit(1)

    def get_element_value(self, element_value_codename):
        try:
            if element_value_codename:
                return self.elements[element_value_codename]['value']
        except Exception:
            print('Element does not have a value with codename: {} .'.format(element_value_codename))
            sys.exit(1)
            

    def get_assets(self, element_codename):                        
        try:
            if element_codename:
                assets = []
                asset_element = self.get_element(element_codename)                
                for asset in asset_element['value']:
                    strongly_typed_asset = Asset(asset)                    
                    assets.append(strongly_typed_asset)                    
                return assets                
        except Exception:
             print('Asset with codename: {} does not exist.'.format(element_codename))
             sys.exit(1)

    def get_asset(self, element_codename, asset_name):                        
        try:
            if element_codename:
                asset_element = self.get_element(element_codename)
                assets = self.get_assets(element_codename)                  
                for asset in assets:                      
                    if asset_name in asset.name:                         
                        return asset
                    else:
                        return 'Asset with name: {} does not exist in the {} element'.format(asset_name, element_codename)
        except Exception:
             print('Asset with codename: {} does not exist.'.format(element_codename))
             sys.exit(1)

    def get_options(self, element_codename):
        element = self.get_element_value(element_codename)
        multiple_choice_options = []

        try:
            for option in element:
                strongly_typed_option = MultipleChoiceOption(option)
                multiple_choice_options.append(strongly_typed_option)
            return multiple_choice_options
        except Exception:
            print('No options selected for {} element.'.format(element_codename))
            sys.exit(1)  

    def get_taxonomy_terms(self, element_codename):
        element = self.get_element_value(element_codename)
        taxonomy_terms = []

        try:
            for term in element:
                strongly_typed_term = TaxonomyTerm(term)
                taxonomy_terms.append(strongly_typed_term)
            return taxonomy_terms
        except Exception:
            print('No taxonomy terms for {} element.'.format(element_codename))
            sys.exit(1)
        
    def get_linked_items(self, element_codename):
        element = self.get_element_value(element_codename)     
        linked_items = []    

        try:    
            for linked_item_codename in element:
                linked_item = ContentItem(self.modular_content[linked_item_codename])
                linked_items.append(linked_item)
            return linked_items
        except Exception:
            print('Linked Element with codename: {} does not exist.'.format(element_codename))
            sys.exit(1)
        




