from src.translator.translator import Translator


class HelsinkiTranslator(Translator):
    def __init__(self):
        super().__init__()

    def load(self, src, tgt):
        model_path = f'Helsinki-NLP/opus-mt-{src}-{tgt}'
        super().load_model(model_path)

    def translate(self, text):
        return self.model(text)[0]['translation_text']