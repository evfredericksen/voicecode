from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CommandPromptGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'command'
        self.mapping = {
            'django restart server': self.restart_server,
            'django run server': 'python manage.py runserver{enter}',
            "launch atom": "atom .{enter}",
        }

    def restart_server(self, words):
        # api.open_window('Command Prompt')
        api.send_string('{ctrl+c}')
        time.sleep(.2)
        api.send_string('python manage.py runserver{enter}')
