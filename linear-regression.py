import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split


df=pd.read_csv("student-mat.csv",sep=";")
print(df.head())
print(df.columns)







