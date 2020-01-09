import sys

class DepthParameter:    
    def __init__(self, value):
        self.value = ensure_integer(type(self).__name__, value)         
        self.parameter = 'depth='
        self.query_string = create_query_string(self.parameter, self.value)


class ElementsParameter:
    def __init__(self, value):
        self.value = value
        self.parameter = 'elements=' 
        self.query_string = create_query_string(self.parameter, self.value)


class LanguageParameter:
    def __init__(self, value):
        self.value = value
        self.parameter = 'language=' 
        self.query_string = create_query_string(self.parameter, self.value)  


class LimitParameter:
    def __init__(self, value):
        self.value = ensure_integer(type(self).__name__, value)
        self.parameter = 'limit='
        self.query_string = create_query_string(self.parameter, self.value)


class OrderParameter:
    def __init__(self, value, order):
        self.value = f'{value}[{order}]'
        self.parameter = 'order='
        self.query_string = create_query_string(self.parameter, self.value)    
    

class SkipParameter:
    def __init__(self, value):
        self.value = ensure_integer(type(self).__name__, value)
        self.parameter = 'skip='
        self.query_string = create_query_string(self.parameter, self.value)


class IncludeTotalCountParameter:
    def __init__(self, value):
        self.value = value
        self.parameter = 'includeTotalCount='
        self.query_string = create_query_string(self.parameter, self.value)


def create_query_string(parameter, value):
    query_string = f'{parameter}{value}'
    return query_string 

def ensure_integer(parameter_name,value):
    if isinstance(value, int):
        return value         
    else:
        print(f'{parameter_name} must be an integer.')
        sys.exit(1)