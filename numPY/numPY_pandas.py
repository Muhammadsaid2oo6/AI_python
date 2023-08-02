import pandas as pd 


path = r"/home/said/Desktop/ai_2/AI_python/numPY/students.csv"
path2 = r"/home/said/Desktop/ai_2/AI_python/numPY/movie.csv"

df = pd.read_csv(path)
df2 = pd.read_csv(path2)

# print(df)
print(df.head(30))
print(df.shape)

