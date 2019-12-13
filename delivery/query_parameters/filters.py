class AllFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)

    def create_query_string(self):
        query_string = '{0}[all]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string


class AnyFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)

    def create_query_string(self):
        query_string = '{0}[any]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string


class EqualsFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value

    def create_query_string(self):
        query_string = '{0}={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string

class GreaterThanFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value

    def create_query_string(self):
        query_string = '{0}[gt]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string

class GreaterThanOrEqualToFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value

    def create_query_string(self):
        query_string = '{0}[gte]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string

    
class InFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)

    def create_query_string(self):
        query_string = '{0}[in]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string


class LessThanFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value

    def create_query_string(self):
        query_string = '{0}[lt]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string
    
    
class LessThanOrEqualToFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = value

    def create_query_string(self):
        query_string = '{0}[lte]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string
    
    
class RangeFilter:
    def __init__(self, codename, value):
        self.codename = codename
        self.value = ','.join(value)

    def create_query_string(self):
        query_string = '{0}[range]={1}'.format(self.codename, self.value)
        cleaned_query_string = query_string_formatter(query_string, self.codename)
        return cleaned_query_string


def query_string_formatter(query_string, codename):
    if 'type' in codename or 'codename' in codename:        
        query_string = query_string.lower()
        query_string = query_string.replace(' ', '_').replace('-', '_')
    return query_string