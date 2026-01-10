import numpy as np
import scipy.stats as scp
from numba import jit

def run_pricer(S0, r, sigma, T, nominal, P, K, d):

    # calcul de la Zc
    zc = nominal * np.exp( -r * T)

    # calcul du call, on applique la formule de black & scholes & merton afin d'obtenir un prix precis du call de la cpn
    
    d1 = np.log( S0 / K ) + ( r - d + 0.5 * sigma**2)* T /(sigma * np.sqrt(T))
    
    d2 = d1 - sigma * np.sqrt(T)

    Call = S0 * np.exp(- d * T) * scp.norm.cdf(d1) - scp.norm.cdf(d2) * K * np.exp(-r * T)

    valeur_option = (nominal * P * Call) / S0
    # on additione le prix de l'option et du zero coupon afin d'obtenir le prix de notre CPN aujourd'hui
    prix_note = zc + valeur_option

    return prix_note

# Dans pricer.py
@jit(nopython=True)
def pricer_montecarlo(S0, r, sigma, T, nominal, P, d, K, n_simulations):
    drift = (r - d - 0.5 * sigma**2) * T
    vol_T = sigma * np.sqrt(T)
    Z = np.random.randn(n_simulations)
    
    # Calculs
    S_T = S0 * np.exp(drift + vol_T * Z)
    S_T_mirror = S0 * np.exp(drift + vol_T * (-Z))
    
    factor = nominal * P / S0
    
    # Payoffs
    payoff_Z = nominal + factor * np.maximum(S_T - K, 0) # On garde celui-ci pour le plot
    payoff_mirror = nominal + factor * np.maximum(S_T_mirror - K, 0)
    
    # Prix (Moyenne Antithétique)
    prix_pcn = np.exp(-r * T) * np.mean(0.5 * (payoff_Z + payoff_mirror))
    
    # RETURN : Prix + Vecteurs pour le dashboard
    return prix_pcn, S_T, payoff_Z


