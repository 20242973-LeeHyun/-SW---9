sklearn 없이 하려면

import pandas as pd 
with open('abalone_attributes.txt', 'r') as f:
   columns = [line.strip() for line in f.readlines()] 
   df = pd.read_csv('abalone.txt', header=None, names=columns) 
   label = df['Sex'] 
   df = df.drop(columns=['Sex']) 

   #여기까진 동일 
#공식 활용 x-xmin/xmax-xmin
   for col in df.columns: 
       col_min = df[col].min() 
       col_max = df[col].max() 
       df[col] = (df[col] - col_min) / (col_max - col_min) 

#print(label)
print(df)
