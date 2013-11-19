import sublime, sublime_plugin
from wsdapicall import WebSequenceDiagramAPICall
from wsdrequest import WebSequenceDiagramRequest

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

        #Create the request.
        wsd_request = WebSequenceDiagramRequest(self.DEFAULT_FORMAT, diagram_source, self.DEFAULT_FORMAT, self.API_VERSION)