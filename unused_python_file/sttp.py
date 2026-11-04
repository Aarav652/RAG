import whisper
import json
import os
model = whisper.load_model("turbo")

mp3s=os.listdir("mp3")
print(mp3s)

for mp3 in mp3s:
    file_name=mp3.split('.')[0]
    result=model.transcribe(audio=f"mp3/{mp3}",language="en",task="translate",word_timestamps=False,fp16=False)
    chunks=[]
    for result in result['segments']:
        chunks.append({
            "start": result['start'],
            "end": result['end'],
            "text": result['text']
        })
    with open(f"mp3_to_text/{file_name}.json", "w") as f:
        json.dump(chunks, f, indent=1)
   

