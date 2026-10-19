# Step 4: estimate p, q, M for digital still cameras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from helper_functions import bass_sales

df = pd.read_csv("data/cipa_shipments.csv")
year_list = df["year"].values
shipments = df["units_thousands"].values
period = np.arange(1, len(shipments) + 1)

# Starting values for p, q, M (M in thousands of units)
start_values = [0.01, 0.4, 1200000]
est, _ = curve_fit(bass_sales, period, shipments, p0=start_values)
p_est, q_est, M_est = est

model_fit = bass_sales(period, p_est, q_est, M_est)
r_squared = 1 - np.sum((shipments - model_fit) ** 2) / np.sum((shipments - shipments.mean()) ** 2)

print(f"p: {p_est:.6f}\nq: {q_est:.6f}\nM: {M_est:.0f} (thousand units)\nR^2: {r_squared:.3f}")

pd.DataFrame({"p": [p_est], "q": [q_est], "M": [M_est], "R2": [r_squared]}).to_csv(
    "data/bass_estimates.csv", index=False)

plt.figure(figsize=(8, 5))
plt.scatter(year_list, shipments, color="purple", label="CIPA values")
plt.plot(year_list, model_fit, label="model fit")
plt.title("Digital Still Camera Diffusion")
plt.xlabel("Year")
plt.ylabel("Shipments (1,000 units)")
plt.legend()
plt.savefig("img/digital_camera_fit.png", dpi=150)
plt.show()
