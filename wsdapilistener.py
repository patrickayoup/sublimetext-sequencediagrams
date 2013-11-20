import sublime
import datetime
import urllib2
import webbrowser

class ApiCallListener(object):
	'''Listens for the completion of an API call.'''

	BASE_URL = 'http://www.websequencediagrams.com/{0}'

	def _parse_errors(self, error_list):
		'''Parses errors into a readable list.'''

		return '\n'.join(error_list)

	def _write_errors(self, errors):
		'''Opens a new window and displays the errors.'''

		#Create a new window and set the title with a timestamp.
		active_window = sublime.active_window()
		error_view = active_window.new_file()
		timestamp = str(datetime.datetime.now()).split('.')[0]
		error_view.set_name("wsdErrors-{0}.txt".format(timestamp))

		#Write the error list to the new window.
		edit = error_view.begin_edit()
		error_view.insert(edit, 0, errors)
		error_view.end_edit(edit)

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
				errors = self._parse_errors(wsd_api_call.result['errors'])
				sublime.error_message('Diagram Generation Failed: There are errors in your source code.')
				sublime.set_timeout(lambda: self._write_errors(errors), 100)
