# DSA 210 PROJECT Arda_Karayel


Education and Environmental Factors in Relation to National Happiness – Project Proposal

# Project Overview

This project aims to analyze the relationship between a country’s education level, environmental quality, and its happiness index. The objective is to determine whether factors such as higher education and improved environmental conditions are associated with greater national well-being.

Using data science techniques, the study explores how tertiary education enrollment, air pollution, forest area, coastline-to-area ratio, and arable land percentage relate to happiness scores across countries.

By comparing these indicators with annual happiness data, the project seeks to uncover consistent patterns and key drivers of life satisfaction, providing insights into how educational and environmental investments may contribute to societal happiness.

# Motivation

Investigate the relationship between education, environmental quality, and happiness.

Explore whether countries with higher tertiary education enrollment, better environmental indicators (forest area, air quality), and geographical advantages (coastline ratio, arable land) report higher happiness scores.

Apply statistical and machine learning methods to identify key patterns and correlations among these factors and overall well-being.


# Objectives

Investigate the Relationship Between Education, Environment, and Happiness

Explore whether countries with higher education levels and better environmental conditions report higher happiness scores.

Identify Key Contributing Factors

Compare the influence of education (tertiary enrollment) and environmental indicators (forest area, air pollution, coastline ratio, arable land) on happiness.

Utilize Data Science Techniques

Apply statistical analysis and machine learning methods to uncover patterns and correlations among these variables and happiness scores.

# Datasets

This project will use publicly available datasets from Kaggle and World Bank Group:

World Happiness Report Dataset:https://www.kaggle.com/datasets/unsdsn/world-happiness
Contains global happiness scores, GDP per capita, social support, freedom index, and life expectancy.

World Bank Education Dataset: https://data.worldbank.org/indicator/SE.TER.ENRR
Includes adult literacy rates and tertiary education enrollment rates for countries.

World Bank Environmental Dataset: https://data.worldbank.org/indicator/AG.LND.FRST.ZS
Includes forest area data, representing the percentage of land area covered by forests for each country.

World Bank Environmental Dataset: https://data.worldbank.org/indicator/EN.ATM.PM25.MC.M3
Includes air pollution data, representing the oercentage of air pollution of countires.

World Bank Environmental Dataset: https://data.worldbank.org/indicator/AG.LND.ARBL.ZS 
Provides the percentage of land that is arable and suitable for agriculture.

Country Coastline Dataset: https://github.com/LSYS/country-coastline-distance
Provides the coastline-to-area ratio for each country, derived from CIA World Factbook and World Resources Institute data.
Used as a geographic feature to evaluate the impact of natural access and location on happiness levels.

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

Environmental Variable

- Forest Area (% of Land Area) → Proportion of land covered by forest, used as an indicator of environmental quality.

- Air Pollution → Represents the average level of harmful fine particles (PM2.5) in the air; higher values indicate worse air quality.

- Coastline Ratio → Ratio of a country's coastline length to its land area; considered as a proxy for access to natural resources, climate, and recreational benefits.

- Arable Land (% of Land Area) → Proportion of land suitable for agriculture; used as an indicator of sustainable land use and food security.

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

4. Machine Learning 
Train a linear regression model to predict happiness scores based on education variables.
Compare different models (Decision Tree, Random Forest) to identify the best predictor.

5. Expected Outcomes
Identification of potential correlations between education and happiness levels.
Insights into whether tertiary education enrollment plays a significant role in happiness.
Visualization of global trends linking education with life satisfaction.


# Hypothesis 

Main hypothesis

H₀: There is no statistically significant relationship between education level, environmental quality, and national happiness scores.

H₁: Education and environmental quality are significantly associated with national happiness scores.


# Predictions

It is expected that countries with higher education levels and better environmental conditions—specifically greater forest coverage, lower air pollution (PM2.5), higher coastline-to-area ratios, and more arable land—will tend to have higher happiness scores.

