import numpy as np
import numba as nb  

@nb.njit # Ca c'est pour compiler tout le bloc et realiser les simulations plus vite 
def run_pricer_monte_carlo(S0, r, sigma, T, n_simulations, nominal, P):
    if S0 <= 0:
        return 0.0, np.zeros(n_simulations)
    
    # 1. Mouvement brownien 
    Z = np.random.randn(n_simulations)

    # 2. Calcul du prix du sous jacent a terme
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    # 3. Calcul du Payoff de l'option : max((S_T - S0) / S0), 0 car capital protégé)
    perf_note = np.maximum((S_T - S0) / S0, 0)
    
    # Payoff final = Nominal + (Gain de participation)
    payoff = nominal * (1 + P * perf_note)

    # 4. On fait moyenne des scénarios possibles
    payoff_moyen = np.mean(payoff)
    
    # On ramène le prix futur à aujourd'hui 
    prix_actuel = payoff_moyen * np.exp(-r * T)
    
    return prix_actuel, S_T

# La fonction nous retourne le prix du produit aujourd'hui et le prix du sous jacent a terme

