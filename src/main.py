#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from myConvexHull import ConvexHull, connectThePoint

#%%
#load
data = datasets.load_iris()
# create df
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    connectPointX, connectPointY = connectThePoint(hull)
    for e in range(len(hull)):
        plt.plot(connectPointX[e], connectPointY[e], colors[i])
plt.legend()

#%%
#load
data2 = datasets.load_iris()
# create df
df2 = pd.DataFrame(data2.data, columns=data2.feature_names)
df2['Target'] = pd.DataFrame(data2.target)
print(df2.shape)
df2.head()

plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Sepal Width vs Sepal Length')
plt.xlabel(data2.feature_names[2])
plt.ylabel(data2.feature_names[3])
for i in range(len(data2.target_names)):
    bucket2 = df2[df2['Target'] == i]
    bucket2 = bucket2.iloc[:,[2,3]].values
    hull2 = ConvexHull(bucket2)
    plt.scatter(bucket2[:, 0], bucket2[:, 1], label=data2.target_names[i])
    connectPointX2, connectPointY2 = connectThePoint(hull2)
    for e in range(len(hull2)):
        plt.plot(connectPointX2[e], connectPointY2[e], colors[i])
plt.legend()

#%%
#load
data3 = datasets.load_wine()
#create df
df3 = pd.DataFrame(data3.data, columns=data3.feature_names)
df3['Target'] = pd.DataFrame(data3.target)
print(df3.shape)
df3.head()
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Alchohol vs color_intensity')
plt.xlabel(data3.feature_names[0])
plt.ylabel(data3.feature_names[9])
for i in range(len(data3.target_names)):
    bucket3 = df3[df3['Target'] == i]
    bucket3 = bucket3.iloc[:,[0,9]].values
    hull3 = ConvexHull(bucket3)
    plt.scatter(bucket3[:, 0], bucket3[:, 1], label=data3.target_names[i])
    connectPointX3, connectPointY3 = connectThePoint(hull3)
    for e in range(len(hull3)):
        plt.plot(connectPointX3[e], connectPointY3[e], colors[i])
plt.legend()

# %%
