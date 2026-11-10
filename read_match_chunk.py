import pandas as pd
import requests as rq
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



# comes from the file emb.py
def create_embedding(prompt):
    request = rq.post('http://localhost:11434/api/embeddings', json={'model': 'bge-m3', 'prompt': prompt})
    embedding = request.json()['embedding']
    return embedding




# step1: load data
with open('data_frame','r') as f:
    data=pd.read_json(f)
# print(data)


#step2: do eda on data and remove empty embedding
data = data[data['embedding'].apply(len) > 0].reset_index(drop=True)


#step3: make the question input and its emedding
question=input('ask a question: ')
quest_emb=create_embedding(question)
print(quest_emb)


#step4:we will see the similarity of quest and text embedding
similarity=cosine_similarity(np.vstack(data['embedding']),[quest_emb]).flatten()
print(similarity)


# step5:we will find the top 3 similarity
top_similarity=3
top_similar_index=similarity.argsort()[::-1][0:top_similarity]#[::-1] reverse the top matches and than select top 3
print(top_similar_index)

# step6:make new_df where the chunks of top similarity is there
new_df=data.iloc[top_similar_index]
print(new_df)




