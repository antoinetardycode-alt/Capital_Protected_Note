import numpy as np
import scipy.stats as scp

def run_pricer(S0, r, sigma, T, nominal, P):

    # calcul de la Zc
    zc = nominal * np.exp( -r * T)

    # calcul du call, on applique la formule de black & scholes & merton afin d'obtenir un prix precis du call de la cpn
    K = S0
    
    d1 = (np.log( S0 / K ) + ( r + (sigma**2)/2)*T )/(sigma * np.sqrt(T))
    
    d2 = d1 - sigma * np.sqrt(T)

    Call = S0 * scp.norm.cdf(d1) - scp.norm.cdf(d2) * K * np.exp(-r * T)

    valeur_option = (nominal * P * Call) / S0
    # on additione le prix de l'option et du zero coupon afin d'obtenir le prix de notre CPN aujourd'hui
    prix_note = zc + valeur_option

    return prix_note

def simulate_index(S0, r, sigma, T, n_simulations): 
    #on utilise un mouvement brownien géometrique afin d'obtenir des prix positifs (des prix peuvent pas etre negatifs) qui suivent la propriété log normale
    Z = np.random.randn(n_simulations) 
    S_T = S0 * np.exp((r - sigma**2/2)*T + sigma*np.sqrt(T)*Z)
    return S_T

def run_payoff(S0, S_T, P, nominal): 
    # Calcul du remboursement : Nominal + (Participation * Performance Positive)
    # Si perf_sous_jacent < 0, np.maximum prend 0 -> on rend juste le nominal, dans le cas contraire, on recupère le nominal auquel on ajoute la performance du sous jacent, conditionnée par le taux de participation.
    payoff = np.maximum(nominal, nominal * (1 + P * (S_T - S0)/S0))
    return payoff 

# La fonction nous retourne le prix du produit aujourd'hui et les prix potentiels du sous jacent a terme

