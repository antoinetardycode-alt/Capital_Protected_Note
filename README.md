# Capital Protected Note (CPN) Pricing & Simulation Tool

![Finance](https://img.shields.io/badge/Domain-Quantitative%20Finance-blue)
![Python](https://img.shields.io/badge/Language-Python%203.9+-green)
![Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

##  Project Overview
This repository provides a professional-grade dashboard for structuring and valuing **100% Capital Protected Notes (CPN)** linked to the S&P 500. The tool enables users to visualize the trade-off between the bond floor (protection) and the optionality (upside participation).

### Structured Product Components:
1.  **Bond Leg**: A Zero-Coupon Bond (ZCB) ensuring the principal is returned at maturity.
2.  **Option Leg**: A European Call option allowing investors to capture equity market growth.

---

##  Technical Features

### 1. Pricing Engine
* **Analytical Model**: Uses the **Black-Scholes-Merton (1973)** formula to determine the Fair Value of the embedded call option.
* **Greeks Calculation**: Real-time monitoring of Delta, Gamma, and Vega.

### 2. Risk & Simulation
* **Monte Carlo Engine**: Simulates price paths using **Geometric Brownian Motion (GBM)**.
* **Payoff Analysis**: Visualizes the note's performance at maturity relative to the underlying's spot price.



### 3. Scenario & Stress Testing
* Analysis of **Implied Volatility** smiles and **Interest Rate** shifts.
* Dynamic adjustment of the **Participation Rate** based on the remaining budget after the Bond Floor purchase.

---

##  Mathematical Framework

The total price of the Note $V_0$ is given by:
$$V_0 = \text{Bond Floor} + (\alpha \times \text{Call Option})$$

Where:
* **Bond Floor**: $F \times e^{-rT}$ (where $F$ is Face Value)
* **Participation Rate ($\alpha$)**: $\frac{V_0 - \text{Bond Floor}}{\text{Call Price}}$

The underlying follows the GBM SDE:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

---

##  Installation & Usage

### Prerequisites
* Python 3.9+
* Pip or Conda

### Step 1: Clone and Install
```bash
git clone [https://github.com/yourusername/cpn-pricing-tool.git](https://github.com/yourusername/cpn-pricing-tool.git)
cd cpn-pricing-tool
pip install -r requirements.txt
```
### Step 2: Launch the Dashboard
```bash
The interface is built with Streamlit for an interactive user experience.
```
### Author
Antoine Tardy Aspiring Structured Product Sales / Finance Student
