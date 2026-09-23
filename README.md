🛡️ RiskGuard AI

AI-Powered Transaction Risk Detection & Explainable Risk Intelligence Dashboard

RiskGuard AI is a machine-learning-powered transaction risk assessment system designed to identify potentially risky financial transactions by analyzing transaction and behavioral signals.

The system combines machine learning, behavioral analysis, explainable risk indicators, and interactive data visualization to transform transaction-level signals into an understandable risk assessment.

---

🚀 Live Demo

Live Application:
AI Risk Manager — Streamlit deployment

Source Code:
Naina137 / AI---Risk---Manager

Developer:
Naina Kumari

LinkedIn:
Naina Kumari

---

🎯 Problem Statement

Digital payment and financial platforms process a large number of transactions every day. Identifying potentially suspicious transactions requires analyzing multiple signals rather than relying only on transaction amount.

Some potentially important signals include:

- Unusually high transaction amounts
- Unusual transaction times
- High transaction frequency
- Multiple device changes
- Country or location mismatch
- Repeated failed attempts
- Unusual account behavior

A risk-management system should not only identify potentially risky transactions, but should also provide an understandable explanation of why a transaction was flagged.

---

💡 Proposed Solution

RiskGuard AI provides an interactive AI-based risk assessment workflow.

The system takes transaction and behavioral information as input and passes the features through a trained Random Forest Classifier.

The model generates a risk probability which is converted into an easy-to-understand risk assessment:

- 🟢 Low Risk
- 🟠 Medium Risk
- 🔴 High Risk

The dashboard then presents the assessment together with the signals that contributed to the risk evaluation.

Core Flow

Transaction & Behavioural Data
            ↓
      Data Processing
            ↓
     Feature Preparation
            ↓
    Random Forest Model
            ↓
      Risk Probability
            ↓
     Risk Classification
            ↓
 Explainable Risk Indicators
            ↓
 Recommended Verification Action

---

✨ Key Features

1. 🎯 AI Transaction Risk Scanner

Users can enter transaction and behavioral information such as:

- Transaction amount
- Transaction hour
- Account age
- Transactions in the last 24 hours
- Device changes
- Country/location mismatch
- Failed attempts

The system then generates an AI-based risk assessment.

---

2. 📊 Dynamic Risk Score

The application converts the model's predicted probability into a percentage-based risk score.

Example:

Risk Score: 87%

Risk Level:
🔴 HIGH RISK

The dashboard uses a visual risk gauge to make the result easier to understand.

---

3. 🧠 Explainable Risk Indicators

RiskGuard AI does not stop at a prediction.

It provides understandable indicators such as:

- High transaction amount
- Unusual transaction time
- High transaction velocity
- Multiple device changes
- Country/location mismatch
- Multiple failed attempts

This helps users understand the factors associated with the model's decision.

---

4. 📈 Risk Intelligence Dashboard

The application provides interactive analytics including:

- Overall risk distribution
- Risk rate by transaction hour
- Transaction amount distribution
- Transaction velocity analysis
- Transaction amount vs. transaction frequency
- Risk rate vs. device changes
- Risk rate vs. failed attempts

These visualizations help identify behavioral patterns in the prototype dataset.

---

5. 🧠 Model Insights

The dashboard includes model-level insights using feature importance from the trained Random Forest model.

This helps visualize which input features contribute most strongly to the model's learned decision process.

---

6. 🏗️ System Architecture

The application provides a dedicated architecture view showing the complete processing pipeline:

┌───────────────────────┐
│ Transaction Data      │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Data Processing       │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Feature Engineering   │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Random Forest Model   │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Risk Probability      │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Explainable Analysis  │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Recommended Action    │
└───────────────────────┘

---

🤖 Machine Learning

Algorithm

The current prototype uses:

Random Forest Classifier

The model is trained using transaction and behavioral features.

Input Features

Feature| Description
"transaction_amount"| Value of the transaction
"hour"| Hour at which the transaction occurred
"account_age_days"| Age of the account
"transactions_last_24h"| Number of transactions within 24 hours
"device_changes"| Number of device changes
"country_mismatch"| Whether a location/country mismatch exists
"failed_attempts"| Number of failed attempts

Model Configuration

Algorithm: Random Forest Classifier
Estimators: 150
Random State: 42
Class Weight: Balanced
Train/Test Split: 80/20

---

📊 Dataset

For this prototype, a synthetic transaction dataset containing 3,000 transactions was generated locally.

The dataset was created to demonstrate the complete machine-learning and risk-scoring pipeline without using real customer, payment, or personally identifiable information.

Dataset Features

transaction_amount
hour
account_age_days
transactions_last_24h
device_changes
country_mismatch
failed_attempts
is_risky

Important Note

«This is a prototype and does not use real Razorpay customer or payment data.»

The synthetic dataset is intended to demonstrate the technical workflow and dashboard functionality.

---

🛠️ Technology Stack

Programming Language

- Python

Data Processing

- Pandas
- NumPy

Machine Learning

- Scikit-learn
- Random Forest Classifier

Dashboard & Visualization

- Streamlit
- Plotly

Model Persistence

- Joblib

Development & Version Control

- Git
- GitHub

Deployment

- Streamlit Community Cloud

---

📁 Project Structure

