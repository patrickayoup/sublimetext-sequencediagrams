class WebSequenceDiagramRequest(object):
    '''
    Represents a request for a diagram to be passed
    in an API call.
    '''

    def __init__(self, style, message, format, api_version):
        '''Initializes the API request.'''
        
        self.style = style 
        self.message = message 
        self.format = format
        #Camel case is important here for their api.
        self.apiVersion = api_version

    def __str__(self):
        '''Returns a string representation of the request.'''

        return 'WebSequenceDiagramRequest\n\tstyle: {0}\n\tmessage: {1}\n\tformat: {2}\n\tapi_version: {3}\n'.format(self.style, self.message, self.format, self.api_version)