import sublime
from sublime_plugin import TextCommand
from .wsdapicall import WebSequenceDiagramAPICall
from .wsdrequest import WebSequenceDiagramRequest
from .wsdapilistener import ApiCallListener

class WebSequenceDiagramsCommand(TextCommand):
    '''
    Generates a Web Sequence Diagram using the source code
    in the editor.
    '''

    #http://www.websequencediagrams.com/users/getapikey
    settings = {};

    def _get_diagram_source(self):
        '''Gets the source code of the diagram.'''

        self.settings = sublime.load_settings('sublimesequencediagrams.sublime-settings')        
        
        return self.view.substr(sublime.Region(0, self.view.size()))

    def run(self, edit):
        '''Executes the command'''

        diagram_source = self._get_diagram_source()

        #Create the listener.
        api_call_listener = ApiCallListener()

        #Create the request.
        wsd_request = WebSequenceDiagramRequest(diagram_source, self.settings)

        #Subscribe to the thread and make the API call.
        api_call = WebSequenceDiagramAPICall(wsd_request)
        api_call.subscribe(api_call_listener)
        api_call.start()