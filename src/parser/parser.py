import os


class Parser:
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
            self.parse(lines)

    def save(self):
        root, extension = os.path.splitext(self.path)
        new_file_path = f"{root}_translated{extension}"
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(self.encode())

    def __iter__(self):
        return self

    def encode(self):
        raise NotImplementedError

    def parse(self, lines):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError

    def translate(self, translated_text):
        raise NotImplementedError
