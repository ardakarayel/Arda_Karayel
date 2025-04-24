# Arda_Karayel



Education Level and Happiness Index - Project Proposal

# Project Overview

This project aims to analyze the relationship between a country's education level and its happiness index to determine whether higher education levels contribute to greater happiness. Using data science techniques, we will investigate whether investment in education correlates with increased life satisfaction. By comparing education-related metrics (literacy rate, average years of schooling, tertiary education enrollment) with happiness scores, this study seeks to uncover patterns and key influencing factors.

# Motivation

Education is often linked to economic prosperity, but its connection to happiness is less explored. This study can provide insights into how learning contributes to life satisfaction. If a strong correlation is found, governments and policymakers may prioritize education as a key factor for holistic societal development. Additionally, this project provides an opportunity to apply data science skills in real-world analysis, improving statistical and analytical expertise.

# Objectives

Investigate the Relationship Between Education and Happiness

Explore whether countries with higher education levels report higher happiness scores.
Identify Key Contributing Factors

Compare the impact of education with other factors such as GDP per capita, social support, and life expectancy.
Utilize Data Science Techniques

Apply statistical methods and visualization techniques to identify correlations between education and happiness.

# Datasets

This project will use publicly available datasets from Kaggle:

World Happiness Report Dataset:https://www.kaggle.com/datasets/unsdsn/world-happiness
Contains global happiness scores, GDP per capita, social support, freedom index, and life expectancy.

World Bank Education Dataset: https://www.kaggle.com/datasets/theworldbank/education-statistics
Includes literacy rates, mean years of schooling, tertiary education enrollment, and government expenditure on education.

Key Variables in the Dataset

Education-Related Variables


- Tertiary Enrollment Rate → Percentage of people enrolled in higher education.
- Adult Literacy Rate → Percentage of adults who can read and write

Happiness-Related Variables

- Happiness Score → Well-being index on a scale of 0 to 10.
- GDP per Capita → Economic performance indicator.
- Freedom Index → Measures the perceived level of personal freedom.
- Life Expectancy -> Expected average lifespan in a country, reflecting overall health and well-being.
- Both datasets will be merged using the "Country" field to ensure accurate comparisons.

# Methodology

The study will follow a structured approach to collect, clean, and analyze data.

1. Data Collection & Cleaning
Merge education and happiness datasets using the "Country" field.
Handle missing values using imputation or removal of incomplete records.
Convert categorical variables into numerical formats for effective analysis.

2. Exploratory Data Analysis (EDA)
Histograms & Distribution Plots → Assess the spread of happiness scores and education levels.
Correlation Matrix (Heatmap) → Identify relationships between education, happiness, and economic factors.
Scatter Plots & Boxplots → Compare education levels across different happiness scores.

3. Hypothesis Testing
Null Hypothesis (H₀): No significant relationship exists between education level and happiness index.
Alternative Hypothesis (H₁): Higher education levels are significantly correlated with higher happiness scores.
Conduct statistical tests (Pearson correlation, regression analysis) to test the hypothesis.

4. Machine Learning (Optional)
Train a linear regression model to predict happiness scores based on education variables.
Compare different models (Decision Tree, Random Forest) to identify the best predictor.

5. Expected Outcomes
Identification of potential correlations between education and happiness levels.
Insights into whether tertiary education enrollment plays a significant role in happiness.
Visualization of global trends linking education with life satisfaction.


# Hypothesis and Predictions

This study aims to test the following hypotheses regarding the relationship between education level and happiness:

Null Hypothesis (H₀): There is no significant relationship between education level and happiness index. Higher education levels do not significantly impact happiness scores.
Alternative Hypothesis (H₁): Higher education levels are significantly correlated with higher happiness scores. Countries with higher tertiary enrollment rate and higher literacy rates tend to have higher happiness levels.

# Predictions

Based on previous research and logical reasoning, the following outcomes are expected:

Countries with higher literacy rates and higher tertiary enrollment rate will have higher happiness scores.
Tertiary education enrollment will be a strong predictor of happiness, but other factors such as GDP per capita and life expectancy may have stronger correlations.
Developed nations will show a stronger correlation between education and happiness, while in developing countries, economic factors may play a more dominant role.

# Findings 
-Education Variables
1. Tertiary Enrollment Datas
   
   The following histogram illustrates the distribution of tertiary enrollment rates across countries in 2017.
The data displays a right-skewed pattern, suggesting that lower enrollment percentages are more frequent.
This highlights the inequality in access to higher education, especially between developed and developing nations.



