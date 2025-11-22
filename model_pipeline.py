"""
Modeling Pipeline for RAIR Abnormality Prediction
NOTE:
This script contains NO real patient data.
All data is synthetic and used only to demonstrate the ML workflow used in the study.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ------------------------------------------------------------
# 1. SYNTHETIC DATA GENERATION (SAFE FOR PUBLIC RELEASE)
# ------------------------------------------------------------

np.random.seed(42)
n_samples = 300

# Synthetic ARM feature simulation (NO real data)
X = pd.DataFrame({
    'ARMRestPresMean': np.random.normal(45, 10, n_samples),
    'IASPercentRel20': np.random.normal(50, 12, n_samples),
    'IASPercentRel40': np.random.normal(30, 8, n_samples),
    'BearDownPush': np.random.normal(15, 4, n_samples),
    'SqueezeIncrease': np.random.normal(80, 20, n_samples),
    'RectalSensation': np.random.normal(20, 5, n_samples)
})

# Synthetic binary target
y = np.random.randint(0, 2, n_samples)

# ------------------------------------------------------------
# 2. TRAIN/TEST SPLIT
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------
# 3. SCALING
# ------------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ------------------------------------------------------------
# 4. MODEL TRAINING (LASSO, RF, GB)
# ------------------------------------------------------------

models = {
    "LASSO_Logistic": LogisticRegression(penalty="l1", solver="liblinear"),
    "RandomForest": RandomForestClassifier(n_estimators=200),
    "GradientBoosting": GradientBoostingClassifier()
}

results = {}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    
    results[name] = {
        "Accuracy": accuracy_score(y_test, preds),
        "Precision": precision_score(y_test, preds),
        "Recall": recall_score(y_test, preds),
        "F1 Score": f1_score(y_test, preds)
    }

# ------------------------------------------------------------
# 5. PRINT RESULTS
# ------------------------------------------------------------
print("\n=== MODEL PERFORMANCE (Synthetic Data) ===\n")
for m, r in results.items():
    print(f"{m}:")
    for metric, score in r.items():
        print(f"  {metric}: {round(score, 3)}")
    print()
