from src.parser.parser import Parser


class TXTParser(Parser):
    def __init__(self, path):
        super().__init__(path)
        self.lines = []
        self.index = 0

    def parse(self, lines):
        self.lines = lines

    def encode(self):
        return '\n'.join(self.lines)

    def __next__(self):
        if self.index < len(self.lines):
            line = self.lines[self.index]
            self.index += 1
            return line
        else:
            raise StopIteration

    def update(self, translated_text):
        self.lines[self.index - 1] = translated_text
