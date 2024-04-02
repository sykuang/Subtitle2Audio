from AzureTTS.main import tts
from dotenv import load_dotenv
from pydub import AudioSegment
from tempfile import TemporaryDirectory
import argparse
import srt
from pathlib import Path
load_dotenv()

def generate_blank_audio(duration: int):
    return AudioSegment.silent(duration=duration*1000)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",type=str,help="Subtitle file")
    parser.add_argument("--voice",type=str,default="en-US-AriaNeural",help="Voice name")
    parser.add_argument("--output",type=str,default="output.wav",help="output filename")
    parser.add_argument("--style",type=str,default="chat",help="Voice style")
    parser.add_argument("--styledegree",type=int,default=1,help="Voice style degree")
    parser.add_argument("-m","--max-sentence",type=int,default=0,help="Max sentence length, 0 for unlimited")
    args=parser.parse_args()
    with open(args.filename,mode="r",encoding="utf-8") as f:
        subs = list(srt.parse(f.read()))
    audios=[]
    with TemporaryDirectory() as tmp_dir:
        for i,sub in enumerate(subs):
            if args.max_sentence>0 and i>=args.max_sentence:
                break
            text = sub.content
            filename = Path(tmp_dir)/Path(f"audio_{i}.wav")
            tts(text, args.voice,  str(filename),args.style,args.styledegree)
            audios.append({"filename":filename,"start":sub.start.total_seconds(),"end":sub.end.total_seconds()})
        final_audio = AudioSegment.empty()
        for audio in audios:
            final_audio += AudioSegment.from_file(audio["filename"])
            final_audio += generate_blank_audio(int(audio["end"]-audio["start"]))
        final_audio.export(args.output,format="wav")
if __name__ == "__main__":
    main()
