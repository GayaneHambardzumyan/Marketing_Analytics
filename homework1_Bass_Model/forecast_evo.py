# Steps 5-7: forecast the diffusion of the Instax Wide Evo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import bass_sales

# p and q from the look-alike (saved by estimate_bass.py)
est = pd.read_csv("data/bass_estimates.csv")
p_est, q_est = est["p"][0], est["q"][0]

# Market potential (thousands of units)
# Fermi estimate: 100 million instax units sold since 1998 (Fujifilm, 2025)
# x 10% share of the WIDE format x 30% share of hybrid (Evo-type) models
M_evo = 100000 * 0.10 * 0.30   # = 3000 thousand units = 3 million

# Forecast horizon: 15 years, launch in 2025 (period 1)
future_period = np.arange(1, 16)
future_years = 2024 + future_period

evo_sales = bass_sales(future_period, p_est, q_est, M_evo)
evo_total = np.cumsum(evo_sales)

# Step 7: adopters by period
adopters_table = pd.DataFrame({
    "Year": future_years,
    "Period": future_period,
    "Annual_Adopters": evo_sales.round(0),
    "Cumulative_Adopters": evo_total.round(0),
    "Share_of_M_%": (evo_total / M_evo * 100).round(1),
})
print(adopters_table.to_string(index=False))
adopters_table.to_csv("data/evo_adopters_forecast.csv", index=False)

plt.figure(figsize=(8, 5))
plt.bar(future_years, evo_sales, color="orange", alpha=0.7, label="Annual adopters")
plt.plot(future_years, evo_total, color="purple", marker="o", label="Adopters (cumulative)")
plt.title("Instax Wide Evo: Predicted Diffusion")
plt.xlabel("Year")
plt.ylabel("Units in thousands")
plt.legend()
plt.savefig("img/evo_diffusion.png", dpi=150)
plt.show()
