import sublime
from threading import Thread
import urllib.parse
import urllib.request
import json
import re

class WebSequenceDiagramAPICall(Thread):
    '''
    Wraps an API request to WSD in a thread to prevent
    sublime text from blocking.
    '''

    ENDPOINT = 'http://www.websequencediagrams.com/'

    def __init__(self, wsd_request, timeout = 5):
        '''Initializes the API call before sending the message.''' 

        self.wsd_request = wsd_request
        self.timeout = timeout  
        self.result = None
        self.subscribers = list()

        Thread.__init__(self)

    def subscribe(self, api_call_listener):
        '''Adds a subscriber to the thread.'''

        self.subscribers.append(api_call_listener)

    def _notify(self):
        '''Notifies all subscribers of an event.'''

        for subscriber in self.subscribers:
            subscriber.on_thread_complete(self)

    def run(self):
        '''Executes the thread. Makes the API request.'''
        
        try:
            data = urllib.parse.urlencode(self.wsd_request.__dict__)
            data = data.encode('UTF-8')
            request = urllib.request.Request(self.ENDPOINT, data)
            response = urllib.request.urlopen(request, timeout = self.timeout)
            string = response.read().decode("UTF-8")
            # the api isn't sending valid JSON, so we have to quote the parameters
            string = re.sub(r"(img|page|numPages|errors):", r'"\1":', string)
            self.result = json.loads(string)
        except urllib.error.HTTPError as e:
            error = 'HTTP ERROR: {0}'.format(str(e.code))  
            sublime.error_message(error)  
            self.result = False
        except urllib.error.URLError as e:  
            error = 'URL ERROR: {0}'.format(str(e.reason))
            sublime.error_message(error)  
            self.result = False
        
        #Notify all observers about the end of the call.
        self._notify()