import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="RiskGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LOAD DATA + MODEL
# ============================================================

model = joblib.load("risk_model.pkl")
data = pd.read_csv("transactions.csv")

# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(37,99,235,0.15), transparent 28%),
        radial-gradient(circle at 90% 15%, rgba(124,58,237,0.12), transparent 25%),
        linear-gradient(135deg, #070b14 0%, #0b1220 45%, #101827 100%);
    color: #f8fafc;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080d18, #0d1424);
    border-right: 1px solid rgba(148,163,184,0.15);
}

.hero {
    background:
        linear-gradient(135deg,
        rgba(15,23,42,0.96),
        rgba(23,37,84,0.92));
    border: 1px solid rgba(96,165,250,0.25);
    border-radius: 24px;
    padding: 32px;
    margin-bottom: 22px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 0;
}

.hero-subtitle {
    color: #a8b6cc;
    font-size: 17px;
    margin-top: 8px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(59,130,246,0.12);
    border: 1px solid rgba(96,165,250,0.25);
    color: #93c5fd;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .5px;
}

.kpi {
    background: rgba(15,23,42,0.72);
    border: 1px solid rgba(148,163,184,0.14);
    border-radius: 18px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.16);
}

.kpi-label {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 600;
}

.kpi-value {
    font-size: 29px;
    font-weight: 800;
    margin-top: 8px;
}

.kpi-small {
    color: #64748b;
    font-size: 12px;
    margin-top: 5px;
}

.panel {
    background: rgba(15,23,42,0.68);
    border: 1px solid rgba(148,163,184,0.13);
    border-radius: 20px;
    padding: 22px;
    margin-top: 18px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.14);
}

.panel-title {
    font-size: 20px;
    font-weight: 750;
    margin-bottom: 5px;
}

.panel-subtitle {
    color: #7f8da3;
    font-size: 13px;
    margin-bottom: 16px;
}

.signal {
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
}

.signal-title {
    font-weight: 700;
    font-size: 14px;
}

.signal-text {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 4px;
}

.high {
    border-left: 4px solid #ef4444;
}

.medium {
    border-left: 4px solid #f59e0b;
}

.low {
    border-left: 4px solid #22c55e;
}

.action-box {
    background: linear-gradient(
        135deg,
        rgba(30,41,59,.85),
        rgba(15,23,42,.9)
    );
    border: 1px solid rgba(96,165,250,.20);
    border-radius: 18px;
    padding: 20px;
}

.architecture {
    text-align: center;
    padding: 22px;
    border-radius: 18px;
    background: rgba(15,23,42,.7);
    border: 1px solid rgba(96,165,250,.15);
}

.arch-step {
    display: inline-block;
    padding: 12px 16px;
    margin: 5px;
    border-radius: 12px;
    background: rgba(37,99,235,.10);
    border: 1px solid rgba(96,165,250,.2);
    color: #bfdbfe;
    font-weight: 650;
    font-size: 13px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 30px 0 10px;
}

