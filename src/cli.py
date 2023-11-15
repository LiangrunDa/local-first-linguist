from src.translator.Helsinki import HelsinkiTranslator
from src.parser.srt import SRTParser
from src.parser.txt import TXTParser
from src.parser.csv import CSVParser
import os
import argparse


def cli():
    parser = argparse.ArgumentParser(description='Translator for SRT files')
    parser.add_argument("-f", "--file", help="file to translate", required=True)
    parser.add_argument('-s', '--source', help='source language', required=True)
    parser.add_argument('-t', '--target', help='target language', required=True)
    parser.add_argument("-m", "--model", help="model to use", required=False, default='Helsinki')

    args = parser.parse_args()
    if args.model == 'Helsinki':
        translator = HelsinkiTranslator()
        translator.load(args.source, args.target)
    else:
        raise Exception('Unsupported model')

    # select parser based on file extension
    extension = os.path.splitext(args.file)[1]
    if extension == '.srt':
        parser = SRTParser(args.file)
    elif extension == '.txt':
        parser = TXTParser(args.file)
    elif extension == '.csv':
        parser = CSVParser(args.file)
    else:
        raise Exception('Unsupported file type')

    for content in parser:
        translated = translator.translate(content)
        parser.update(translated)

    parser.save()


if __name__ == '__main__':
    cli()

