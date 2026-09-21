
import pandas as pd
data = pd.read_csv('PhiUSIIL_Phishing_URL_Dataset.csv')
print(data.columns)
print("Total rows:", len(data))
print(data.head())
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
features = data[['URLLength', 'NoOfLettersInURL', 'NoOfDegitsInURL', 'IsHTTPS', 'NoOfSubDomain']]
labels = data['label']
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)
