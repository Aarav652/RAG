import requests as rq
import json
import os



def create_embedding(prompt):
    request = rq.post('http://localhost:11434/api/embeddings', json={'model': 'bge-m3', 'prompt': prompt})
    embedding = request.json()['embedding']
    return embedding



files = os.listdir('mp3_to_text')
data = []
chunk_id = 0



for file in files:
    with open(f'mp3_to_text/{file}', 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    try:
        chunks=json_file['chunked']
        
    # it will print json file who is not structure wise good
    except:
        print(file)


    # creating embeddings for the text of the file
    print(f'creating embedding for {file}')
    for chunk in chunks:
        chunk['embedding']=create_embedding(chunk['text'])
        chunk_id+=1
        chunk['chunk_id']=chunk_id
        data.append(chunk)

    print('done......')



with open('data_frame' , 'w') as f:
    json.dump(data,f)