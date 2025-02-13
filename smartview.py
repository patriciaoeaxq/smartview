import json
import os
import keyboard

class SmartView:
    def __init__(self, config_file='custom_terms.json'):
        self.config_file = config_file
        self.terms = self.load_terms()

    def load_terms(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                return json.load(file)
        return {}

    def save_terms(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.terms, file, indent=4)

    def add_term(self, shortcut, expansion):
        self.terms[shortcut] = expansion
        self.save_terms()

    def remove_term(self, shortcut):
        if shortcut in self.terms:
            del self.terms[shortcut]
            self.save_terms()

    def replace_shortcuts(self):
        for shortcut, expansion in self.terms.items():
            keyboard.add_abbreviation(shortcut, expansion)

    def run(self):
        self.replace_shortcuts()
        print("SmartView is running. Press ESC to stop.")
        keyboard.wait('esc')

if __name__ == "__main__":
    smartview = SmartView()

    # Example usage
    smartview.add_term('brb', 'be right back')
    smartview.add_term('omw', 'on my way')

    smartview.run()