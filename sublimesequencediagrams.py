import sublime, sublime_plugin
from wsdapicall import WebSequenceDiagramAPICall
from wsdrequest import WebSequenceDiagramRequest
from wsdapilistener import ApiCallListener

class WebSequenceDiagramsCommand(sublime_plugin.TextCommand):
    '''
    Generates a Web Sequence Diagram using the source code
    in the editor.
    '''

    DEFAULT_FORMAT = 'png'
    DEFAULT_DIAGRAM_STYLE = 'napkin'
    API_VERSION = 1

    def _get_diagram_source(self):
        '''Gets the source code of the diagram.'''

        return self.view.substr(sublime.Region(0, self.view.size()))

    def run(self, edit):
        '''Executes the command'''

        diagram_source = self._get_diagram_source()

        #Create the listener.
        api_call_listener = ApiCallListener()

        #Create the request.
        wsd_request = WebSequenceDiagramRequest(self.DEFAULT_DIAGRAM_STYLE, diagram_source, self.DEFAULT_FORMAT, self.API_VERSION)

        #Make the API call.
        api_call = WebSequenceDiagramAPICall(wsd_request)
        api_call.subscribe(api_call_listener)
        api_call.start()