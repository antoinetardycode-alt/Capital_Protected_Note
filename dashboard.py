import streamlit as st # le dashboard
import matplotlib.pyplot as plt # visualisation des graphiques
import yfinance as yf # datas d'internet
import pricer as pr # fonction du pricer
import numpy as np

sp500 = yf.Ticker("^GSPC") # data sur s&p500
prix_SP = sp500.fast_info['last_price'] # dernier prix de l'actif sous jacent 

st.header('Capital Protected Note Dashboard') # C'est le titre du dashboard
st.sidebar.title('Pricing Inputs') # on déclare nos paramètres

S0 = st.sidebar.number_input('Spot Price', value = prix_SP, min_value=0.01) # dernier prix du S&P500
K = st.sidebar.number_input('Strike Price', value = S0, min_value = 0.00) # choix du niveau de strike
nominal = st.sidebar.number_input('Notional Amount', value=10000) # montant nominal qu'on souhaite investir
P = st.sidebar.slider('Participation Rate', value = 0.8, min_value=0.0, max_value=2.00) # taux de participation a la performance
r = st.sidebar.number_input('Risk-Free Rate', value = 0.03, min_value=-0.001) # free risk rate 10 ans 
sigma = st.sidebar.slider('Implied Volatility', value = 0.2, min_value=0.050 , max_value=0.850 ) # volatilité implicite, 0.85 valeur extreme du vix (expl covid/ faillite leman brother)
T = st.sidebar.slider('Maturity', min_value= 1, max_value=15 ) # maturité du contrat
n_simulations = st.sidebar.slider('MC Simulations', value = 1000, max_value = 100000) # nombre de simulations, on limite a 100000 pour eviter les crashs
d = st.sidebar.slider('Dividend Yield', value = 0.00, min_value= 0.00)

try:
    prix_note = pr.run_pricer(S0, r, sigma, T, nominal, P, K, d)
except:
    prix_note = 0.0 # Placeholder si tu n'as pas encore codé le BS

prix_pcn, ST_vec, payoff_vec = pr.pricer_montecarlo(S0, r, sigma, T, nominal, P, d, K, n_simulations) 

# 2. METRIQUES
col1, col2 = st.columns(2)
col1.metric("Price Closed-Form (BS)", f"{prix_note:.2f} €")
col2.metric("Price Monte Carlo", f"{prix_pcn:.2f} €", delta=f"{(prix_pcn-prix_note):.2f}")

fig, ax = plt.subplots(figsize=(10, 6))

display_limit = 2000
ax.scatter(ST_vec[:display_limit], payoff_vec[:display_limit], 
           alpha=0.4, s=5, c='blue', label='Scénarios MC (Échantillon)')

s_range = np.linspace(ST_vec.min(), ST_vec.max(), 100)
payoff_theo = nominal + (nominal * P / S0) * np.maximum(s_range - K, 0)
ax.plot(s_range, payoff_theo, color='red', linewidth=2, label='Payoff Théorique')

ax.axhline(nominal, color='green', linestyle='--', label='Capital Garanti')
ax.axvline(K, color='gray', linestyle=':', label=f'Strike ({K:.2f})')
ax.set_title(f'Payoff Profile | Capital Protected Note (Maturité {T} ans)', fontsize=12)
ax.set_xlabel('Spot à maturité ($S_T$)')
ax.set_ylabel('Payoff (€)')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3, linestyle='--')

st.pyplot(fig)
