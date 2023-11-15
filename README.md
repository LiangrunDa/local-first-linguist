# Local-first Linguist:Translate your files locally

## What is Local-first Linguist?

Local-first Linguist is a local translator for different file formats. It is free and doesn't require any internet connection.

Current supported file formats:
- Text files: txt
- Tables: csv
- Subtitles: srt

TODO:
- md
- json
- xml

## How to use it?

1. Download this repository

```bash
git clone https://github.com/LiangrunDa/local-first-linguist.git
```

2. Install the dependencies

```bash
pip install torch
pip install transformers
pip install sentencepiece
```

3. Translate your files

```bash
translate -f <file_path> -s <source_language> -t <target_language>
```

for example:
```bash
translate -f samples/me.srt -s en -t zh
```

## Supported languages

Now I only integrated the [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) models, which supports 1400+ pairs. You can find the full list [here](https://huggingface.co/Helsinki-NLP).

Some languages abbreviations:
- English (en)
- Chinese (zh)
- Japanese (ja/jap)
- Spanish (es)
- French (fr)
- German (de)
- ...

TODO: Integrate [Fairseq](https://github.com/facebookresearch/fairseq)