#Transformando JSON em CSV 
#É necessário a extenção PANDAS


import pandas as pd
import json

with open('data.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.to_csv('data.csv', index=False)
