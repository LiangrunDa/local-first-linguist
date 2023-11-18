from src.translator.Helsinki import HelsinkiTranslator
from src.translator.mt5ja2zh import MT5Ja2ZhTranslator
from src.parser.srt import SRTParser
from src.parser.txt import TXTParser
from src.parser.csv import CSVParser
import os
import argparse
from tqdm import tqdm


def cli():
    parser = argparse.ArgumentParser(description='Translator for SRT files')
    parser.add_argument("-f", "--file", help="file to translate", required=True)
    parser.add_argument('-s', '--source', help='source language', required=True)
    parser.add_argument('-t', '--target', help='target language', required=True)
    parser.add_argument("-m", "--model", help="model to use", required=False, default='Helsinki')
    parser.add_argument("-l", "--max-length", help="maximum length", required=False, default=128, type=int)
    args = parser.parse_args()
    if args.model == 'Helsinki':
        try:
            translator = HelsinkiTranslator()
            translator.load(args.source, args.target)
        except Exception as e:
            if str(e) == 'Model not found':
                print("Unsupported language pair, try other models")
            else:
                print(e)
            exit(1)
    elif args.model == "MT5":
        if args.source != 'ja' or args.target != 'zh':
            raise Exception('Unsupported language pair')
        translator = MT5Ja2ZhTranslator(args.max_length)
        translator.load()
    else:
        raise Exception('Unsupported model')

    # select parser based on file extension
    file_parser = None
    extension = os.path.splitext(args.file)[1]
    if extension == '.srt':
        file_parser = SRTParser(args.file)
    elif extension == '.txt':
        file_parser = TXTParser(args.file)
    elif extension == '.csv':
        file_parser = CSVParser(args.file)
    else:
        raise Exception('Unsupported file type')

    print("Translation started")
    file_parser.load()
    for content in tqdm(file_parser, total=len(file_parser)):
        translated = translator.translate(content)
        file_parser.update(translated) 

    file_parser.save()


if __name__ == '__main__':
    cli()


