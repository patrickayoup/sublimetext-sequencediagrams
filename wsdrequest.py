import sublime

class WebSequenceDiagramRequest(object):
    '''
    Represents a request for a diagram to be passed
    in an API call.
    '''

    def __init__(self, message, settings):
        '''Initializes the API request.'''

        #Camel case is important here for their api.
        self.apiVersion = settings.get('api_version')
        self.style = settings.get('style') 
        self.format = settings.get('format')
        self.apikey = settings.get('apikey')
        self.message = message 

    def __str__(self):
        '''Returns a string representation of the request.'''

        return 'WebSequenceDiagramRequest\n\tstyle: {0}\n\tmessage: {1}\n\tformat: {2}\n\tapi_version: {3}\n'.format(self.style, self.message, self.format, self.api_version)