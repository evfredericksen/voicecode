from pynhost import grammarbase, api
from pynhost.grammars.atom.atombase import AtomBaseGrammar

class AtomCommandsGrammar(AtomBaseGrammar):
    def __init__(self):
        super().__init__()
        self.dict_file = 'atomcmds.json'
        self.mapping = {
            'line <num> <1->': self.go_to_line,
            'halt': self.space(',', start=False)
        }
        self.load_command('join lines')
        self.load_command('toggle comment'),
        self.load_command('clear select'),
        self.load_command('fuzzy'),
        self.load_command('drop'),
        self.load_command('climb'),
        self.load_command('save file'),
        self.load_numbered_command('undo'),
        self.load_numbered_command('snipe') # backspace
        self.load_numbered_command('indent') # backspace
        self.load_numbered_command('outdent') # backspace


    def go_to_line(self, words):
        num = self._num(words)
        self.do_command('l' + str(num))

    def letter(self, words):
        api.send_string(words[0][0])

    def char(self, words):
        api.send_string(self._other_chars[words[0]])