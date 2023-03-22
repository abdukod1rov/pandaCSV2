import pandas as pd
import hashlib

df = pd.read_csv("User-1.csv")
user_df = pd.read_csv("User_info-1.csv")
# last = df.iloc[-1]['ID']
#
# record = df.loc[df['ID'] == 3]
# last_index = int(user_df.iloc[-1]['ID'])
# print(record)
for index, row in df.iterrows():
    if row['Username'] == 'samandar' and row['Answer'] == 'hp':
        row['PSW'] = 'admin21'

print(df)
