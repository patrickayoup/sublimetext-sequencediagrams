from threading import Thread
import urllib  
import urllib2

class WebSequenceDiagramAPICall(Thread):
    '''
    Wraps an API request to WSD in a thread to prevent
    sublime text from blocking.
    '''

    def __init__(self, style, message, format, api_version, timeout):
        '''Initializes the API call before sending the message.''' 

        self.style = style 
        self.message = message 
        self.format = format
        self.api_version = api_version 
        self.timeout = timeout  
        self.result = None

        super.__init__(self)

    def run(self):
        '''Executes the thread. Makes the API request.'''
        
        try:  
            data = urllib.urlencode({'css': self.original})  
            request = urllib2.Request('http://prefixr.com/api/index.php', data,  
                headers={"User-Agent": "Sublime Prefixr"})  
            http_file = urllib2.urlopen(request, timeout=self.timeout)  
            self.result = http_file.read()  
            return  

        except (urllib2.HTTPError) as (e):  
            err = '%s: HTTP error %s contacting API' % (__name__, str(e.code))  
        except (urllib2.URLError) as (e):  
            err = '%s: URL error %s contacting API' % (__name__, str(e.reason))  

        sublime.error_message(err)  
        self.result = False