from src.parser.parser import Parser


class SRTParser(Parser):
    def __init__(self, path):
        super().__init__(path)
        self.subtitles = []
        self.index = 0

    def parse(self, lines):
        index = 0
        while index < len(lines):
            if lines[index].strip().isdigit():
                index += 1
                timecode = lines[index].strip()
                start, end = timecode.split(' --> ')
                index += 1
                text = ''
                while index < len(lines) and lines[index].strip() != '':
                    text += lines[index].strip() + ' '
                    index += 1
                self.subtitles.append({'start': start, 'end': end, 'text': text})
            else:
                index += 1

    def encode(self):
        encoded = ''
        index = 1
        for subtitle in self.subtitles:
            encoded += str(index) + '\n'
            encoded += subtitle['start'] + ' --> ' + subtitle['end'] + '\n'
            encoded += subtitle['text'] + '\n\n'
            index += 1
        return encoded

    def __next__(self):
        if self.index < len(self.subtitles):
            subtitle = self.subtitles[self.index]
            self.index += 1
            return subtitle['text']
        else:
            raise StopIteration

    def update(self, translated_text):
        self.subtitles[self.index - 1]['text'] = translated_text

    def __len__(self):
        return len(self.subtitles)
