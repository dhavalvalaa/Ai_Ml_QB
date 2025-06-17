import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Step 1: Simulate past normal behavior (e.g., daily spending in $)
past_transactions = np.random.normal(loc=100, scale=10, size=1000)
# average $50, normal behavior

# Step 2: New transaction comes in
new_transaction = int(input("enter transcation amont"))
# the user suddenly spent $120 today

# Step 3: Calculate deviation (Chi-Square score)
mean = np.mean(past_transactions)
std = np.std(past_transactions)

# Chi-Square score (simplified as squared deviation over variance)
chi_square_score = ((new_transaction - mean) ** 2) / (std ** 2)

# Step 4: Set a threshold (e.g., 95% confidence)
threshold = chi2.ppf(0.95, df=1)  # df=1 for one feature

# Step 5: Decision
if chi_square_score > threshold:
    print(f"⚠️ Suspicious transaction! Score = {chi_square_score:.2f} > Threshold = {threshold:.2f}")
else:
    print(f"✅ Normal transaction. Score = {chi_square_score:.2f} ≤ Threshold = {threshold:.2f}")

# (Optional) Visualize
plt.hist(past_transactions, bins=30, color='skyblue', edgecolor='black', alpha=0.7, density=True)
plt.axvline(new_transaction, color='red', linestyle='dashed', linewidth=2, label="New Transaction")
plt.title("Past User Transactions")
plt.xlabel("Transaction Amount ($)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
