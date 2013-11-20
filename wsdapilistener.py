import sublime
import datetime
import urllib2
import webbrowser

class ApiCallListener(object):
	'''Listens for the completion of an API call.'''

	BASE_URL = 'http://www.websequencediagrams.com/{0}'

	def _parse_errors(self, error_list):
		'''Parses errors into a nice readable list.'''

		return '\n'.join(error_list)

	def _write_errors(self, errors):
		'''Opens a new window and displays the errors.'''

		active_window = sublime.active_window()
		error_view = active_window.new_file()
		timestamp = str(datetime.datetime.now()).split('.')[0]
		error_view.set_name("wsdErrors-{0}.txt".format(timestamp))

		edit = error_view.begin_edit()
		error_view.insert(edit, 0, errors)
		error_view.end_edit(edit)

	def _show_diagram(self, diagram_url):
		'''Downloads the generated diagram from the server.'''

		webbrowser.open_new_tab(diagram_url)

	def on_thread_complete(self, wsd_api_call):
		'''Called when the api call completes.'''

		#If the result is NONE, then there was a REST error.
		#If the errors list is not empty, then there was a service error.
		if wsd_api_call.result:
			if not wsd_api_call.result['errors']:
				self._show_diagram(self.BASE_URL.format(wsd_api_call.result['img']))
			else:
				errors = self._parse_errors(wsd_api_call.result['errors'])
				sublime.error_message('Diagram Generation Failed: There are errors in your source code.')
				sublime.set_timeout(lambda: self._write_errors(errors), 100)
