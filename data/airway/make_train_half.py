import pandas as pd

train_half = pd.read_csv('./train.csv',encoding='cp949')

zero = train_half[train_half['target'] == 0][:3309].iloc[1:]
one = train_half[train_half['target'] == 1].iloc[1:]

final = pd.concat([zero,one])

final.to_csv('./train_half.csv')

