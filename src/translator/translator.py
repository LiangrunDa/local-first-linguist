from transformers import pipeline, MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        try:
            local_model = MarianMTModel.from_pretrained(pretrained_model_name_or_path=model_path)
            local_tokenizer = MarianTokenizer.from_pretrained(pretrained_model_name_or_path=model_path)
            self.model = pipeline("translation", model=local_model, tokenizer=local_tokenizer)
        except Exception as e:
            print(e)
            raise Exception('Model not found')

    def translate(self, text):
        raise NotImplementedError
