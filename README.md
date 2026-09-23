<div align="center">

# 🛡️ RiskGuard AI

### AI-Powered Transaction Risk Intelligence & Explainable Risk Detection

**Detect • Analyze • Explain • Decide**

[🚀 LIVE DEMO](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app) • [💻 GITHUB](https://github.com/Naina137/AI---Risk---Manager) • [🔗 LINKEDIN](https://www.linkedin.com/in/naina-kumari-06373132b/)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)

</div>

---

# 🚀 Live Demo

👉 https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app

# 📌 Overview

RiskGuard AI is an AI-powered transaction risk intelligence prototype designed to identify potentially risky financial transactions using transaction-level and behavioral signals.

The system combines Machine Learning, Behavioral Analysis, Risk Scoring, Explainability, and Interactive Visualization to transform transaction data into an understandable risk assessment.

🎯 Buildathon Track: AI Risk Manager

# 🚨 Problem Statement

Modern digital payment systems process large numbers of transactions continuously.

Suspicious activity may not always be identified by transaction amount alone. Multiple behavioral signals may indicate increased transaction risk.

Potential risk signals include:

- 💰 Unusual transaction amounts
- 🕐 Unusual transaction timing
- 🔄 High transaction frequency
- 📱 Multiple device changes
- 🌍 Country mismatch
- 🔐 Repeated failed attempts
- 👤 Unusual account behavior

The challenge is to analyze these signals together and provide an understandable risk assessment.

# 💡 Proposed Solution

RiskGuard AI provides an interactive machine-learning-based transaction risk assessment workflow.

Transaction Data
→ Feature Processing
→ Behavioral Risk Analysis
→ Random Forest ML Model
→ Risk Probability
→ Risk Classification
→ Explainable Risk Indicators
→ Interactive Dashboard

The system transforms transaction information into a risk assessment and provides supporting indicators so that the result is easier to understand.

# 🧠 System Architecture

┌─────────────────────────────────────────┐
│            TRANSACTION INPUT            │
│                                         │
│ Amount • Time • Account • Device        │
│ Location • Failed Attempts • Velocity   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          FEATURE PROCESSING              │
│                                         │
│ Transaction & Behavioral Signals        │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          RANDOM FOREST MODEL             │
│                                         │
│          Machine Learning Engine        │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│            RISK PROBABILITY              │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          RISK CLASSIFICATION             │
│                                         │
│     🟢 LOW   🟠 MEDIUM   🔴 HIGH        │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          EXPLAINABLE DASHBOARD           │
│                                         │
│ Risk Score • Indicators • Analytics     │
│ Feature Importance • Insights           │
└─────────────────────────────────────────┘

# ✨ Key Features

| Feature | Description |
|---|---|
| 🎯 Transaction Risk Scanner | Analyze an individual transaction |
| 🤖 ML Prediction | Random Forest based risk classification |
| 📊 Risk Score | Probability-based risk assessment |
| 🔍 Explainability | Human-readable risk indicators |
| 📈 Interactive Analytics | Explore transaction and behavioral patterns |
| 🕐 Time Analysis | Analyze transaction behavior by hour |
| 💰 Amount Analysis | Analyze transaction amount patterns |
| 🔄 Velocity Analysis | Analyze transaction frequency |
| 📱 Device Analysis | Analyze device-change behavior |
| 🌍 Location Analysis | Analyze country mismatch |
| 🔐 Security Analysis | Analyze failed attempts |
| 🧠 Feature Importance | Understand important model features |
| 🌐 Web Dashboard | Interactive Streamlit application |
| ☁️ Cloud Deployment | Streamlit Community Cloud deployment |

# ⭐ Project Highlights

- 🤖 AI-powered transaction risk assessment
- 🌲 Random Forest machine-learning model
- 🎯 Dynamic risk scoring
- 🔍 Explainable risk indicators
- 📊 Behavioral risk analysis
- 📈 Interactive Streamlit dashboard
- 📊 Plotly-based visual analytics
- 🧠 Model feature importance
- 🗃️ Synthetic 3,000-transaction dataset
- 🕐 Time-based transaction analysis
- 💰 Transaction amount analysis
- 🔄 Transaction velocity analysis
- 📱 Device-change analysis
- 🌍 Country mismatch analysis
- 🔐 Failed-attempt analysis
- ☁️ Streamlit Cloud deployment
- 💻 GitHub version control
- 🏗️ Prototype-ready architecture

# 📊 Risk Intelligence

RiskGuard AI analyzes multiple transaction and behavioral signals.

### 💰 Transaction Signals

- Transaction amount
- Transaction hour
- Transactions in the last 24 hours

### 👤 Account Signals

- Account age
- Device changes

### 🔐 Security Signals

- Country mismatch
- Failed attempts

These signals are processed by the machine-learning model to generate the transaction risk assessment.

# 🤖 Machine Learning

## Model

The current prototype uses a Random Forest Classifier.

### Model Configuration

- Algorithm: Random Forest Classifier
- Estimators: 150
- Random State: 42
- Class Weight: Balanced
- Train/Test Split: 80/20

### Input Features

- transaction_amount
- hour
- account_age_days
- transactions_last_24h
- device_changes
- country_mismatch
- failed_attempts

### Risk Output

🟢 LOW RISK

🟠 MEDIUM RISK

🔴 HIGH RISK

# 🔍 Explainable Risk Assessment

A risk-management system should not only answer:

"Is this transaction risky?"

It should also help answer:

"Which signals are associated with this assessment?"

RiskGuard AI presents human-readable indicators such as:

- 💰 High transaction amount
- 🕐 Unusual transaction timing
- 🔄 High transaction velocity
- 📱 Multiple device changes
- 🌍 Country mismatch
- 🔐 Multiple failed attempts

This creates a more understandable and transparent decision-support workflow.

# 📈 Analytics Dashboard

The dashboard provides interactive visual analysis for exploring transaction behavior.

Analytics include:

- 📊 Risk distribution
- 🕐 Risk by transaction hour
- 💰 Transaction amount distribution
- 🔄 Transaction velocity
- 📱 Risk vs. device changes
- 🔐 Risk vs. failed attempts
- 🌍 Country mismatch analysis
- 📈 Transaction amount patterns
- 🧠 Model feature importance

# 🗃️ Dataset

The prototype uses a synthetic dataset containing 3,000 transaction records.

The dataset was generated specifically for demonstrating the machine-learning risk assessment workflow without using real customer payment information.

### Dataset Fields

- transaction_amount
- hour
- account_age_days
- transactions_last_24h
- device_changes
- country_mismatch
- failed_attempts
- is_risky

### 🔐 Privacy

No real customer payment information is used.

The prototype does not contain:

- Card numbers
- Bank account information
- Payment credentials
- Real customer financial records
- Real customer payment data

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| ML Algorithm | Random Forest Classifier |
| Visualization | Plotly |
| Web Application | Streamlit |
| Model Persistence | Joblib |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

# 📁 Project Structure

AI---Risk---Manager/

├── app.py
├── generate_data.py
├── train.py
├── risk_model.pkl
├── transactions.csv
├── requirements.txt
└── README.md

### File Description

- app.py — Main Streamlit application
- generate_data.py — Synthetic transaction data generation
- train.py — Machine-learning training pipeline
- risk_model.pkl — Trained Random Forest model
- transactions.csv — Synthetic transaction dataset
- requirements.txt — Python dependencies
- README.md — Project documentation

# ⚙️ Installation & Setup

### 1. Clone Repository

git clone https://github.com/Naina137/AI---Risk---Manager.git

cd AI---Risk---Manager

### 2. Create Virtual Environment

Windows:

python -m venv venv

venv\Scripts\activate

Linux/macOS:

python3 -m venv venv

source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Generate Dataset

python generate_data.py

### 5. Train Model

python train.py

This generates the trained model:

risk_model.pkl

### 6. Run Application

streamlit run app.py

The application will open at:

http://localhost:8501

# ☁️ Deployment

RiskGuard AI is deployed using Streamlit Community Cloud.

Deployment Flow:

Local Development
→ Python Application
→ Git Repository
→ GitHub
→ Streamlit Community Cloud
→ Live Risk Dashboard

# 🔗 Important Links

🚀 Live Demo:
https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app

💻 GitHub Repository:
https://github.com/Naina137/AI---Risk---Manager

👩‍💻 LinkedIn:
https://www.linkedin.com/in/naina-kumari-06373132b/

🐙 GitHub Profile:
https://github.com/Naina137

# 👩‍💻 Developer

## Naina Kumari

Computer Science & Engineering — Data Science

Interests:

Data Science • Machine Learning • Artificial Intelligence • Data Analytics • Cybersecurity • Software Development

GitHub:
https://github.com/Naina137

LinkedIn:
https://www.linkedin.com/in/naina-kumari-06373132b/

# 🏆 Buildathon Context

### 🎯 Track: AI Risk Manager

RiskGuard AI was developed as a prototype for an AI Risk Manager challenge.

The project demonstrates how machine learning and behavioral transaction signals can be combined to create an intelligent risk-assessment layer between transaction data and operational decision-making.

### Core Concept

Transaction Data
+
Behavioral Signals
+
Machine Learning
+
Risk Scoring
+
Explainability
+
Interactive Analytics
↓
AI Risk Intelligence

# 🧪 Technical Challenges

### 1. Feature Design

Selecting transaction and behavioral features that can represent meaningful risk signals.

### 2. Synthetic Data Generation

Creating a structured dataset for experimentation without using real financial information.

### 3. Machine Learning Pipeline

Data Generation
→ Data Processing
→ Feature Selection
→ Model Training
→ Model Persistence
→ Risk Prediction

### 4. Explainability

Converting model predictions and behavioral signals into understandable risk indicators.

### 5. Interactive Visualization

Combining risk prediction, metrics, charts, and insights into a single dashboard.

### 6. Deployment

Deploying the application as an accessible web application through Streamlit Community Cloud.

# 🏅 Complete Project Workflow

USER / TRANSACTION
        ↓
INPUT SIGNALS
        ↓
DATA PROCESSING
        ↓
ML ENGINE
        ↓
RANDOM FOREST
        ↓
RISK SCORE
        ↓
LOW / MEDIUM / HIGH
        ↓
EXPLANATION
        ↓
INTERACTIVE DASHBOARD

# 🎯 Why RiskGuard AI?

RiskGuard AI focuses on three core principles:

### 🔴 DETECT

Identify potentially risky transaction patterns.

### 🔵 ANALYZE

Understand transaction and behavioral signals.

### 🟢 EXPLAIN

Present understandable indicators behind the assessment.

DETECT
↓
ANALYZE
↓
EXPLAIN
↓
DECISION SUPPORT

# 🔮 Future Scope

The current version is a prototype and can be extended with:

### 🤖 Advanced AI

- Advanced anomaly detection
- Fraud-specific classification
- Ensemble learning
- Adaptive risk thresholds
- Advanced Explainable AI

### ⚡ Real-Time Processing

- Real-time transaction streams
- Instant risk scoring
- Real-time alerts
- Event-driven processing

### 🔐 Security Intelligence

- Device fingerprinting
- Behavioral profiling
- Account takeover detection
- Suspicious login analysis

### 🧠 Advanced Analytics

- Graph-based transaction analysis
- Network-based fraud detection
- Customer behavior profiling
- Model drift monitoring
- Continuous model retraining

### 🏗️ Production Capabilities

- REST API-based risk scoring
- Database integration
- Authentication and authorization
- Monitoring and logging
- Human-in-the-loop review
- Production-grade security and privacy controls

# 📌 Project Information

| Category | Details |
|---|---|
| Project Name | RiskGuard AI |
| Track | AI Risk Manager |
| Domain | AI / Machine Learning / FinTech |
| Primary Language | Python |
| ML Algorithm | Random Forest Classifier |
| Dataset | Synthetic Transaction Dataset |
| Records | 3,000 |
| Interface | Streamlit |
| Visualization | Plotly |
| ML Framework | Scikit-learn |
| Model Storage | Joblib |
| Deployment | Streamlit Community Cloud |
| Version Control | GitHub |

# 📊 Project Status

| Component | Status |
|---|---|
| Dataset Generation | ✅ Completed |
| ML Model | ✅ Implemented |
| Risk Prediction | ✅ Implemented |
| Risk Scoring | ✅ Implemented |
| Explainability | ✅ Implemented |
| Analytics Dashboard | ✅ Implemented |
| Visualization | ✅ Implemented |
| GitHub Repository | ✅ Available |
| Cloud Deployment | ✅ Live |

# ⚠️ Disclaimer

RiskGuard AI is an educational and buildathon prototype.

It is not a production fraud-detection system or financial decision-making system.

Real-world deployment would require:

- Representative production datasets
- Extensive model validation
- Security testing
- Privacy controls
- Regulatory compliance
- Bias and fairness evaluation
- Continuous monitoring
- Model-performance evaluation
- Human oversight

---

<div align="center">

# 🛡️ RiskGuard AI

### Intelligent • Explainable • Data-Driven Risk Assessment

**Detect • Analyze • Explain • Decide**

<br>

🚀 [LIVE DEMO](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)

💻 [GITHUB](https://github.com/Naina137/AI---Risk---Manager)

🔗 [LINKEDIN](https://www.linkedin.com/in/naina-kumari-06373132b/)

<br>

⭐ **If you found this project interesting, consider starring the repository!**

</div>
