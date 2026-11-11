#####################################################################
## FINAL ASSIGNMENT
## Basic course for structural equation modeling
#####################################################################

# Libraries
import pandas as pd
import numpy as np
import pyreadstat
import statsmodels.formula.api as smf
from semopy import Model, calc_stats

# Data
df, meta = pyreadstat.read_sav("dataset.sav")
print(df.head())
print(df.columns.tolist())
print(df.shape)

####################################################################

## Part 1:

# Descriptive variables
descriptive_vars = [
    "miema",
    "matisum_1",
    "matisum_2",
    "mie1c",
    "mie2c",
    "mie3c",
    "mie1c_2",
    "mie2c_2",
    "mie3c_2"
]
data_desc = df[descriptive_vars]
descriptives = data_desc.describe().T
descriptives = descriptives.rename(columns={
    "count": "N",
    "mean": "Mean",
    "std": "SD",
    "min": "Min",
    "25%": "Q1",
    "50%": "Median",
    "75%": "Q3",
    "max": "Max"
})

# Missing Values
missing = data_desc.isna().sum()
missing_percentage = data_desc.isna().mean() * 100
missing_table = pd.DataFrame({
    "Missing N": missing,
    "Missing %": missing_percentage
})
missing_patterns = (
    data_desc.isna()
    .astype(int)
    .value_counts()
    .reset_index(name="Frequency")
)

# Correlation
correlations = data_desc.corr(method="pearson")

# Covariance
covariances = data_desc.cov()

# Covariance coverage
valid = data_desc.notna().astype(int)
coverage_counts = valid.T @ valid
covariance_coverage = coverage_counts / len(data_desc)

# Descriptive statistics results to Excel
descriptives_excel = descriptives.round(3)
missing_excel = missing_table.round(3)
correlations_excel = correlations.round(3)
covariances_excel = covariances.round(3)
covariance_coverage_excel = covariance_coverage.round(3)

excel_file = "descriptive_statistics.xlsx"

with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:

    descriptives_excel.to_excel(
        writer,
        sheet_name="Descriptive Stats"
    )
    missing_excel.to_excel(
        writer,
        sheet_name="Missing Values"
    )
    missing_patterns.to_excel(
        writer,
        sheet_name="Missing Patterns",
        index=False
    )
    correlations_excel.to_excel(
        writer,
        sheet_name="Correlations"
    )
    covariances_excel.to_excel(
        writer,
        sheet_name="Covariances"
    )
    covariance_coverage_excel.to_excel(
        writer,
        sheet_name="Covariance Coverage"
    )

####################################################################

## Part 2: (Regression Analysis)

# Regression analysis variables
regression_vars = [
    "matisum_2",
    "matisum_1",
    "miema"
]

# Listwise deletion
reg_data = df[regression_vars].dropna()

print("Sample size:", len(reg_data))

# Regression model
model_reg = smf.ols(
    formula="matisum_2 ~ matisum_1 + miema",
    data=reg_data
).fit()

# Regression results
results = pd.DataFrame({
    "B": model_reg.params,
    "SE": model_reg.bse,
    "t-value": model_reg.tvalues,
    "p-value": model_reg.pvalues,
    "CI Lower": model_reg.conf_int()[0],
    "CI Upper": model_reg.conf_int()[1]
})

# Model fit
fit = pd.DataFrame({
    "N": [int(model_reg.nobs)],
    "R-squared": [model_reg.rsquared],
    "Adjusted R-squared": [model_reg.rsquared_adj],
    "F-statistic": [model_reg.fvalue],
    "F p-value": [model_reg.f_pvalue]
})

# Regression analysis results to Excel
with pd.ExcelWriter(
    "regression_results.xlsx",
    engine="openpyxl"
) as writer:

    results.round(3).to_excel(writer, sheet_name="Regression")
    fit.round(3).to_excel(writer, sheet_name="Model Fit", index=False)


####################################################################

## Part 3: (Confirmatory Factor Analysis, CFA)

# CFA variables
cfa_vars = [
    "mie1c",
    "mie2c",
    "mie3c",
    "mie1c_2",
    "mie2c_2",
    "mie3c_2"
]
cfa_data = df[cfa_vars].copy()
print("Total sample size:", len(cfa_data))

# Listwise deletion
cfa_data = cfa_data.dropna().copy()
print("Complete observations:", len(cfa_data))

# CFA model
cfa_model = """
mat_interest1 =~ mie1c + mie2c + mie3c
mat_interest2 =~ mie1c_2 + mie2c_2 + mie3c_2

mat_interest1 ~~ mat_interest2

mie1c ~~ mie1c_2
"""

# CFA model using maximum likelihood (MLW)
model_cfa = Model(cfa_model)

result_cfa = model_cfa.fit(
    cfa_data,
    obj="MLW"
)

# Parameter estimates
cfa_results = model_cfa.inspect(std_est=True)

# Model Fit
fit_indices = calc_stats(model_cfa)

# CFA results to Excel
cfa_results_excel = cfa_results.round(3)
fit_indices_excel = fit_indices.T.round(3)

excel_file3 = "cfa_results.xlsx"

with pd.ExcelWriter(excel_file3, engine="openpyxl") as writer:
    cfa_results_excel.to_excel(
        writer,
        sheet_name="CFA",
        index=False
    )
    fit_indices_excel.to_excel(
        writer,
        sheet_name="Model Fit"
    )
