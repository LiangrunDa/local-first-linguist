from src.translator.translator import Translator


class MT5Ja2ZhTranslator(Translator):
    def __init__(self, max_length):
        super().__init__()
        self.max_length = max_length

    def load(self):
        model_path = f'larryvrh/mt5-translation-ja_zh'
        super().load_model(model_path)

    def translate(self, text):
        return self.model(f'<-ja2zh-> {text}', max_length=self.max_length)[0]['translation_text']
 
