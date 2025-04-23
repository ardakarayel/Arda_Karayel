# Arda_Karayel



Education Level and Happiness Index - Project Proposal

#Project Overview

This project aims to analyze the relationship between a country's education level and its happiness index to determine whether higher education levels contribute to greater happiness. Using data science techniques, we will investigate whether investment in education correlates with increased life satisfaction. By comparing education-related metrics (literacy rate, average years of schooling, tertiary education enrollment) with happiness scores, this study seeks to uncover patterns and key influencing factors.

#Motivation

Education is often linked to economic prosperity, but its connection to happiness is less explored. This study can provide insights into how learning contributes to life satisfaction. If a strong correlation is found, governments and policymakers may prioritize education as a key factor for holistic societal development. Additionally, this project provides an opportunity to apply data science skills in real-world analysis, improving statistical and analytical expertise.

#Objectives

Investigate the Relationship Between Education and Happiness

Explore whether countries with higher education levels report higher happiness scores.
Identify Key Contributing Factors

Compare the impact of education with other factors such as GDP per capita, social support, and life expectancy.
Utilize Data Science Techniques

Apply statistical methods and visualization techniques to identify correlations between education and happiness.

#Datasets

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

#Methodology

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


#Hypothesis and Predictions

This study aims to test the following hypotheses regarding the relationship between education level and happiness:

Null Hypothesis (H₀): There is no significant relationship between education level and happiness index. Higher education levels do not significantly impact happiness scores.
Alternative Hypothesis (H₁): Higher education levels are significantly correlated with higher happiness scores. Countries with higher tertiary enrollment rate and higher literacy rates tend to have higher happiness levels.

#Predictions

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

