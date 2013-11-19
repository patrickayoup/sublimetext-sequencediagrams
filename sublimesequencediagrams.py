import sublime, sublime_plugin

DIAGRAM_STYLE = 'napkin'

class WebSequenceDiagramsCommand(sublime_plugin.TextCommand):
	'''
	Generates a Web Sequence Diagram using the source code
	in the editor.
	'''

	def _get_diagram_source():
		'''Gets the source code of the diagram.'''
		return self.view.substr(sublime.Region(0, self.view.size()))

	def run(self, edit):
		'''Executes the command'''
		
		