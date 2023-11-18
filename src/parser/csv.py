from src.parser.parser import Parser


class CSVParser(Parser):
    def __init__(self, path):
        super().__init__(path)
        self.lines = []
        self.index = 0
        self.elementIdx = 0

    def parse(self, lines):
        for line in lines:
            elements = line.split(',')
            elements = [element.strip() for element in elements]
            self.lines.append(elements)

    def encode(self):
        encoded = ''
        for line in self.lines:
            encoded += ','.join(line) + '\n'
        return encoded

    def __next__(self):
        if self.index < len(self.lines):
            line = self.lines[self.index]
            if self.elementIdx < len(line):
                element = line[self.elementIdx]
                self.elementIdx += 1
                return element
            else:
                self.elementIdx = 0
                self.index += 1
                element = self.__next__()
                return element
        else:
            raise StopIteration

    def update(self, translated_text):
        self.lines[self.index][self.elementIdx - 1] = translated_text

    def __len__(self):
        cnt = 0
        for i in range(self.lines):
            cnt += len(self.lines[i])
        return cnt
