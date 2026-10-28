# Customer Churn Analysis

## Project Overview
This project analyzes customer churn patterns using Python, Pandas, and Matplotlib. The objective is to understand customer retention, compare churn across contract types, and examine monthly charges.

## Dataset
- **Customer records:** 500
- **Columns:** 18
- **Data type:** Synthetic customer data created for practice
- **Target column:** `Churn`

## Tools Used
- Python
- Pandas
- Matplotlib
- VS Code

## Data Quality Checks
- Missing values: 0
- Duplicate rows: 0
- Customer records loaded successfully: 500

## Key Performance Indicators
- **Total customers:** 500
- **Churned customers:** 169
- **Retained customers:** 331
- **Overall churn rate:** 33.80%
- **Retention rate:** 66.20%
- **Average monthly charge:** 67.67 dataset currency units

## Key Business Findings

### 1. Overall Churn
169 out of 500 customers churned, resulting in a churn rate of 33.80% in this synthetic dataset.

### 2. Churn by Contract Type
- Month-to-month: 41.84%
- One year: 28.24%
- Two year: 12.00%

Month-to-month customers had the highest observed churn rate. The business could investigate retention offers or longer-term contract options.

### 3. Monthly Charges
- Average charges for churned customers: 68.29
- Average charges for retained customers: 67.36

The averages are relatively close. Monthly charges alone do not explain the observed churn pattern.

## Visualizations
- `churn_by_contract.png` — churn rate by contract type
- `monthly_charges_by_churn.png` — average monthly charges by churn status
- `customer_churn_dashboard.png` — summary dashboard

## Project Files
- `customers.csv` — synthetic customer dataset
- `main.py` — analysis and visualization code
- `README.md` — project documentation
- PNG files — generated charts

## Limitations
This is a learning project based on synthetic data, not real customer records. The results demonstrate analysis techniques and should not be treated as findings about an actual company.

## Future Improvements
- Build an interactive Power BI dashboard
- Perform deeper churn analysis by tenure, internet service, and payment method
- Explore SQL queries for customer retention analysis
