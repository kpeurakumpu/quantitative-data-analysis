# The Relationship Between Children's Mathematics Interest and Mathematics Skills

**Quantitative Data Analysis | Python | Mplus | Statistical Modelling**

## 1. Project Overview

This project examines the relationship between children's interest in mathematics and their mathematical skills across two measurement occasions: autumn and spring.

The study applies quantitative statistical methods to investigate whether mathematics interest is associated with subsequent mathematics skills and to evaluate the measurement structure of mathematics interest.

The analysis was conducted primarily using Python, with additional Confirmatory Factor Analysis (CFA) performed in Mplus.

## 2. Research Questions

1. Does children's interest in mathematics in autumn predict their mathematics skills in spring, after controlling for their mathematics skills in autumn?
2. Do three observed indicators of mathematics interest measure a latent mathematics-interest construct in autumn and spring?

## 3. Methodology

### Descriptive Statistics

- Summary statistics: mean, median, standard deviation, quartiles and range.
- Missing data analysis.
- Pearson correlation matrix.
- Covariance matrix.
- Covariance coverage analysis.

### Regression Analysis

Multiple Linear Regression using Ordinary Least Squares (OLS).

The model examines the association between autumn mathematics interest and spring mathematics skills, controlling for autumn mathematics skills.

### Confirmatory Factor Analysis (CFA)

A two-factor measurement model was estimated to examine mathematics interest in autumn and spring.

- Two latent mathematics interest factors.
- Three observed indicators per measurement occasion.
- Model fit evaluation.
- Standardized factor loadings.
- Comparison of Python (`semopy`) and Mplus estimation results.

## 4. Key Findings

### Descriptive Statistics

- Original dataset: 167 participants.
- Nine variables included in the analysis.
- Valid observations (159-165) varied across variables due to missing data.
- Mathematics interest indicators generally showed relatively high scores.

### Regression Results

The regression model was statistically significant:

- R² = 0.539
- F = 89.86
- p < 0.001

Autumn mathematics skills were a significant positive predictor of spring mathematics skills (B = 0.700, p < 0.001).

Autumn mathematics interest had a positive but statistically insignificant coefficient (B = 0.595, p = 0.052).

### CFA Results

The two-factor CFA model produced the following fit indices:

| Fit index | Python (semopy) | Mplus |
|---|---:|---:|
| CFI | 0.962 | 0.958 |
| TLI | 0.919 | 0.911 |
| RMSEA | 0.121 | 0.091 |
| SRMR | Not reported | 0.050 |

The Mplus model was estimated using MLR, with FIML handling missing observations. The Python analysis used listwise deletion.

All six observed indicators had positive and statistically significant factor loadings. The standardized correlation between the autumn and spring latent factors was 0.417 (p < 0.001).

The overall model fit was mixed and the results should be interpreted with caution.

## 5. Tools and Technologies

- **Python:** Data processing and statistical analysis.
- **pandas:** Data manipulation and descriptive statistics.
- **statsmodels:** Multiple linear regression.
- **semopy:** Structural equation modelling and CFA.
- **Mplus:** Confirmatory Factor Analysis.
- **Excel:** Statistical results and reporting.

## 6. Repository Structure

```text
quantitative-data-analysis/
│
├── README.md
│
├── report/
│   └── research_report.pdf
│
├── python/
│   ├── main.py
│   └── requirements.txt
│
├── mplus/
│   ├── cfa_model.inp
│   ├── cfa_model.out
│   └── README.md
│
├── results/
│   ├── descriptive_statistics.xlsx
│   ├── regression_results.xlsx
│   └── cfa_results.xlsx
│
├── figures/
│   ├── correlation_matrix.png
│   ├── regression_coefficients.png
│   └── cfa_model.png
│
└── data/
    └── README.md
```

## 7. Data and Reproducibility

The original dataset is not included in this repository pending confirmation of data-sharing permissions.

Python scripts, model specifications and selected analytical outputs are intended to document the research workflow. Reproduction of the analysis requires access to the underlying dataset and the relevant software packages.

## 8. Research Conclusion

The findings suggest that children's earlier mathematics skills were a stronger predictor of their later mathematics skills than their earlier mathematics interest, after controlling for initial skills.

The CFA results provided support for modelling mathematics interest as a latent construct at both measurement occasions, although some model fit indices indicated potential limitations.

## 9. Author

Quantitative Research Project  
Basic Course for Structural Equation Modeling
