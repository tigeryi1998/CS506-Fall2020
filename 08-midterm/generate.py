import pandas as pd

trainingSet = pd.read_csv("./data/train.csv")
testingSet = pd.read_csv("./data/test.csv")

predictionSet = pd.merge(trainingSet, testingSet, left_on='Id', right_on='Id')
print(predictionSet.columns)

predictionSet = predictionSet.drop(columns=['Score_x'])
predictionSet = predictionSet.rename(columns={'Score_y': 'Score'})

print(predictionSet.columns)
predictionSet.to_csv("./data/prediction.csv", index=False)

X_train = trainingSet[trainingSet['Score'].notnull()]
print(trainingSet.shape)
print(X_train.shape)
X_train.to_csv("./data/X_train.csv", index=False)