![tertiary enrollment histogram ](https://github.com/user-attachments/assets/093bcb35-fe55-4da8-b8da-bc60080830d1)


The boxplot displays the distribution of tertiary enrollment percentages across countries in 2017.
The median enrollment rate is around 50%, with a wide interquartile range, indicating high variability among countries.
A few outliers above 100% suggest that some countries report tertiary enrollment exceeding the traditional age group, possibly due to lifelong learning or returning students.
![tertiary box plot](https://github.com/user-attachments/assets/0874fbfa-53e2-4016-879f-af3d385c653f)


2.Adult Literacy Rates

 The following histogram shows the distribution of adult literacy rates across countries in 2017.
The distribution is left-skewed, indicating that higher literacy rates are more common, with many countries scoring above 70–80%.
This pattern reflects a global trend towards widespread basic education, although a few regions still face significant literacy challenges.

 ![literacy rate histogram](https://github.com/user-attachments/assets/eccdeb52-bd69-41c5-9fbc-ffb99d0635d1)


 The boxplot presents the distribution of adult literacy rates across countries in 2017.
The median literacy rate is around 75–80%, and the interquartile range is relatively narrow, indicating that most countries fall within a similar range.
A few outliers on the lower end (below 40%) highlight regions where literacy remains a major challenge, emphasizing global inequality in basic education access.

![literacy rate box plot](https://github.com/user-attachments/assets/a65bd8ff-7738-4022-bde5-5a56f882190a)

-Happiness Variables

1.Happiness Scores

The histogram illustrates the distribution of happiness scores across countries in 2017.
The shape appears approximately normal, with most countries scoring between 5 and 6.5 on the scale.
This suggests that global well-being levels tend to cluster around the middle, with fewer countries reporting very low or very high happiness.

![happiness score histogram ](https://github.com/user-attachments/assets/1ce2546e-9bd4-4b68-a6c2-fa6e3af1c6cb)


This boxplot displays the distribution of happiness scores across countries in 2017.
The median score is around 5.5, and the data is fairly symmetrical, with most values falling between 4.5 and 6.5.
The absence of extreme outliers indicates a relatively consistent global trend in well-being levels, without major deviations.



![happiness box plot](https://github.com/user-attachments/assets/27903a13-f522-479b-8eea-f3194087e0d3)


2. GDP per Capita, Life Expectancy and Freedom

   The following histograms illustrate the distributions of GDP per capita, perceived freedom, and life expectancy across countries in 2017.
All three variables display a right-skewed pattern, suggesting that lower values are more frequent, while higher values are observed in a smaller number of countries.
This highlights ongoing global disparities in economic resources, personal freedom, and health outcomes.

   ![happiness ve other varibles histogram ](https://github.com/user-attachments/assets/73dda712-8467-4737-b228-16e21d5e255b)


The scatter plots below illustrate the relationships between happiness score and three key indicators: GDP per capita, freedom, and life expectancy.
All three show a positive correlation, meaning that as GDP, freedom, or life expectancy increases, happiness scores also tend to rise.
Among the three, GDP per capita and life expectancy exhibit a stronger linear trend, suggesting that economic and health-related factors may have a more direct impact on national well-being.

![happiness ve other varibles scatter](https://github.com/user-attachments/assets/81f8bbc9-7896-4620-9a85-3ea1cca886ef) 

# Statistics

The descriptive statistics highlight a significant variance in tertiary education enrollment rates across countries, with values ranging from under 10% to over 120%. In contrast, adult literacy rates are more uniformly distributed, clustering around 80%. Happiness scores are concentrated around the midpoint (mean = 5.35), reflecting moderate global well-being levels.

- Tertiary Enrollment Rate (2017) %0-100

   Count              : 193
   
   Mean               : 43.26
   
   Median             : 42.36
   
   Mode               : 23.09
   
   Variance           : 781.66
   
   Standard Deviation : 27.96


- Adult Literacy Rate (2017) %0-100

   Count              : 266
   
   Mean               : 79.10
   
   Median             : 79.79
   
   Mode               : 66.34
   
   Variance           : 126.08
   
   Standard Deviation : 11.23

- Happiness Score (2017) 0-10

   Count              : 155
   
   Mean               : 5.35
   
   Median             : 5.28
   
   Mode               : 7.28
   
   Variance           : 1.28
   
   Standard Deviation : 1.13

 * p-value and Corelation Coefficients
    
   * Tertiary Enrollment vs Happiness (Pearson Correlation)
   
         Correlation Coefficient (r): 0.6404
        
         P-value                    : 3.7797e-14
         
   * Literacy Rate vs Happiness (Pearson Correlation)
   
         Correlation Coefficient (r): 0.1199
        
         P-value                    : 1.5808e-01
   
   * Tertiary Enrollment vs Happiness Score (Spearman Correlation)
   
         Correlation Coefficient (ρ): 0.6491
        
         P-value                    : 1.3098e-14
         
   * Literacy Rate vs Happiness Score (Spearman Correlation)
   
         Correlation Coefficient (ρ): 0.1164
        
         P-value                    : 1.7093e-01

The correlation between tertiary enrollment and happiness score is both strong and statistically significant, supported by:

Pearson r = 0.6404, p = 3.78e-14

Spearman ρ = 0.6491, p = 1.30e-14

These extremely low p-values (p < 0.001) confirm that the relationship is unlikely due to chance.

On the other hand, the relationship between adult literacy and happiness is:

Pearson r = 0.1199, p = 0.158

Spearman ρ = 0.1164, p = 0.170

Since both p-values are greater than 0.05, this indicates that literacy rate does not have a statistically significant correlation with happiness.

# Comparison and Correlation Analysis

- Tertiary Enrollment Rate vs Happiness Scores Comparison

  This section compares tertiary education enrollment rates with national happiness scores using both downloadable data and a grouped bar chart. The visualization reveals patterns across countries, showing how access to higher education may be linked to greater well-being.
  
  ![happiness score x tertiary enrollment histogram](https://github.com/user-attachments/assets/a7a88029-017c-4822-8db1-c683004b0220)

    ![download](https://github.com/user-attachments/assets/117e86bf-a981-430f-a399-c935d04fa8cd)


- Adult Literacy Rate vs Happiness Scores Comparison

   The bar charts below highlight the comparison between adult literacy rates and national happiness levels. Despite high literacy in most countries, happiness varies widely, supporting the statistical finding that literacy rate has little predictive power over happiness scores (r ≈ 0.12, p > 0.05).

![happiness score x literacy rate histogram](https://github.com/user-attachments/assets/897ce753-1ab2-4759-b970-1104fc4fc1a1)

![download ](https://github.com/user-attachments/assets/33adf692-b0b7-4d2e-96d3-1cdbd3db6f07)

  
 



- Correlation Between Happiness Score and Tertiary Enrollment Rate
  
 This scatter plot demonstrates the relationship between a country's tertiary education enrollment rate and its Happiness Score in 2017.

 A positive trend is clearly visible: countries with higher enrollment rates tend to report higher levels of happiness.

The distribution shows a moderate to strong upward correlation, though not perfectly linear.

Outliers exist (e.g., countries with high enrollment but average happiness), but the overall pattern supports the idea that access to higher education is associated with greater well-being.

 ![happines score x tertiary Enrollment scatter](https://github.com/user-attachments/assets/34493be6-64f6-440f-bd09-22f9057b7f55)
  
  The scatter plot shows a clear positive association between tertiary education enrollment and national happiness levels. The clustering of data points suggests that countries with broader access to higher education generally report higher well-being. This observation is backed by a statistically significant correlation (r = 0.64, p < 0.001).

- Correlation Between Happiness Score and Adult Literacy Rate
  
This scatter plot visualizes the relationship between a country's adult literacy rate and its Happiness Score in 2017.

While the distribution appears somewhat positive, the trend is much weaker and less consistent than in the tertiary enrollment plot.

Countries with high literacy (above 90%) show a wide spread of happiness scores — from below 5.0 to above 7.0 — suggesting that literacy alone does not strongly predict well-being.

The data points are more scattered, and the lack of a clear trend is confirmed statistically by a low correlation coefficient (r = 0.12) and a non-significant p-value (p = 0.158).

This implies that while literacy may be a foundational indicator of development, it is not a strong standalone driver of happiness at the national level.

 ![happiness score x literacy rate scatter](https://github.com/user-attachments/assets/beb6eff9-c7d0-48f4-9823-8b61aeb62436)

 
 Although the scatter plot shows a slightly upward trend between adult literacy rate and happiness, the correlation is weak and statistically insignificant (r = 0.12, p = 0.158). This suggests that literacy, while crucial for development, does not directly translate into higher national well-being.



Based on the correlation analysis conducted using Pearson and Spearman methods, we evaluated the relationship between education-related metrics and happiness scores to determine which hypothesis can be accepted.

# Hypothesis Testing: Education and Happiness

###  Hypothesis Recap:

- **H₀ (Null Hypothesis):** There is no significant relationship between education level and happiness.
- **H₁ (Alternative Hypothesis):** Higher education levels are significantly correlated with higher happiness scores.

---

###  Tertiary Enrollment:

- **Pearson r = 0.6404**, **p = 3.78e-14**
- **Spearman ρ = 0.6491**, **p = 1.30e-14**

 Since both p-values are **well below 0.05**, we reject the null hypothesis **H₀**.  
 There is a **strong and statistically significant** positive correlation between tertiary education and happiness.  
➡ **We accept the alternative hypothesis (H₁)** for tertiary enrollment.

---

###  Adult Literacy Rate:

- **Pearson r = 0.1199**, **p = 0.158**
- **Spearman ρ = 0.1164**, **p = 0.170**

 Both p-values are **greater than 0.05**, indicating no statistically significant relationship.  
 Thus, we **fail to reject the null hypothesis (H₀)** for literacy rate.

---

###  Final Decision:

- **Tertiary Enrollment**: H₀ rejected → education correlates with happiness   
- **Adult Literacy Rate**: H₀ not rejected → no significant relationship 

Overall, this supports the hypothesis that **higher access to advanced education** contributes meaningfully to national happiness levels.





