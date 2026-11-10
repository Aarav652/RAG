##steps to see this project context


##step1: collect your videos in folder
the videos are collecte in the folder

##step2: convert videos to audios
using ffmpeg they are converted into audios and stored in the mp3 folder
in process_video.py this proccess occurs

##step3:mp3 to text
in sttp.py the mp3s are converted into text and saved in the mp3_to_text folder as chunks

##step4:creating embedding 
we have create embedding for the text of chunks

##step5:save chunks along with embeddings in data_frame
the chunks are save along with their text embeddings
this code are in the embedding for text of chunk.py

##step6:matching question and text embeddings
we will take question as input than make its embedding
here,in rea_match_chunk.py the chunks text embeddings are matched to question embedding 
at, last we will give the 3 best result

##this project is by turbo model of open-ai whisper
##i cant use the LLM because i dont have enough storage

