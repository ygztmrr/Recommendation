import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
import uvicorn
import pandas as pd

# model

rules= pd.read_pickle("./rules.pkl")
#result=rules[rules['antecedents'] == {'Karpuz 8 kg'}].sort_values(['confidence'], ascending=False)[1:2].consequents.to_dict()
#print(result)



# init api
app = FastAPI()

#routes
@app.get('/')
def get_root():

	return {'message': 'Welcome to the HB Recommendation API'}
    
   
@app.get('/predict/{name}')
async def predict(name:str):
    result=rules[(rules['antecedents'] == {name})&(rules["consequents_len"]==1)].sort_values(['confidence'], ascending=False)[0:10].consequents.tolist()
    return result
    
    
if __name__ == '__main__':    
    uvicorn.run(app, host='127.0.0.1', port=8000)