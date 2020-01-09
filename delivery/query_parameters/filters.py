class AllFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)
        self.filter = '[all]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)

class AnyFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)
        self.filter = '[any]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)


class EqualsFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value
        self.filter = '='
        self.query_string= create_query_string(self.codename, self.filter, self.value)


class GreaterThanFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value
        self.filter = '[gt]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)
        

class GreaterThanOrEqualToFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value
        self.filter = '[gte]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)

    
class InFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)
        self.filter = '[in]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)


class LessThanFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value
        self.filter = '[lt]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)
    
    
class LessThanOrEqualToFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value
        self.filter = '[lte]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)
    
    
class RangeFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)
        self.filter = '[range]='
        self.query_string= create_query_string(self.codename, self.filter, self.value)


def create_query_string(codename, query_filter, value):
    query_string = f'{codename}{query_filter}{value}'
    if 'type' in codename or 'codename' in codename:   
        query_string = query_string_formatter(query_string, codename)
    return query_string 

def query_string_formatter(query_string, codename):      
    query_string = query_string.lower()
    query_string = query_string.replace(' ', '_').replace('-', '_')
    return query_string