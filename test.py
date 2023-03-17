import pandas as pd
import hashlib

df = pd.read_csv("User-1.csv")

last = df.iloc[-1]['ID']

df['Password'] = df['Password'].replace(hashlib.sha256(''))
