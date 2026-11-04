import requests as rq
import json
import os
import pandas as pd



def create_embedding(prompt):
    request = rq.post('http://localhost:11434/api/embeddings', json={'model': 'bge-m3', 'prompt': prompt})
    embedding = request.json()['embedding']
    return embedding



files = os.listdir('mp3_to_text')
data = []
chunk_id = 0






for file in files:
    with open(f'mp3_to_text/{file}', 'r') as f:
        json_file=json.load(f)

    for chunk in json_file['chunked']:
        chunk['embedding']=create_embedding(chunk['text'])
        chunk['chunk_id']=chunk_id
        chunk_id+=1
        data.append(chunk)
        print('successfully created embedding for chunk text')
    print(f'successfully created embedding for file {file}')

    
      
df=pd.DataFrame(data)

with open('data_frame','w') as f:
    json.dump(data,f)