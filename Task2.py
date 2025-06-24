import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("C:\\Users\\Mohamed shapan\\Desktop\\SABA🙃\\Elevate Lab\\Task2\\Task2-Exploratory-Data-Analysis\\pokemon_data.csv")

print("📌 First 5 rows of the dataset:")
print(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Missing Values in Each Column:")
print(df.isnull().sum())

print("\n📌 Summary Statistics:")
print(df.describe())

print("\n📌 Columns in the Dataset:")
print(df.columns.tolist())


plt.figure(figsize=(8, 5))
sns.histplot(df['moves'], bins=20, kde=True)
plt.title('Distribution of Attack')
plt.xlabel('Attack')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df['height'])
plt.title('Boxplot of heght')
plt.show()

plt.figure(figsize=(10, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

selected_features = ['name','base_experience','height','weight','types','abilities']
sns.pairplot(df[selected_features])
plt.suptitle('Pairplot of Pokémon Stats', y=1.02)
plt.show()



