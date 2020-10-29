import pandas as pd

prediction = pd.read_csv("./data/prediction.csv")
prediction['Score'] = 4.0

submission = prediction[['Id', 'Score']]
print(submission.head())
submission.to_csv("./data/submission.csv", index=False)
