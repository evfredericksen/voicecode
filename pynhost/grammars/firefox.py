from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class FirefoxGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'vimperator'
        self.dict_file = 'firefox.json'
        self.priority = 2
        self.load_all_commands()
        self.load_all_numbered_commands()
