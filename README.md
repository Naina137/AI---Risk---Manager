<div align="center">

# 🛡️ RiskGuard AI

### AI-Powered Transaction Risk Intelligence & Explainable Risk Detection

**Detect • Analyze • Explain • Decide**

<br>

[![🚀 Live Demo](https://img.shields.io/badge/%F0%9F%9A%80%20LIVE%20DEMO-STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)
[![💻 Source Code](https://img.shields.io/badge/%F0%9F%92%BB%20SOURCE%20CODE-GITHUB-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Naina137/AI---Risk---Manager)
[![🔗 LinkedIn](https://img.shields.io/badge/%F0%9F%94%97%20LINKEDIN-NAINA%20KUMARI-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/naina-kumari-06373132b/)

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Naina137/AI---Risk---Manager)

</div>

---

## 📌 Overview

**RiskGuard AI** is an AI-powered transaction risk intelligence prototype designed to identify potentially risky financial transactions using transaction-level and behavioral signals.

The system combines **Machine Learning, Behavioral Analysis, Risk Scoring, Explainability, and Interactive Visualization** to transform transaction data into an understandable risk assessment.

### 🎯 Buildathon Track

**AI Risk Manager**

---

## 🚨 Problem Statement

Modern digital payment systems process a large number of transactions continuously.

Identifying potentially risky activity can require analyzing multiple signals rather than relying on a single transaction attribute.

Potential risk signals include:

- 💰 Unusual transaction amounts
- 🕐 Unusual transaction timing
- 🔄 High transaction frequency
- 📱 Multiple device changes
- 🌍 Country mismatch
- 🔐 Repeated failed attempts
- 👤 Unusual account behavior

The challenge is to analyze these signals together and provide an understandable risk assessment.

---

## 💡 Solution

RiskGuard AI provides an interactive machine-learning workflow that:

1. Collects transaction and behavioral information
2. Processes relevant risk features
3. Uses a trained Random Forest model
4. Generates a risk score
5. Classifies the transaction by risk level
6. Provides explainable risk indicators
7. Displays analytics through an interactive dashboard

### Risk Levels

| Level | Description |
|:---:|---|
| 🟢 **Low Risk** | Lower-risk transaction pattern |
| 🟠 **Medium Risk** | Transaction requires additional attention |
| 🔴 **High Risk** | Stronger risk indicators detected |

---

## 🧠 System Architecture

RiskGuard AI follows a structured end-to-end pipeline:

**Transaction Input**  
↓  
**Feature Processing**  
↓  
**Random Forest Risk Engine**  
↓  
**Risk Score**  
↓  
**Risk Classification**  
↓  
**Explainable Dashboard**  
↓  
**Analytics & Insights**

### Architecture Components

| Component | Purpose |
|---|---|
| 💳 Transaction Input | Receives transaction and behavioral information |
| ⚙️ Feature Processing | Prepares relevant features for the ML model |
| 🤖 Random Forest Risk Engine | Performs machine-learning based risk prediction |
| 📊 Risk Score | Produces probability-based risk assessment |
| 🎯 Risk Classification | Converts the assessment into Low, Medium, or High Risk |
| 🔍 Explainable Dashboard | Displays risk indicators and supporting information |
| 📈 Analytics & Insights | Provides visual analysis of transaction behavior |
| 🧠 Feature Importance | Shows important features used by the trained model |

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎯 Transaction Risk Scanner | Analyze an individual transaction |
| 🤖 ML Risk Prediction | Random Forest based classification |
| 📊 Risk Score | Probability-based risk assessment |
| 🔍 Explainable Indicators | Human-readable risk signals |
| 📈 Interactive Dashboard | Explore transaction and behavioral patterns |
| 🕐 Time Analysis | Analyze transaction behavior by hour |
| 💰 Amount Analysis | Analyze transaction amount patterns |
| 🔄 Velocity Analysis | Analyze transaction frequency |
| 📱 Device Analysis | Analyze device-change behavior |
| 🌍 Location Analysis | Analyze country mismatch |
| 🔐 Security Analysis | Analyze failed attempts |
| 🧠 Feature Importance | Understand important model features |
| ☁️ Cloud Deployment | Streamlit Community Cloud deployment |

---

## ⭐ Project Highlights

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

---

## 📊 Risk Intelligence

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

---

## 🤖 Machine Learning

### Model

The current prototype uses a **Random Forest Classifier**.

### Configuration

| Parameter | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Estimators | 150 |
| Random State | 42 |
| Class Weight | Balanced |
| Train/Test Split | 80/20 |

### Input Features

| Feature | Description |
|---|---|
| `transaction_amount` | Transaction amount |
| `hour` | Transaction hour |
| `account_age_days` | Account age |
| `transactions_last_24h` | Recent transaction frequency |
| `device_changes` | Number of device changes |
| `country_mismatch` | Location mismatch indicator |
| `failed_attempts` | Failed transaction/security attempts |

### Model Output

The model generates a risk prediction that is presented through the dashboard as:

🟢 **LOW RISK**  
🟠 **MEDIUM RISK**  
🔴 **HIGH RISK**

---

## 🔍 Explainable Risk Assessment

A risk-management system should not only answer:

> **"Is this transaction risky?"**

It should also help answer:

> **"Which signals are associated with this assessment?"**

RiskGuard AI presents human-readable indicators such as:

- 💰 High transaction amount
- 🕐 Unusual transaction timing
- 🔄 High transaction velocity
- 📱 Multiple device changes
- 🌍 Country mismatch
- 🔐 Multiple failed attempts

This creates a more understandable and transparent decision-support workflow.

---

## 📈 Analytics Dashboard

The dashboard provides interactive visual analysis for exploring transaction behavior.

### Analytics Include

- 📊 Risk distribution
- 🕐 Risk by transaction hour
- 💰 Transaction amount distribution
- 🔄 Transaction velocity
- 📱 Risk vs. device changes
- 🔐 Risk vs. failed attempts
- 🌍 Country mismatch analysis
- 📈 Transaction amount patterns
- 🧠 Model feature importance

The dashboard combines **transaction-level assessment** with **overall behavioral analytics**.

---

## 🗃️ Dataset

The prototype uses a **synthetic dataset containing 3,000 transaction records**.

The dataset was generated specifically for demonstrating the machine-learning risk assessment workflow without using real customer payment information.

### Dataset Fields

- `transaction_amount`
- `hour`
- `account_age_days`
- `transactions_last_24h`
- `device_changes`
- `country_mismatch`
- `failed_attempts`
- `is_risky`

### 🔐 Privacy

No real customer payment information is used.

The prototype does not contain:

- ❌ Card numbers
- ❌ Bank account information
- ❌ Payment credentials
- ❌ Real customer financial records
- ❌ Real customer payment data

---

## 🛠️ Technology Stack

<div align="center">

### 🐍 Programming Language

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

### 📊 Data Processing & Analysis

[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

### 🤖 Machine Learning

[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

### 📈 Data Visualization

[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

### 🌐 Web Application

[![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

### 📦 Model Persistence

[![Joblib](https://img.shields.io/badge/Joblib-Model%20Persistence-4B8BBE?style=for-the-badge)](https://joblib.readthedocs.io/)

### 🔧 Version Control & Source Code

[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Naina137/AI---Risk---Manager)

### ☁️ Deployment

[![Streamlit Cloud](https://img.shields.io/badge/Streamlit%20Cloud-Live%20Deployment-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)

</div>

---

## 📁 Project Structure

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit application |
| `generate_data.py` | Synthetic transaction data generation |
| `train.py` | Machine-learning training pipeline |
| `risk_model.pkl` | Trained Random Forest model |
| `transactions.csv` | Synthetic transaction dataset |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

### 💻 Source Code

👉 [**View RiskGuard AI Source Code on GitHub**](https://github.com/Naina137/AI---Risk---Manager)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

    git clone https://github.com/Naina137/AI---Risk---Manager.git
    cd AI---Risk---Manager

### 2️⃣ Create a Virtual Environment

**Windows**

    python -m venv venv
    venv\Scripts\activate

**Linux / macOS**

    python3 -m venv venv
    source venv/bin/activate

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Generate Dataset

    python generate_data.py

### 5️⃣ Train the Model

    python train.py

This generates:

    risk_model.pkl

### 6️⃣ Run the Application

    streamlit run app.py

The application will open at:

    http://localhost:8501

---

## ☁️ Deployment

RiskGuard AI is deployed using **Streamlit Community Cloud**.

### Deployment Flow

**Local Development**  
↓  
**Python Application**  
↓  
**Git Repository**  
↓  
[**GitHub Repository**](https://github.com/Naina137/AI---Risk---Manager)  
↓  
**Streamlit Community Cloud**  
↓  
[**Live Risk Dashboard**](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)

### 🚀 Deployed Application

[![Open Live App](https://img.shields.io/badge/%F0%9F%9A%80%20OPEN%20LIVE%20APP-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)

---

## 🔗 Important Links

| Resource | Link |
|---|---|
| 🚀 Live Demo | [**RiskGuard AI — Live Application**](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app) |
| 💻 Source Code | [**RiskGuard AI — GitHub Repository**](https://github.com/Naina137/AI---Risk---Manager) |
| 👩‍💻 LinkedIn | [**Naina Kumari — LinkedIn**](https://www.linkedin.com/in/naina-kumari-06373132b/) |
| 🐙 GitHub Profile | [**Naina137 — GitHub**](https://github.com/Naina137) |

---

## 👩‍💻 Developer

<div align="center">

# Naina Kumari

### Computer Science & Engineering — Data Science

**Data Science • Machine Learning • Artificial Intelligence • Data Analytics • Cybersecurity • Software Development**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-Naina137-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Naina137)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Naina%20Kumari-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/naina-kumari-06373132b/)

<br>

### 🔗 Project Resources

[🚀 **Live Demo**](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)  
[💻 **Source Code / GitHub Repository**](https://github.com/Naina137/AI---Risk---Manager)  
[🔗 **Connect on LinkedIn**](https://www.linkedin.com/in/naina-kumari-06373132b/)

</div>

---

## 🏆 Buildathon Context

### 🎯 Track: AI Risk Manager

RiskGuard AI was developed as a prototype for an **AI Risk Manager** challenge.

The project demonstrates how machine learning and behavioral transaction signals can be combined to create an intelligent risk-assessment layer between transaction data and operational decision-making.

### Core Concept

**Transaction Data**  
+  
**Behavioral Signals**  
+  
**Machine Learning**  
+  
**Risk Scoring**  
+  
**Explainability**  
+  
**Interactive Analytics**  
↓  
**AI Risk Intelligence**

---

## 🧪 Technical Challenges

### 1. Feature Design

Selecting transaction and behavioral features that can represent meaningful risk signals.

### 2. Synthetic Data Generation

Creating a structured dataset for experimentation without using real financial information.

### 3. Machine Learning Pipeline

The project follows:

**Data Generation → Data Processing → Feature Selection → Model Training → Model Persistence → Risk Prediction**

### 4. Explainability

Converting model predictions and behavioral signals into understandable risk indicators.

### 5. Interactive Visualization

Combining risk prediction, metrics, charts, and insights into a single dashboard.

### 6. Deployment

Deploying the application as an accessible web application through Streamlit Community Cloud.

---

## 🔄 Complete Project Workflow

| Stage | Process |
|---|---|
| 1️⃣ | Transaction / Behavioral Input |
| 2️⃣ | Feature Processing |
| 3️⃣ | Random Forest ML Engine |
| 4️⃣ | Risk Score Generation |
| 5️⃣ | Risk Classification |
| 6️⃣ | Explainable Indicators |
| 7️⃣ | Analytics Dashboard |
| 8️⃣ | Decision Support |

---

## 🎯 Why RiskGuard AI?

RiskGuard AI focuses on three core principles:

### 🔴 Detect

Identify potentially risky transaction patterns.

### 🔵 Analyze

Understand transaction and behavioral signals.

### 🟢 Explain

Present understandable indicators behind the assessment.

**Detect → Analyze → Explain → Decision Support**

---

## 🔮 Future Scope

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

---

## 📌 Project Information

| Category | Details |
|---|---|
| Project Name | RiskGuard AI |
| Track | AI Risk Manager |
| Domain | AI / Machine Learning / FinTech |
| Primary Language | [Python](https://www.python.org/) |
| ML Algorithm | Random Forest Classifier |
| Dataset | Synthetic Transaction Dataset |
| Records | 3,000 |
| Interface | [Streamlit](https://streamlit.io/) |
| Visualization | [Plotly](https://plotly.com/) |
| ML Framework | [Scikit-learn](https://scikit-learn.org/) |
| Data Analysis | [Pandas](https://pandas.pydata.org/) + [NumPy](https://numpy.org/) |
| Model Storage | Joblib |
| Deployment | [Streamlit Community Cloud](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app) |
| Source Code | [GitHub Repository](https://github.com/Naina137/AI---Risk---Manager) |

---

## 📊 Project Status

| Component | Status |
|---|---|
| Dataset Generation | ✅ Completed |
| ML Model | ✅ Implemented |
| Risk Prediction | ✅ Implemented |
| Risk Scoring | ✅ Implemented |
| Explainability | ✅ Implemented |
| Analytics Dashboard | ✅ Implemented |
| Visualization | ✅ Implemented |
| GitHub Repository | [✅ Available](https://github.com/Naina137/AI---Risk---Manager) |
| Cloud Deployment | [✅ Live](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app) |

---

## ⚠️ Disclaimer

**RiskGuard AI is an educational and buildathon prototype.**

It is **not a production fraud-detection system or financial decision-making system**.

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

[![🚀 LIVE DEMO](https://img.shields.io/badge/%F0%9F%9A%80%20LIVE%20DEMO-OPEN%20APP-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai---risk---manager-cpxhbr4uexjwz9bkdfo3rh.streamlit.app)

[![💻 GITHUB](https://img.shields.io/badge/%F0%9F%92%BB%20GITHUB-VIEW%20SOURCE-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Naina137/AI---Risk---Manager)

[![🔗 LINKEDIN](https://img.shields.io/badge/%F0%9F%94%97%20LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/naina-kumari-06373132b/)

<br><br>

⭐ **If you found this project interesting, consider starring the repository!**

</div>
