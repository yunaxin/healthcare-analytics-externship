## About This Project

This project was completed as part of the TruBridge Healthcare Data Analytics Externship through Extern.

The analysis explores the relationship between county-level socioeconomic factors and late-stage breast cancer outcomes among women under 50 in California using statistical analysis, data visualization, and regression modeling.

---

## Project Workflow

### Data Cleaning & Preparation

Raw datasets were cleaned and standardized using Python scripts located in:

scripts/

The cleaning process included:
- handling missing values
- formatting FIPS codes
- datatype conversion
- selecting relevant variables
- standardizing county-level datasets

---

### Dataset Merging

Cleaned datasets were merged using county FIPS codes to create a unified dataset for statistical analysis and modeling.

Final merged dataset:
`datasets/cleaned/final_merged_dataset.csv`

---

### Statistical Analysis

The main exploratory data analysis (EDA), statistical testing, regression modeling, and visualizations are included in:

`statistical_analysis.ipynb`

---

## Interactive Dashboard

An interactive dashboard generated with AI-assisted tools for exploring the analysis and visualizations can be viewed here:

- [View Dashboard](https://yunaxin.github.io/healthcare-analytics-externship/dashboard/index.html)

---

## Research Report & Presentation

Project report can be found here:

- `analysis_report.pdf`

---

## Tools & Skills Used

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- Statistical Analysis
- Exploratory Data Analysis (EDA)
- Linear Regression
- Hypothesis Testing
- Data Cleaning & Preprocessing
- Healthcare Analytics
- Data Visualization

