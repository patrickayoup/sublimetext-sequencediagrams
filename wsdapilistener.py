import sublime
import datetime
import webbrowser

class ApiCallListener(object):
	'''Listens for the completion of an API call.'''

	BASE_URL = 'http://www.websequencediagrams.com/{0}'

	def _write_errors(self, errors):
		'''Opens a new window and displays the errors.'''

		#timestamp = str(datetime.datetime.now()).split('.')[0]

		active_window = sublime.active_window()
		l = list(errors)
		l.insert(0, 'Errors occurred during save:')
		active_window.show_quick_panel(l, self.on_select_error);

	def _show_diagram(self, diagram_url):
		'''Opens the generated diagram in the default web browser.'''

		webbrowser.open_new_tab(diagram_url)

	def on_thread_complete(self, wsd_api_call):
		'''Called when the api call completes.'''

		#If the result is NONE, then there was an HTTP error.
		#If the errors list is not empty, then there was a service error.
		if wsd_api_call.result:
			if not wsd_api_call.result['errors']:
				#Display the generated diagram in the web browser.
				self._show_diagram(self.BASE_URL.format(wsd_api_call.result['img']))
			else:
				#Show an error message and display errors in a new window.
				errors = wsd_api_call.result['errors']
				#sublime.error_message('Diagram Generation Failed: There are errors in your source code.')
				sublime.set_timeout(lambda: self._write_errors(errors), 100)

	def on_select_error(self, index):
		return;
