
import pandas as pd

import matplotlib.pyplot as plt

# Load customer data
df = pd.read_csv("customers.csv", sep="\t")

# Display first 5 rows
print(df.head())

# Display total rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column information
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check total records
print("\nTotal Customers:")
print(len(df))

# Total customers
total_customers = len(df)

# Count customers who left the company
churned_customers = (df["Churn"] == "Yes").sum()

# Calculate churn rate
churn_rate = (churned_customers / total_customers) * 100

# Count customers who stayed
active_customers = (df["Churn"] == "No").sum()

print("\n--- Customer Churn Analysis ---")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Active Customers:", active_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

# Analyze churn by contract type
print("\n--- Churn Analysis by Contract ---")

contract_analysis = df.groupby("Contract").agg(
    Total_Customers=("CustomerID", "count"),
    Churned_Customers=("Churn", lambda x: (x == "Yes").sum())
)

# Calculate churn percentage for each contract
contract_analysis["Churn_Rate"] = (
    contract_analysis["Churned_Customers"]
    / contract_analysis["Total_Customers"] * 100
)

print(contract_analysis.round(2))


# Create a bar chart
plt.figure(figsize=(8,5 ))

plt.bar(
    contract_analysis.index,
    contract_analysis["Churn_Rate"]
)

plt.title("Customer Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")

plt.tight_layout()

# Save chart as an image
plt.savefig("churn_by_contract.png")

plt.show()


# Average monthly charges by churn status
print("\n--- Monthly Charges Analysis ---")

charges_analysis = df.groupby("Churn")["MonthlyCharges"].mean()

print(charges_analysis.round(2))

# Create a bar chart
plt.figure(figsize=(7, 5))

plt.bar(
    charges_analysis.index,
    charges_analysis.values
)

plt.title("Average Monthly Charges: Churn vs Non-Churn")
plt.xlabel("Customer Churn Status")
plt.ylabel("Average Monthly Charges")

plt.tight_layout()
plt.savefig("monthly_charges_by_churn.png")
plt.show()

# Business Insights Report
print("\n========== BUSINESS INSIGHTS ==========")

total_customers = len(df)
churned = (df["Churn"] == "Yes").sum()
retained = (df["Churn"] == "No").sum()
churn_rate = (churned / total_customers) * 100

# Contract with the highest churn rate
highest_churn_contract = contract_analysis["Churn_Rate"].idxmax()
highest_churn_rate = contract_analysis["Churn_Rate"].max()

# Average monthly charges by churn status
avg_churned_charges = df.loc[
    df["Churn"] == "Yes", "MonthlyCharges"
].mean()

avg_retained_charges = df.loc[
    df["Churn"] == "No", "MonthlyCharges"
].mean()

print(f"Total Customers: {total_customers}")
print(f"Customers Churned: {churned}")
print(f"Customers Retained: {retained}")
print(f"Overall Churn Rate: {churn_rate:.2f}%")

print(
    f"Highest Churn Contract: {highest_churn_contract}"
)
print(f"Contract Churn Rate: {highest_churn_rate:.2f}%")

print(
    f"Average Charges (Churned): {avg_churned_charges:.2f}"
)
print(
    f"Average Charges (Retained): {avg_retained_charges:.2f}"
)

# KPI Summary Report
print("\n========== KPI SUMMARY ==========")

total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()

churn_rate = churned_customers / total_customers * 100
retention_rate = retained_customers / total_customers * 100

total_monthly_revenue = df["MonthlyCharges"].sum()
average_monthly_charge = df["MonthlyCharges"].mean()

print(f"Total Customers: {total_customers}")
print(f"Churned Customers: {churned_customers}")
print(f"Retained Customers: {retained_customers}")
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Retention Rate: {retention_rate:.2f}%")
print(f"Total Monthly Charges: {total_monthly_revenue:.2f}")
print(f"Average Monthly Charge: {average_monthly_charge:.2f}")

# Create a simple KPI dashboard
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: Customer Churn Distribution
churn_counts = df["Churn"].value_counts()

axes[0].bar(churn_counts.index, churn_counts.values)
axes[0].set_title("Customer Churn Distribution")
axes[0].set_xlabel("Churn Status")
axes[0].set_ylabel("Number of Customers")

# Chart 2: Average Monthly Charges
axes[1].bar(charges_analysis.index, charges_analysis.values)
axes[1].set_title("Average Monthly Charges")
axes[1].set_xlabel("Churn Status")
axes[1].set_ylabel("Average Charges")

fig.suptitle(
    f"Customer Churn Dashboard | Churn Rate: {churn_rate:.2f}%"
)

plt.tight_layout()
plt.savefig("customer_churn_dashboard.png", dpi=300)
plt.show()
# Final Report
report = f"""
CUSTOMER CHURN ANALYSIS REPORT
==============================

Total Customers: {len(df)}
Churned Customers: {(df["Churn"] == "Yes").sum()}
Retained Customers: {(df["Churn"] == "No").sum()}
Overall Churn Rate: {churn_rate:.2f}%

CONTRACT-WISE CHURN
-------------------
{contract_analysis.round(2).to_string()}

AVERAGE MONTHLY CHARGES
-----------------------
{charges_analysis.round(2).to_string()}

KEY FINDINGS
------------
1. Month-to-month contracts have the highest churn rate.
2. Two-year contracts have the lowest churn rate.
3. Average monthly charges are relatively close for churned
   and retained customers.

Note: This project uses synthetic data for practice.
"""

with open("final_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nFinal report saved as final_report.txt")