# Capital Protected Note (CPN) Pricing & Simulation Tool

![Finance](https://img.shields.io/badge/Domain-Quantitative%20Finance-blue)
![Python](https://img.shields.io/badge/Language-Python%203.9+-green)
![Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B)

##  Project Overview
This repository contains a professional-grade tool for structuring and valuing **100% Capital Protected Notes (CPN)** on the S&P 500 index. The tool allows users to analyze the trade-off between bond floor protection and optionality upside.

### Components:
1. **Bond Leg**: A Zero-Coupon Bond (ZCB) used to guarantee the principal at maturity.
2. **Option Leg**: A European Call option to capture equity market performance.

---

##  Technical Features

### 1. Pricing Engine
* **Model**: Analytical **Black-Scholes-Merton (1973)** formula used for the Fair Value calculation of the embedded call.

### 2. Risk & Simulation
* **Monte Carlo Engine**: Simulates thousands of price paths using **Geometric Brownian Motion (GBM)**.
* **Payoff Analysis**: Visual representation of the note's value at maturity relative to the underlying's performance.



### 3. Stress Testing
* Scenario analysis for **Implied Volatility** shifts and **Interest Rate** fluctuations to observe the deformation of the product's Fair Value.

---

##  Installation & Usage

### Prerequisites
Ensure you have Python installed. It is recommended to use a virtual environment.

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
Step 2: Run the Dashboard
The project features an interactive Streamlit interface for real-time structuring.

Bash
streamlit run dashboard.py
