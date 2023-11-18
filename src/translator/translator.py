from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch


class Translator:
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        try:
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            local_model = AutoModelForSeq2SeqLM.from_pretrained(pretrained_model_name_or_path=model_path).to(device)
            local_tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_path)
            self.model = pipeline("translation", model=local_model, tokenizer=local_tokenizer, device=0 if device.type == "cuda" else -1)
        except Exception as e:
            print(e)
            raise Exception('Model not found')

    def translate(self, text):
        raise NotImplementedError
