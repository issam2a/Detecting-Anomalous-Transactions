# Mobile Money Fraud Detection

This project uses machine learning to detect fraudulent mobile money transactions using a real-world dataset of over 6 million records. We aim to build a robust classification model to distinguish between fraudulent and legitimate transactions with high accuracy.

---

## 📂 Dataset Overview

The dataset contains detailed transaction-level data:

| Column | Description |
| --- | --- |
| `step` | Time step of the transaction |
| `type` | Type of transaction (`TRANSFER`, `CASH_OUT`, etc.) |
| `amount` | Amount transferred |
| `nameOrig` | Sender's ID |
| `oldbalanceOrg` | Sender's balance before transaction |
| `newbalanceOrig` | Sender's balance after transaction |
| `nameDest` | Receiver's ID |
| `oldbalanceDest` | Receiver's balance before transaction |
| `newbalanceDest` | Receiver's balance after transaction |
| `isFraud` | 1 if the transaction is fraudulent, 0 otherwise |
| `isFlaggedFraud` | 1 if flagged by the system, 0 otherwise |

---

## 🧪 Project Workflow

### 1. **Data Loading & Preprocessing**

- Load and inspect data
- Remove irrelevant columns
- Check for nulls and inconsistencies

### 2. **Exploratory Data Analysis (EDA)**

- Fraud distribution across transaction types
- Imbalance in the dataset
- Suspicious balance changes

### 3. **Feature Engineering**

- Derived features like:
    - `errorOrig` = `oldbalanceOrg - newbalanceOrig - amount`
    - `balanceDiffOrig`, `balanceDiffDest`
- Flagging zero or negative balances

### 4. **Handling Class Imbalance**

- Used `class_weight='balanced'` in Random Forest
- Preserved fraud ratio with stratified splitting

### 5. **Modeling**

- Baseline: Logistic Regression
- Best Model: Random Forest Classifier
- Resampling with **SMOTE** to handle class imbalance  
- Evaluation with classification metrics and ROC-AUC
- Deployed **Streamlit App** where you can manually test transactions 

### 6. **Evaluation**

- **Classification Report**
- **ROC Curve and AUC**

---

## 🔍 Final Model Results

- Precision (fraud): 0.95 → when the model says "fraud", it’s right 95% of the time.
- Recall (fraud): 0.96 → it catches 96% of all frauds.
- ROC-AUC: 0.998 → almost perfect ranking ability.

Overall accuracy: basically 100% (but we don’t care much about accuracy here because of imbalance).




## 🛠️ Tools & Libraries

- Python
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `joblib`
- `imbalnced-learn`

---

## 📌 Key Takeaways

- Fraud occurs almost exclusively in `TRANSFER` and `CASH_OUT`
- Most system-flagged frauds were false positives
- Carefully engineered features like balance difference helped boost model accuracy
- Random Forest handled imbalance well and provided interpretability through feature importances

---
## ⚡ How to Run Locally

1. Clone the repo:
    
    ```bash
    git clone https://github.com/issam2a/Detecting-Anomalous-Transactions.git
    
    
    ```
    

Install dependencies:


pip install -r requirements.txt
Run the app:


streamlit run [app.py](http://app.py/)




✨ Author
Issam Issa  – LinkedIn : www.linkedin.com/in/issam-issa 