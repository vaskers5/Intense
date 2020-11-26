import pandas as pd
from Classifier import GenreClassifier

df = pd.read_csv('data_from_colab.csv')
classifier = GenreClassifier(df)
df['personality_type'] = classifier.get_psycho()


