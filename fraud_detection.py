# ================================
# STEP 1: Import Libraries
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# ================================
# STEP 2: Load Dataset
# ================================
# Replace 'transactions.csv' with your file path
df = pd.read_csv("transactions.csv")

print("Shape of dataset:", df.shape)
print("Columns:", df.columns)

# ================================
# STEP 3: Basic EDA
# ================================
print(df.head())
print(df.info())
print(df["fraud_label"].value_counts())  # Assuming fraud label column is 'fraud_label'

# Check fraud ratio
fraud_ratio = df["fraud_label"].mean()
print(f"Fraud cases ratio: {fraud_ratio:.4f}")

# Plot fraud distribution
sns.countplot(x="fraud_label", data=df)
plt.title("Fraud vs Legitimate Transactions")
plt.show()

# ================================
# STEP 4: Preprocessing
# ================================
# Example: Convert datetime column
if "transaction_date" in df.columns:
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df["day_of_week"] = df["transaction_date"].dt.dayofweek
    df["hour"] = df["transaction_date"].dt.hour
    df["month"] = df["transaction_date"].dt.month

# Encode categorical features
cat_cols = df.select_dtypes(include=["object"]).columns
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# Scale numerical features
scaler = StandardScaler()
num_cols = df.select_dtypes(include=["int64","float64"]).columns.drop("fraud_label")
df[num_cols] = scaler.fit_transform(df[num_cols])

# ================================
# STEP 5: Train-Test Split
# ================================
X = df.drop("fraud_label", axis=1)
y = df["fraud_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# ================================
# STEP 6: Train Model
# ================================
model = RandomForestClassifier(class_weight="balanced", random_state=42, n_estimators=200)
model.fit(X_train, y_train)

# ================================
# STEP 7: Evaluation
# ================================
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