AI---Risk---Manager/
│
├── app.py
│       └── Main Streamlit dashboard
│
├── generate_data.py
│       └── Synthetic transaction dataset generator
│
├── train.py
│       └── Machine learning training pipeline
│
├── transactions.csv
│       └── Generated transaction dataset
│
├── risk_model.pkl
│       └── Trained Random Forest model
│
├── requirements.txt
│       └── Python dependencies
│
└── README.md
        └── Project documentation

---

⚙️ How It Works

Step 1 — Generate Dataset

The project first generates synthetic transaction records containing transaction and behavioral signals.

python generate_data.py

This creates:

transactions.csv

---

Step 2 — Train the Model

The generated dataset is loaded and divided into training and testing sets.

python train.py

The Random Forest model is trained and saved as:

risk_model.pkl

---

Step 3 — Launch the Dashboard

Install the required dependencies:

pip install -r requirements.txt

Then launch the application:

streamlit run app.py

The Streamlit dashboard opens locally and provides the complete risk-analysis interface.

---

🖥️ Dashboard Modules

🎯 Risk Scanner

Real-time interactive transaction risk assessment.

📊 Intelligence Center

Visual analytics for transaction and behavioral patterns.

🧠 Model Insights

Feature importance and machine-learning model information.

🏗️ System Design

End-to-end architecture and future evolution of the solution.

---

🔐 Risk Decision Logic

The prototype maps model probability into three operational categories:

0% – 39%
🟢 LOW RISK

40% – 69%
🟠 MEDIUM RISK

70% – 100%
🔴 HIGH RISK

The classification is intended for demonstration and prototype decision-support purposes.

---

📌 Example Risk Scenario

A transaction with signals such as:

Transaction Amount: ₹50,000
Transaction Hour: 02:00
Account Age: 30 days
Transactions / 24h: 25
Device Changes: 3
Country Mismatch: Yes
Failed Attempts: 4

can trigger multiple risk indicators.

The dashboard then presents:

🔴 HIGH RISK

Risk Score: [Model Generated Score]

Potential Indicators:
• High transaction amount
• Unusual transaction time
• High transaction velocity
• Multiple device changes
• Location mismatch
• Multiple failed attempts

The score is generated by the trained model and is not manually assigned.

---

📈 Why Explainability Matters

A risk model should not only answer:

«"Is this transaction risky?"»

It should also help answer:

«"What signals contributed to this assessment?"»

RiskGuard AI therefore combines the machine-learning prediction with human-readable risk indicators.

This creates a more transparent decision-support workflow.

---

🚀 Future Scope

The current system is a prototype. Future versions can evolve into a production-oriented risk intelligence platform.

Planned Improvements

- Real-time transaction stream processing
- Advanced anomaly detection
- Fraud-specific classification models
- Adaptive risk thresholds
- Real-time alert generation
- Human-in-the-loop transaction review
- Device fingerprint intelligence
- Behavioral profiling
- Graph-based transaction relationship analysis
- Model drift monitoring
- Continuous model retraining
- Production payment infrastructure integration
- API-based risk scoring
- Explainable AI using advanced interpretability techniques

---

🧪 Current Prototype Limitations

The current version intentionally uses synthetic data.

Therefore, the model's performance should not be interpreted as real-world fraud-detection performance.

For a production system, the model would require:

- Realistic and representative transaction data
- Proper fraud labels
- Strong class-imbalance handling
- Cross-validation
- Precision/Recall analysis
- F1-score
- ROC-AUC / PR-AUC
- False-positive monitoring
- Model drift detection
- Security and privacy controls
- Continuous validation

---

🔒 Security & Privacy

RiskGuard AI does not use real customer payment information in this prototype.

The dataset is synthetic and generated specifically for demonstration.

No:

- Customer credentials
- Payment credentials
- Card numbers
- Bank information
- Personal financial records

are used by the prototype.

---

💻 Local Setup

Clone the repository

git clone <repository-url>
cd AI---Risk---Manager

Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Generate dataset

python generate_data.py

Train model

python train.py

Run application

streamlit run app.py

---

🌐 Deployment

The application is deployed using Streamlit Community Cloud.

The GitHub repository contains the application source code, model artifact, generated prototype dataset, and dependency configuration required for deployment.

---

🎯 Buildathon Track

Track 2 — AI Risk Manager

RiskGuard AI focuses on using machine learning and behavioral transaction analysis to support automated risk identification and explainable decision-making.

---

👩‍💻 Developer

Naina Kumari

Computer Science & Engineering — Data Science

Interested in:

- Data Science
- Machine Learning
- Artificial Intelligence
- Data Analytics
- Full-Stack Development
- Cybersecurity

Connect

- GitHub: Naina137
- LinkedIn: Naina Kumari

---

⭐ Project Highlights

✓ AI-powered transaction risk assessment
✓ Random Forest machine-learning model
✓ Explainable risk indicators
✓ Dynamic risk scoring
✓ Interactive Streamlit dashboard
✓ Plotly visual analytics
✓ Behavioural risk analysis
✓ Model feature importance
✓ Synthetic 3,000-transaction dataset
✓ GitHub version control
✓ Streamlit Cloud deployment
✓ Prototype-ready architecture

---

⚠️ Disclaimer

RiskGuard AI is an educational and buildathon prototype created to demonstrate an AI-based transaction risk-management workflow.

It is not a production fraud-detection system and should not be used to make real financial decisions without proper validation, security review, regulatory compliance, and production-grade data and infrastructure.

---

⭐ If you found this project interesting, consider giving the repository a star!
