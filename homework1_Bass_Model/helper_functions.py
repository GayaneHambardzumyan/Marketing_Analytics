import numpy as np


def bass_sales(period, p, q, M):
    # S(t) = p*M + (q - p)*N(t-1) - (q/M)*N(t-1)^2
    predicted = np.zeros(len(period))
    total = np.zeros(len(period)) 

    for i in range(len(period)):
        prev_total = total[i - 1] if i > 0 else 0
        predicted[i] = p * M + (q - p) * prev_total - (q / M) * prev_total**2
        total[i] = prev_total + predicted[i]
    return predicted
