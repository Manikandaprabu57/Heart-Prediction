import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Select relevant features for training
X = data[['age', 'sex', 'high_blood_pressure', 'serum_creatinine', 'ejection_fraction']]
y = data['DEATH_EVENT']

# Split data for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline for scaling and model training
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, 'heart_risk_model.pkl')
print("Model trained with selected features and saved successfully!")