Among all variables, tertiary education is anticipated to show the strongest positive correlation with happiness. Air pollution is expected to have a moderate to strong negative impact, while forest area and arable land may show mild positive effects. Coastline ratio is also expected to have a small positive influence, reflecting geographic and lifestyle advantages.

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

-Forest Area (% of land)

 The histogram shows the distribution of forest area (% of land) across all countries in 2017. Most countries have relatively low forest coverage, with a noticeable concentration in the 0–20% range. However, a smaller number of countries exhibit very high forest density, reflected in the right-skewed tail. The KDE curve suggests a multi-modal distribution, indicating regional or environmental clustering.

![Forest histogram](https://github.com/user-attachments/assets/c22e49aa-1a18-4d48-a8ed-016f0f6f7dbc) 


The box plot illustrates the spread of forest area percentages across all countries in 2017. The median falls near the center of the interquartile range, suggesting a fairly balanced distribution. The length of the box indicates moderate variability, while the whiskers show a wide range of values. A few outliers may exist beyond the whiskers, representing countries with exceptionally high or low forest coverage.

![forest box plot](https://github.com/user-attachments/assets/d291ab98-6fae-437f-ac82-076eaa33b452)

-Air Pollution

The histogram shows that most countries have relatively low to moderate air pollution levels, while a smaller group experiences much higher exposure.

The distribution is clearly right-skewed, indicating that only a few countries suffer from very high pollution, while the majority remain in a safer range.

![histogram air pollution](https://github.com/user-attachments/assets/4cdf3a5d-db82-43d4-a779-de8564b4dbcf)

This boxplot displays the distribution of PM2.5 air pollution levels across three groups: Low, Medium, and High.

As expected, each group shows increasing concentration ranges, with the High pollution group having the widest and most elevated values. This visual confirms a clear separation between pollution levels among countries in 2017.

![box plot air plootuion](https://github.com/user-attachments/assets/a7ce5b85-8b4d-435a-91e0-28ab6aa95fa6)

This map illustrates global air pollution levels in 2017, measured by PM2.5 concentration.

Darker red regions represent countries with the highest pollution levels, such as India, Pakistan, and several North African and Middle Eastern countries.

Lighter areas (especially in Europe, Oceania, and parts of South America) indicate cleaner air and lower PM2.5 exposure.

The data clearly highlights significant regional differences in air quality across the globe.

![air pollution heatmap ](https://github.com/user-attachments/assets/3a3077f9-bfe8-4fdd-aaba-dad999105eb7)

- Arable Land

  The distribution of arable land percentage in 2017 is heavily right-skewed, with the majority of countries falling below 15%. Only a few countries possess significantly higher percentages, exceeding 40%. This highlights the unequal global distribution of arable land and suggests that transformation may be necessary before using this variable in machine learning models.
  
![histogram](https://github.com/user-attachments/assets/fcbad3ac-c244-404a-9aa2-4c9224548300)

The boxplot shows that most countries had arable land percentages between approximately 5% and 20% in 2017, with a median around 10%. The presence of multiple outliers beyond 40% indicates that a small number of countries possess significantly higher proportions of arable land. 

![box plot](https://github.com/user-attachments/assets/5ce1a3c6-0baa-450d-a717-2eaf7a0de668)

- Coastline Ratio
 
  The distribution of coastline-to-area ratios in 2017 is highly skewed to the right, with the vast majority of countries having a ratio below 10%. This indicates that most countries have relatively little coastline compared to their land area. However, a small number of countries—mostly small island nations—have extremely high ratios, pushing the distribution into a long tail. This imbalance suggests that the raw variable may require transformation before being used in analytical or machine learning contexts.
  
![histogram](https://github.com/user-attachments/assets/a8ad3959-9348-4d82-bd39-1ad18796eeb4)

The pie chart shows that nearly half of all countries (46.7%) have a coastline-to-area ratio below 10%, indicating that they are either landlocked or have very limited coastal access. As the ratio increases, the number of countries in each category declines significantly. Only 5.7% of countries fall into the highest range (75–100%), highlighting that extensive coastlines relative to land area are rare and often characteristic of small island nations. This visual emphasizes the highly uneven global distribution of coastal access.

![pie char](https://github.com/user-attachments/assets/16f558ca-f88a-4b6a-aa18-e5c331888db6)


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

- Forest Area Ratio (2017) % 0-100
 
   Count              : 222
   
   Mean               : 32.59
   
   Median             : 31.18
   
   Mode               : 0.0
   
   Variance           : 559.32
   
   Standard Deviation : 23.65
  
- Air pollution Ratio (2017) % 0-100
  
  Count : 248
  
  Mean : 27.06
  
  Median : 21.86
  
  Mode : 40.78
  
  Variance : 300.03
  
  Standard Deviation : 17.32

 - Arable Land Ratio % 0-100
    
  Count : 255
 
  Mean : 13.68
 
  Median : 10.08
 
  Mode : 2.86
 
  Variance : 167.22
 
  Standard Deviation : 12.93

- Coastline to Area Ratio  % 0–100
  
   Count : 235
  
   Mean : 26.74
  
   Median : 0.82
  
   Mode : 0.00
  
   Variance : 8235.38

   Standard Deviation : 90.75

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

   * Forest Area vs Happiness Score (Pearson Correlation)

         Correlation Coefficient (r): 0.0957

         P-value                    : 2.7854e-01

   * Forest Area vs Happiness Score (Spearman Correlation)

         Correlation Coefficient (ρ): 0.1037
    
         P-value                   : 2.4025e-01
     
   * Air Pollution vs Happiness Score (Pearson Correlation)

         Correlation Coefficient (ρ): -0.4664
 
         P-value                   : 0.0
  
   * Air Pollution vs Happiness Score (Spearman Correlation)

         Correlation Coefficient (ρ): -0.5832
 
         P-value                   : 0.0
     
   * Arable Land vs Happiness Score (Pearson Correlation)
 
         Correlation Coefficient (r): -0.1380
     
         P-value                    : 0.1117

   * Arable Land vs Happiness Score (Spearman Correlation)
     
         Correlation Coefficient (ρ): -0.1371
     
         P-value                    : 0.1141  

   The study examined how several factors—including education, land use, and environmental conditions—relate to national happiness scores using both Pearson and Spearman correlation methods.

Tertiary enrollment rate exhibits a strong and statistically significant positive correlation with happiness (r ≈ 0.64, p < 0.001), supporting the idea that access to higher education is a key driver of national well-being.

In contrast, adult literacy rate shows only a weak and statistically insignificant correlation (r ≈ 0.12, p > 0.15), suggesting that while basic education is widespread, it may not alone predict higher life satisfaction.

Forest area percentage shows a very weak and statistically insignificant relationship with happiness (r ≈ 0.10, p > 0.2), indicating that forest coverage, though environmentally valuable, may not directly impact subjective well-being on a national scale.

Air pollution ratio stands out with a moderate and statistically significant negative correlation with happiness (r = -0.47 to -0.58, p ≈ 0.000), highlighting the importance of clean air as a consistent and measurable factor affecting people's quality of life.

Arable land ratio shows a weak and negative but statistically insignificant correlation (r ≈ -0.14, p > 0.1), implying that agricultural capacity may be more relevant for economic or food security concerns rather than immediate happiness.

Interestingly, the coastline-to-area ratio, after transformation, demonstrates a moderate and statistically significant positive correlation with happiness (r ≈ 0.36–0.42, p < 0.001), suggesting that proximity to coastlines might contribute to well-being through channels like recreation, climate, and economic opportunities.

Interpretation:
Overall, the results suggest that access to higher education, clean air, and coastal environments are more influential on happiness levels than broader geographic or structural indicators such as land use or literacy. These findings may guide policymakers toward interventions that prioritize environmental quality and educational access as key components of national well-being.

# Comparison and Correlation Analysis

- Tertiary Enrollment Rate vs Happiness Scores Comparison

  This section compares tertiary education enrollment rates with national happiness scores using both downloadable data and a grouped bar chart. The visualization reveals patterns across countries, showing how access to higher education may be linked to greater well-being.
  
  ![happiness score x tertiary enrollment histogram](https://github.com/user-attachments/assets/a7a88029-017c-4822-8db1-c683004b0220)

    ![download](https://github.com/user-attachments/assets/117e86bf-a981-430f-a399-c935d04fa8cd)


- Adult Literacy Rate vs Happiness Scores Comparison

   The bar charts below highlight the comparison between adult literacy rates and national happiness levels. Despite high literacy in most countries, happiness varies widely, supporting the statistical finding that literacy rate has little predictive power over happiness scores (r ≈ 0.12, p > 0.05).

![happiness score x literacy rate histogram](https://github.com/user-attachments/assets/897ce753-1ab2-4759-b970-1104fc4fc1a1)

![download ](https://github.com/user-attachments/assets/33adf692-b0b7-4d2e-96d3-1cdbd3db6f07)


- Forest Area Ratio vs Happiness Score Comparison

  This bar chart shows the average forest area (% of land) across countries grouped by their happiness score ranges. Countries with higher happiness scores tend to have slightly more forest coverage on average, suggesting a potential link between environmental quality and well-being.

 ![forest vs happiness bar chart](https://github.com/user-attachments/assets/3d5c41c5-2707-4219-bf1e-4ebd76b5b8a1)
 

 - Coastline Ratio vs Happiness Score Comparison 
 
 The bar chart shows that average happiness scores tend to increase with higher coastline-to-area ratios. Countries with minimal coastline (0–1%) have the lowest average happiness, while those in the 25–100% range show the highest scores. This suggests a positive association between coastal access and national well-being.
![coast vs happy bar chart](https://github.com/user-attachments/assets/1a1f923b-85e4-49ca-9ba4-ca96ecf28246)

- Arable Land Ratio vs Happiness Score Comparison
  
  The bar chart shows no clear trend between arable land percentage and average happiness scores.
All three groups (low, medium, high) have similar values, indicating that arable land is not strongly linked to well-being.
This aligns with the correlation results, where both Pearson and Spearman coefficients were weak and p-values above 0.1, confirming the relationship is statistically insignificant.

  ![happy x arable bar chart](https://github.com/user-attachments/assets/b5f77c78-ec1b-4ef4-bd2a-938c8bc8872d)


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



 - Correlation Between Happiness Score and Forest Area Ratio

 The scatter plot displays the relationship between forest area (% of land) and happiness score across countries in 2017. While the data points are widely scattered, there is a slight upward trend, indicating a potential weak positive correlation between forest coverage and happiness. However, the variability suggests that forest area alone is not a strong predictor of national happiness.

![Forest  x happiness scatter plot](https://github.com/user-attachments/assets/a1895cef-7d00-4d05-997d-8d27b3c07b17)

- Correlation Between Happiness Score and Air Pollution Ratio

The scatter plot displays the relationship between air pollution levels (PM2.5) and happiness scores across countries in 2017. The data points suggest a downward trend, indicating a moderate negative correlation between air pollution and happiness. Countries with higher PM2.5 levels generally report lower happiness scores. However, the dispersion of the points shows that air pollution alone may not fully explain variations in happiness across nations.


![air pollutions vs happiness scatter plot](https://github.com/user-attachments/assets/4fdb7979-7663-480b-92b0-46311676dd73)

- Correlation Between Happiness Score and Arable Land Ratio
  
The scatter plot shows no clear trend between arable land (log + scaled) and happiness score. The data points are widely dispersed, and there is no visible upward or downward pattern. This suggests that the percentage of arable land in a country is not strongly associated with national happiness levels.

![scatter](https://github.com/user-attachments/assets/441e10a2-e90c-4e97-984a-354c9155f9b3)

-  Correlation Between Happiness Score and Coastline Ratio
  
The scatter plot suggests a positive relationship between coastline ratio (log + scaled) and happiness score. While most countries cluster around lower coastline values, those with higher coastline-to-area ratios generally tend to have higher happiness scores. This pattern supports the idea that greater coastal access may be associated with improved well-being, possibly due to economic, environmental, or lifestyle factors.

  ![SCATTER](https://github.com/user-attachments/assets/7052e579-1ad0-464d-84d4-e654f084ce42)


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
 **We accept the alternative hypothesis (H₁)** for tertiary enrollment.

---

###  Adult Literacy Rate:

- **Pearson r = 0.1199**, **p = 0.158**
- **Spearman ρ = 0.1164**, **p = 0.170**

 Both p-values are **greater than 0.05**, indicating no statistically significant relationship.  
 Thus, we **fail to reject the null hypothesis (H₀)** for literacy rate.

---
# Hypothesis Testing: Forest Area and Happiness

### Hypothesis Recap:
 - **H₀ (Null Hypothesis):** There is no significant relationship between forest area and happiness.
 - **H₁ (Alternative Hypothesis):** Forest area is significantly correlated with happiness scores.

Forest Area:
- **Pearson r = 0.0957**,**p = 0.2785**
- **Spearman ρ = 0.1037**,**p = 0.2403**

Both p-values are greater than 0.05, indicating no statistically significant relationship.
Thus, we fail to reject the null hypothesis (H₀) for forest area.

 We do not accept the alternative hypothesis (H₁) for forest area.
---
# Hypothesis Testing: Air Pollution and Happiness

### Hypothesis Recap:
- **H₀ (Null Hypothesis):** There is no significant relationship between air pollution (PM2.5) and happiness.
- **H₁ (Alternative Hypothesis):** Air pollution is significantly correlated with happiness scores.

Air Pollution:

- **Pearson r = -0.4664, p = 0.0000**
- **Spearman ρ = -0.5832, p = 0.0000**

Both p-values are well below 0.05, indicating a statistically significant relationship between air pollution and happiness scores.
Thus, we reject the null hypothesis (H₀) and conclude that there is a significant negative association.

 We accept the alternative hypothesis (H₁) for air pollution.
---

# Hypothesis Testing: Arable Land and Happiness

### Hypothesis Recap:

- **H₀ (Null Hypothesis):** There is no significant relationship between arable land percentage and happiness.

- **H₁ (Alternative Hypothesis):** Arable land is significantly correlated with happiness scores.

 Arable land:
 
- **Pearson r = -0.1380, p = 0.1117**
- **Spearman ρ = -0.1371, p = 0.1141**

Both p-values are greater than 0.05, indicating that the relationship is not statistically significant.
We fail to reject the null hypothesis.
There is no sufficient evidence to support a significant correlation between arable land and happiness.

---

# Hypothesis Testing: Coastline Ratio and Happiness
### Hypothesis Recap:

- **H₀ (Null Hypothesis):** There is no significant relationship between coastline ratio and happiness.

- **H₁ (Alternative Hypothesis):** Coastline ratio is significantly correlated with happiness scores.

Coastline:
 
- **Pearson r = 0.3608, p = 0.00001**
- **Spearman ρ = 0.4206, p = 0.00000**

Both p-values are well below 0.05, indicating a statistically significant positive relationship.
We reject the null hypothesis.
There is strong evidence that greater coastline access is positively associated with happiness.

###  Final Decision:

- **Tertiary Enrollment**: H₀ rejected → education correlates with happiness   
- **Adult Literacy Rate**: H₀ not rejected → no significant relationship
- **Forest Area**: H₀ not rejected → no significant relationship
- **Air Pollution**: H₀ rejected → higher air pollution correlates with lower happiness
- **Arable Land**: H₀ not rejected → no significant relationship
- **Coastline Ratio**: H₀ rejected → greater coastal access correlates with higher happiness

Overall, these results support the hypothesis that higher access to advanced education, clean air, and coastal environments are associated with greater national happiness. In contrast, basic literacy, forest coverage, and agricultural land appear to have limited direct influence on happiness scores at the global level.


# Machine Learning Tecniques

Objective:
The goal of this analysis was to predict Happiness Scores based on multiple country-level indicators:

Tertiary Enrollment

Air Pollution

Forest Land Ratio

Coastline-to-Area Ratio

Arable Land Percentage

Results Overview:

Linear Regression:

MSE: 1.18

R²: 0.03

→ The model struggles to capture the relationship; results are barely better than a constant average prediction.

Decision Tree Regression:

MSE: 0.34

R²: 0.72

→ Captures non-linear patterns well. Performance is strong, with predictions closely aligned with actual scores.

Random Forest Regression:

MSE: 0.35

R²: 0.71

→ Similar to Decision Tree. Robust and performs well, though may be slightly overfitting flat regions due to discrete splits.

Interpretation:
Among the models tested, Decision Tree and Random Forest perform significantly better than Linear Regression. This suggests that the relationship between country indicators and happiness is non-linear and complex, benefiting from tree-based models that handle interactions and non-linear boundaries effectively.

![regression analysis](https://github.com/user-attachments/assets/e4da65c1-a4bb-4e67-bb5c-cad4b9a9d6c2)

- Bar Chart
  Average Actual and Predicted Happiness Score by Year

 Both actual and predicted values show consistent trends across years, indicating the model’s ability to capture general patterns.
Small differences between actual and predicted scores suggest room for slight improvement in capturing year-specific factors.

![bar chart](https://github.com/user-attachments/assets/ad69f9e4-32da-4ccf-b3a4-8e1512678237)


- Confusion Matrix For Binned Happiness Score

 Happiness scores were divided into five categories to evaluate how accurately the model predicts each class.
The matrix shows strong alignment along the diagonal, especially in the Neutral and Happy categories, indicating high classification accuracy.
Most misclassifications occur between neighboring classes like Unhappy and Neutral, which is expected due to score proximity.
This suggests the model captures overall patterns well but could be refined for clearer separation between close score ranges.

![confusion matrix](https://github.com/user-attachments/assets/1abee017-9c6e-4286-aa46-62e68ae2e178)

Very Unhappy: 0–4
Unhappy: 4–5
Neutral: 5–6
Happy: 6–7
Very Happy: 7–10

# Limitations 

This analysis may contain mild bias due to several factors:

Data availability: Not all countries had complete datasets for all variables, which led to a reduced sample size in some comparisons.

Limited variable selection: The analysis focused on a specific set of factors (education and environmental), while excluding others such as healthcare, governance, income inequality, or cultural differences, which may also significantly influence happiness.

Interpretation bias: The subjective nature of happiness, and the fact that it is based on self-reported surveys, introduces cultural or regional interpretation differences.

Model limitations: While tree-based models performed well, they can be harder to interpret and may overfit certain patterns in relatively small datasets.

The analysis may contain mild bias due to missing data in certain countries and the limited selection of variables. However, the overall results are statistically significant and consistent with the information provided by the dataset.

# Conclusion 

 This study explored the relationship between education levels, environmental indicators, and national happiness scores across a broad set of countries. The findings suggest that tertiary education enrollment, clean air (low PM2.5 levels), and geographic features such as coastline ratio are significantly associated with higher happiness levels.

In contrast, variables like adult literacy, forest area, and arable land showed weak or statistically insignificant correlations, indicating that not all development indicators directly impact subjective well-being.

Among the machine learning models tested, tree-based methods like Decision Tree and Random Forest outperformed linear regression, capturing non-linear patterns between variables and happiness. These results underline the complexity of happiness as a multi-dimensional construct and suggest that access to higher education and environmental quality are stronger predictors of national well-being than basic education or land use factors.
