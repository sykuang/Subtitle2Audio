sykuang: generate readme.md

GitHub Copilot: # Project Title

This project is a Python script that generates an audio file from a subtitle file using Text-to-Speech (TTS).

## Description

The script takes a subtitle file as input and generates an audio file. It uses the `argparse` library to parse command line arguments. The user can specify the voice, output filename, voice style, voice style degree, and maximum sentence length. The script reads the subtitle file, generates an audio file for each subtitle using TTS, and then combines all the audio files into a single output file.

## Installation

This project requires Python 3 and the following Python libraries installed:

- `pydub`
- `argparse`
- `srt`

To install these libraries, you can use pip:

```bash
pip install -r requirments.txt
```

## Usage

To run the script, you can use the following command:

### Copy env
``` bash
cp .env.example .env
```

### Run command
```bash
python main.py <subtitle_file> --voice <voice_name> --output <output_filename> --style <voice_style> --styledegree <voice_style_degree> --max-sentence <max_sentence_length>
```
```bash
python main.py '.\a.srt' --voice en-US-AndrewMultilingualNeural --style customerservice
```
Replace `<subtitle_file>`, `<voice_name>`, `<output_filename>`, `<voice_style>`, `<voice_style_degree>`, and `<max_sentence_length>` with your desired values.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)