div[data-testid="stMetric"] {
    background: rgba(15,23,42,.65);
    border: 1px solid rgba(148,163,184,.12);
    padding: 12px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🛡️ RiskGuard AI")

    st.caption("AI-powered transaction risk intelligence")

    st.divider()

    section = st.radio(
        "Workspace",
        [
            "🎯 Risk Scanner",
            "📊 Intelligence",
            "🧠 Model Insights",
            "🏗️ System Design"
        ]
    )

    st.divider()

    st.markdown("### System Status")

    st.success("● ML Engine Online")

    st.caption("Random Forest Risk Classifier")

    st.caption("Prototype Dataset: 3,000 transactions")

    st.divider()

    st.caption(
        "Prototype uses synthetic transaction data. "
        "No real customer or payment information is used."
    )

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">

<span class="badge">AI RISK INTELLIGENCE • PROTOTYPE</span>

<div class="hero-title">
🛡️ RiskGuard AI
</div>

<div class="hero-subtitle">
Intelligent transaction risk detection with explainable AI
</div>

<p style="color:#718096;margin-top:16px;max-width:900px;">
Analyze transaction behavior, detect suspicious patterns,
generate a dynamic risk score and understand <b>why</b> a
transaction may require attention.
</p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# KPI OVERVIEW
# ============================================================

total = len(data)
risky = int(data["is_risky"].sum())
safe = total - risky
risk_rate = round((risky / total) * 100, 2)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-label">TRANSACTIONS ANALYZED</div>
        <div class="kpi-value">{total:,}</div>
        <div class="kpi-small">Prototype transaction population</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-label">FLAGGED TRANSACTIONS</div>
        <div class="kpi-value">{risky:,}</div>
        <div class="kpi-small">Model-labelled elevated risk</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-label">LOW-RISK TRANSACTIONS</div>
        <div class="kpi-value">{safe:,}</div>
        <div class="kpi-small">Transactions below risk threshold</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi">
        <div class="kpi-label">RISK RATE</div>
        <div class="kpi-value">{risk_rate}%</div>
        <div class="kpi-small">Across prototype dataset</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# RISK SCANNER
# ============================================================

if section == "🎯 Risk Scanner":

    st.markdown("""
    <div class="panel">
        <div class="panel-title">🎯 Real-Time Transaction Risk Scanner</div>
        <div class="panel-subtitle">
        Enter transaction and behavioral signals. The ML engine
        evaluates the transaction and generates an explainable risk assessment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:

        st.markdown("### 💳 Transaction Signals")

        amount = st.number_input(
            "Transaction Amount (₹)",
            min_value=1.0,
            value=5000.0,
            step=500.0
        )

        hour = st.slider(
            "Transaction Hour",
            0,
            23,
            14
        )

        transactions = st.number_input(
            "Transactions in Last 24 Hours",
            min_value=1,
            max_value=100,
            value=5
        )

    with right:

        st.markdown("### 👤 Behavioural Signals")

        account_age = st.number_input(
            "Account Age (days)",
            min_value=1,
            max_value=5000,
            value=365
        )

        device_changes = st.number_input(
            "Device Changes",
            min_value=0,
            max_value=20,
            value=0
        )

        failed_attempts = st.number_input(
            "Failed Attempts",
            min_value=0,
            max_value=20,
            value=0
        )

        mismatch_text = st.selectbox(
            "Country / Location Mismatch",
            ["No", "Yes"]
        )

    st.write("")

    analyze = st.button(
        "⚡ RUN AI RISK ANALYSIS",
        use_container_width=True
    )

    if analyze:

        mismatch = 1 if mismatch_text == "Yes" else 0

        input_data = pd.DataFrame([{
            "transaction_amount": amount,
            "hour": hour,
            "account_age_days": account_age,
            "transactions_last_24h": transactions,
            "device_changes": device_changes,
            "country_mismatch": mismatch,
            "failed_attempts": failed_attempts
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        score = round(float(probability) * 100, 2)

        # -----------------------------------------
        # RISK CLASS
        # -----------------------------------------

        if score >= 70:
            level = "HIGH RISK"
            emoji = "🔴"
            css = "high"
            recommendation = "Hold for additional verification"
        elif score >= 40:
            level = "MEDIUM RISK"
            emoji = "🟠"
            css = "medium"
            recommendation = "Request additional verification"
        else:
            level = "LOW RISK"
            emoji = "🟢"
            css = "low"
            recommendation = "Allow / continue standard monitoring"

        st.divider()

        st.markdown("## 📡 AI Decision")

        r1, r2 = st.columns([1.2, 1])

        with r1:

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=score,
                    number={
                        "suffix": "%",
                        "font": {"size": 42}
                    },
                    title={
                        "text": "Transaction Risk Score",
                        "font": {"size": 18}
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "color": "#ef4444",
                            "thickness": 0.25
                        },
                        "steps": [
                            {
                                "range": [0, 40],
                                "color": "#123c2a"
                            },
                            {
                                "range": [40, 70],
                                "color": "#4a3612"
                            },
                            {
                                "range": [70, 100],
                                "color": "#4b1717"
                            }
                        ]
                    }
                )
            )

            fig.update_layout(
                height=350,
                margin=dict(l=25, r=25, t=60, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font={"color": "white"}
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with r2:

            st.markdown(
                f"""
                <div class="signal {css}" style="margin-top:25px;">
                    <div style="font-size:13px;color:#94a3b8;">
                    AI ASSESSMENT
                    </div>
                    <div style="font-size:30px;font-weight:800;margin:10px 0;">
                    {emoji} {level}
                    </div>
                    <div style="font-size:15px;">
                    Risk probability
                    </div>
                    <div style="font-size:36px;font-weight:800;">
                    {score}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="action-box">
                <b>Recommended Action</b>
                <br><br>
                {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )

        # -----------------------------------------
        # RISK FACTORS
        # -----------------------------------------

        st.markdown("## 🧠 Why was this transaction flagged?")

        factors = []

        if amount > 10000:
            factors.append(
                ("🔴", "High transaction amount",
                 "Amount crosses the prototype high-value threshold.")
            )

        if hour <= 4:
            factors.append(
                ("🟠", "Unusual transaction time",
                 "Transaction occurs during late-night hours.")
            )

        if transactions > 15:
            factors.append(
                ("🔴", "High transaction velocity",
                 "More than 15 transactions were observed within 24 hours.")
            )

        if device_changes >= 2:
            factors.append(
                ("🔴", "Device instability",
                 "Multiple device changes were detected.")
            )

        if mismatch == 1:
            factors.append(
                ("🔴", "Location mismatch",
                 "The transaction location differs from the expected country.")
            )

        if failed_attempts >= 3:
            factors.append(
                ("🔴", "Repeated failed attempts",
                 "Multiple failed authentication/payment attempts were detected.")
            )

        if not factors:
            st.success(
                "✓ No major risk indicators were triggered."
            )
        else:

            cols = st.columns(2)

            for i, factor in enumerate(factors):

                icon, title, desc = factor

                with cols[i % 2]:

                    st.markdown(
                        f"""
                        <div class="signal">
                        <div class="signal-title">
                        {icon} {title}
                        </div>
                        <div class="signal-text">
                        {desc}
                        </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        # -----------------------------------------
        # TRANSACTION PROFILE
        # -----------------------------------------

        st.markdown("## 📋 Transaction Profile")

        p1, p2, p3, p4 = st.columns(4)

        p1.metric("Amount", f"₹{amount:,.0f}")
        p2.metric("Transactions / 24h", transactions)
        p3.metric("Device Changes", device_changes)
        p4.metric("Failed Attempts", failed_attempts)

        profile = pd.DataFrame({
            "Signal": [
                "Transaction amount",
                "Transaction hour",
                "Account age",
                "Transactions / 24h",
                "Device changes",
                "Country mismatch",
                "Failed attempts"
            ],
            "Observed Value": [
                f"₹{amount:,.2f}",
                f"{hour}:00",
                f"{account_age} days",
                transactions,
                device_changes,
                mismatch_text,
                failed_attempts
            ]
        })

        st.dataframe(
            profile,
            use_container_width=True,
            hide_index=True
        )

# ============================================================
# INTELLIGENCE
# ============================================================

elif section == "📊 Intelligence":

    st.markdown("## 📊 Risk Intelligence Center")

    st.caption(
        "Explore behavioural patterns across the prototype transaction population."
    )

    # --------------------------------------------------------
    # RISK DISTRIBUTION
    # --------------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:

        risk_counts = data["is_risky"].value_counts()

        pie_df = pd.DataFrame({
            "Status": [
                "Low Risk",
                "Elevated Risk"
            ],
            "Transactions": [
                int(risk_counts.get(0, 0)),
                int(risk_counts.get(1, 0))
            ]
        })

        fig = px.pie(
            pie_df,
            names="Status",
            values="Transactions",
            hole=0.58,
            title="Risk Distribution"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=390
        )

        st.plotly_chart(fig, use_container_width=True)

    with c2:

        hourly = data.groupby("hour")["is_risky"].mean().reset_index()
        hourly["risk_rate"] = hourly["is_risky"] * 100

        fig = px.line(
            hourly,
            x="hour",
            y="risk_rate",
            markers=True,
            title="Risk Rate by Transaction Hour"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=390,
            xaxis_title="Hour of day",
            yaxis_title="Risk rate (%)"
        )

        st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------------
    # AMOUNT ANALYSIS
    # --------------------------------------------------------

    st.markdown("## 💰 Transaction Behaviour")

    c3, c4 = st.columns(2)

    with c3:

        fig = px.histogram(
            data,
            x="transaction_amount",
            color="is_risky",
            nbins=35,
            title="Transaction Amount Distribution",
            opacity=0.75
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

    with c4:

        fig = px.scatter(
            data.sample(min(1000, len(data)), random_state=42),
            x="transactions_last_24h",
            y="transaction_amount",
            color="is_risky",
            size="failed_attempts",
            hover_data=[
                "device_changes",
                "country_mismatch"
            ],
            title="Transaction Velocity vs Amount"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------------
    # DEVICE + FAILURE ANALYSIS
    # --------------------------------------------------------

    st.markdown("## 🔐 Behavioural Risk Signals")

    c5, c6 = st.columns(2)

    with c5:

        device = (
            data.groupby("device_changes")["is_risky"]
            .mean()
            .reset_index()
        )

        device["risk_rate"] = device["is_risky"] * 100

        fig = px.bar(
            device,
            x="device_changes",
            y="risk_rate",
            title="Risk Rate vs Device Changes"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=360
        )

        st.plotly_chart(fig, use_container_width=True)

    with c6:

        failures = (
            data.groupby("failed_attempts")["is_risky"]
            .mean()
            .reset_index()
        )

        failures["risk_rate"] = failures["is_risky"] * 100

        fig = px.bar(
            failures,
            x="failed_attempts",
            y="risk_rate",
            title="Risk Rate vs Failed Attempts"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=360
        )

        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# MODEL INSIGHTS
# ============================================================

elif section == "🧠 Model Insights":

    st.markdown("## 🧠 Explainable AI Model Center")

    st.caption(
        "Understand which signals influence the Random Forest model."
    )

    features = [
        "Transaction Amount",
        "Transaction Hour",
        "Account Age",
        "Transactions / 24h",
        "Device Changes",
        "Country Mismatch",
        "Failed Attempts"
    ]

    importance = model.feature_importances_

    imp_df = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(
        "Importance",
        ascending=True
    )

    fig = px.bar(
        imp_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Model Feature Importance"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "white"},
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("## 🔎 Model Details")

    a, b, c = st.columns(3)

    a.metric(
        "Algorithm",
        "Random Forest"
    )

    b.metric(
        "Estimators",
        "150"
    )

    c.metric(
        "Features",
        "7"
    )

    st.markdown("""
    <div class="panel">

    <div class="panel-title">
    How the AI decision works
    </div>

    <div class="panel-subtitle">
    The model receives transaction and behavioural signals,
    learns patterns from the training dataset and returns
    a probability of elevated risk.
    </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SYSTEM DESIGN
# ============================================================

else:

    st.markdown("## 🏗️ System Architecture")

    st.caption(
        "End-to-end architecture of the AI Risk Manager prototype."
    )

    st.markdown("""
    <div class="architecture">

    <span class="arch-step">💳 Transaction Data</span>
    →
    <span class="arch-step">🧹 Preprocessing</span>
    →
    <span class="arch-step">⚙️ Feature Engineering</span>
    →
    <span class="arch-step">🤖 Random Forest</span>
    →
    <span class="arch-step">📊 Risk Score</span>
    →
    <span class="arch-step">🧠 Explanation</span>
    →
    <span class="arch-step">🚨 Action</span>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎯 Core Capabilities")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="panel">
        <h3>🔍 Detection</h3>
        <p style="color:#94a3b8;">
        Identifies behavioural patterns associated with
        elevated transaction risk.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="panel">
        <h3>🧠 Explainability</h3>
        <p style="color:#94a3b8;">
        Shows the behavioural signals that contributed
        to the risk assessment.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="panel">
        <h3>⚡ Decision Support</h3>
        <p style="color:#94a3b8;">
        Converts model output into a practical verification
        recommendation.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 🚀 Future Evolution")

    st.markdown("""
    - Real-time transaction streaming
    - Anomaly detection using unsupervised learning
    - Adaptive risk thresholds
    - Human-review workflow
    - Device fingerprint intelligence
    - Graph-based transaction relationship analysis
    - Continuous model monitoring
    - Production payment API integration
    """)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
RiskGuard AI • AI Risk Manager • Buildathon Prototype<br>
Synthetic data used for demonstration — no real payment/customer data.
</div>
""", unsafe_allow_html=True)