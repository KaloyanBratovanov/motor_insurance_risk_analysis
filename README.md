# Motor Insurance Risk Analysis

## Project Overview

This project explores how mathematics and Python can be used to analyze real motor insurance data.

Using a dataset of **105,555 insurance records**, the analysis investigates the relationships between vehicle characteristics and insurance premiums, the probability of insurance claims, and the distribution of claim costs.

The project was developed as part of the **Math Concepts for Developers** course at SoftUni.

## Research Questions

The analysis focuses on four main questions:

1. **How Do Vehicle Characteristics Affect Insurance Premiums?**
2. **How Does Engine Power Affect Insurance Premiums?**
3. **How Likely Is an Insurance Claim?**
4. **What Can We Learn from Insurance Claim Costs?**

## Methods

The project applies the following mathematical methods:

- **Linear Algebra:** Multiple linear regression to estimate insurance premiums.
- **Calculus:** Partial derivatives and definite integrals to analyze the predicted premium function.
- **Probability:** Claim frequency and conditional probability across driver age groups.
- **Statistics:** Mean, median, standard deviation, and Pearson correlation.

## Key Findings

- **18.61%** of insurance records had at least one claim.
- Increasing engine power by 10 units increases the predicted premium by approximately **€10.60**, with other vehicle characteristics held constant.
- The average annual claim cost per insurance record with positive claim costs was **€825.04**, while the median was **€289.44**.
- Engine power had the strongest positive correlation with insurance premiums among the three vehicle characteristics examined.

## Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib

## Dataset

The analysis uses the [Motor Insurance Dataset — Mendeley Data](https://doi.org/10.17632/5cxyb5fp4f.2).

## How to Run

1. Clone or download this repository.
2. Install the required Python libraries:
   ```bash
   pip install numpy pandas matplotlib notebook
   ```
3. Make sure the dataset is located at:
   `data/Motor vehicle insurance data.csv`
4. Open `motor_insurance_risk_analysis.ipynb` in Jupyter Notebook or VS Code.
5. Run the notebook cells in order.

## Conclusion

The analysis demonstrates how mathematical and statistical methods can help identify patterns in insurance premiums, claim probabilities, and claim costs. The results provide a foundation for understanding insurance risk using real data.
