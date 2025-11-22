Machine learning–based prediction of RAIR abnormality using high-resolution anorectal manometry data

🚀 Overview

This project applies machine learning techniques to pediatric high-resolution anorectal manometry (ARM) data to predict RAIR (Rectoanal Inhibitory Reflex) abnormality.
The goal is to support clinical decision-making by identifying physiologic pressure and relaxation patterns associated with impaired RAIR responses.

This repository contains the final research paper, feature evaluation tables, and visualization results.

🧠 Key Highlights

Predicts RAIR abnormality using ARM-derived physiologic features

Models evaluated: Logistic Regression (LASSO), SVM, Decision Tree, Random Forest, Gradient Boosting, Ensemble

Best model: Ensemble + Random Forest

Top predictors:

IAS Percent Relaxation (40%, 20%, 30%)

Resting anal pressure

IAS relaxation duration

Push & squeeze maneuver metrics

📄 Project Files (located in /docs/)
File	Description
Project_Report_Final.pdf	Full academic paper with methods, results, tables, and discussion
Project_Report_Final.docx	Editable Word version of the final paper
Feature_Importance_Table_1.pdf	Feature ranking across models
Table_evaluation_metrix.docx	Evaluation metrics for all ML models
Visualization Result.docx	Result images & plots

All key documents are stored in the docs/ directory for easy access.

🔍** Methodology Summary**

Dataset source: De-identified pediatric ARM studies curated at SSM Health Cardinal Glennon Children’s Hospital

**Predictors:
Resting pressure

IAS relaxation percentages (10–60%)

IAS relaxation duration

Push & squeeze metrics

Rectal sensation

**Outcome:**

0 = RAIR present

1 = RAIR absent/abnormal

Preprocessing:

Missing value imputation

StandardScaler normalization

SMOTE oversampling for imbalance

Evaluation metrics:

Accuracy, Precision, Recall, Specificity

F1 Score

Cohen’s Kappa

ROC–AUC

📈 Key Results

Ensemble Model and Random Forest outperformed all others, capturing non-linear patterns in ARM physiology.

IAS relaxation and resting pressures were the strongest predictors of abnormal RAIR.

These features align with known clinical physiology and validate the model’s interpretability.

Pediatric-arm-ML/
│── README.md
│── docs/
│     ├── Project_Report_Final.pdf
│     ├── Project_Report_Final.docx
│     ├── Feature_Importance_Table_1.pdf
│     ├── Table_evaluation_metrix.docx
│     └── Visualization Result.docx

Acknowledgment

Data curated by Dhiren Patel,
SSM Health Cardinal Glennon Children’s Hospital.

📬 Contact

For questions or collaboration:
Chaitali Chaudhari
