import streamlit as st # le dashboard
import matplotlib.pyplot as plt # visualisation des graphiques
import yfinance as yf # datas d'internet
import pricer as pr # fonction du pricer

sp500 = yf.Ticker("^GSPC") # data sur s&p500
prix_SP = sp500.fast_info['last_price'] # dernier prix de l'actif sous jacent 
         
taux = yf.Ticker("^TNX") # taux sans risque, ici CBOE Interest Rate 10 Year T No (^TNX), contrainte data source free
taux_actuel = taux.fast_info['last_price'] /100 # formatage, BP a pourcentage

st.header('Dashboard de la Capital Protected Note') # C'est le titre du dashboard
st.sidebar.title('Paramètres de la Note') # on déclare nos paramètres

S0 = st.sidebar.number_input('Prix sous jacent', value = prix_SP, min_value=0.01) # dernier prix du S&P500
nominal = st.sidebar.number_input('Nominal', value=10000) # montant nominal qu'on souhaite investir
P = st.sidebar.slider('Taux participation', value = 0.8, min_value=0.0, max_value=2.00) # taux de participation a la performance
r_floor = st.sidebar.slider('Taux Floor', value = 0.00)
r = st.sidebar.number_input('Taux', value = taux_actuel, min_value=-0.001) # free risk rate 10 ans 
sigma = st.sidebar.slider('Volatilité', value = 0.2, min_value=0.050 , max_value=0.850 ) # volatilité implicite, 0.85 valeur extreme du vix (expl covid/ faillite leman brother)
T = st.sidebar.slider('Maturité', min_value= 1, max_value=15 ) # maturité du contrat
n_simulations = st.sidebar.slider('Nombre de simulations ', value = 1000, max_value = 100000) # nombre de simulations, on limite a 100000 pour eviter les crashs

prix_note = pr.run_pricer(S0, r, sigma, T, nominal, P, r_floor) # prix qu'on doit payer aujourd'hui si on veut detenir ce
S_T = pr.simulate_index(S0, r, sigma, T, n_simulations) # evolution des prix suivant un mouvement brownien geometrique 
payoff = pr.run_payoff(S0, S_T, P, nominal, r_floor) # profil de rendement de la partie optionel

col_1 , col_2 = st.columns(2)

with col_1 : 
    st.metric(label="Le prix de la note à aujourd'hui est:", value = f"{prix_note:.2f} €")

fig, ax = plt.subplots()
ax.scatter(S_T, payoff, alpha=0.5, s=1, label='Scénarios Monte Carlo')
ax.axhline(nominal, color='r', linestyle='--', label='Plancher (Protection)')
ax.set_title('Profil de remboursement à l\'échéance')
ax.set_xlabel('Prix du S&P 500 dans')
ax.set_ylabel('Payoff (€)')
ax.legend()

st.pyplot(fig)
