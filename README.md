# Tuberculosis Treatment Success Rate 

The aim of this analysis is to investigate the trends and disparities in tuberculosis (TB) treatment success rates across various WHO regions from 1995 to 2020. By utilizing the provided dataset, the objective is to identify patterns, assess the effectiveness of interventions, and understand the factors influencing TB treatment outcomes. Specifically, the study aims to explore variations in treatment success rates among different types of TB cases and geographical regions. Through this analysis, the goal is to gain valuable insights that can inform evidence-based policies and interventions to enhance TB treatment outcomes worldwide.

# Data Set

## Overview 

This dataset contains information about tuberculosis (TB) treatment success rates across different regions and years. It includes data on new TB cases, previously treated TB cases, HIV-positive TB cases, multidrug-resistant TB (MDR-TB) cases, and extensively drug-resistant TB (XDR-TB) cases. The data is organized by the World Health Organization (WHO) regions: Global, Africa, Americas, South-East Asia, Europe, Eastern Mediterranean, and Western Pacific.

## Features Explination 

Features :

1. WHO Region (DataType : Object) : The region to which the data belongs (e.g., Global, Africa, Americas, etc.).
2. Year (DataType : INT64) : The year in which the data was recorded.
3. Treatment Success Rate for New TB Cases  (DataType : INT64) : successful treatment outcomes for new TB cases.
4. Treatment Success Rate for Previously Treated TB Cases  (DataType : INT64) : successful treatment outcomes for previously treated TB cases.
5. Treatment Success Rate for HIV-Positive TB Cases (DataType : FLOAT64) : successful treatment outcomes for TB cases in patients who are HIV-positive.
6. Treatment Success Rate for Patients Treated for MDR-TB (%) (DataType : FLOAT64) : Percentage of successful treatment outcomes for multidrug-resistant TB (MDR-TB) cases.
7. Treatment Success Rate for XDR-TB Cases (DataType : FLOAT64) :successful treatment outcomes for extensively drug-resistant TB (XDR-TB) cases.


# Setup

```python
# Install the requirements.txt packages.
$ pip3 install -r requirements.txt
```
# Usage

Terms:

1. input_file_path: Absolute File Path of the input csv file.
2. output_file_path: Directory for storring the plots.


```python
>>> python3 run.py input_file_path output_file_path
```

# Visualizing Data

## Plot 1
The provided count plot illustrates the distribution of the "WHO region" feature across seven distinct classes: Global, Africa, America, South-East Asia, Europe, Eastern Mediterranean, and Western Pacific. Each class is evenly distributed, indicating an equal representation within the dataset. The x-axis represents the different WHO regions, while the y-axis indicates the count of occurrences for each specific region. This visualization provides a clear overview of the balanced distribution of data points among the WHO regions, highlighting the equal representation of each region within the dataset.

![WHORegion Count Plot](media/WHORegion_countplot.png)

## Plot 2

A correlation heatmap is a graphical representation of the correlation matrix, showing how strongly different variables are related to one another. This visualization technique is particularly useful in statistics, data analysis, and machine learning to identify patterns, trends, and relationships within datasets.

Here's a detailed explanation of correlation heatmap:

### Understanding Correlation:

Correlation measures the strength and direction of a linear relationship between two variables. It ranges from -1 to 1:

-   Positive Correlation (1):   When one variable increases, the other variable tends to increase as well.
-   Negative Correlation (-1):   When one variable increases, the other variable tends to decrease.
-   No Correlation (0):   There is no linear relationship between the variables.

### Correlation Matrix:

In data analysis, we often deal with multiple variables. A correlation matrix is a table that shows the correlation coefficients between many variables. Each cell in the table represents the correlation between two variables.

### Correlation Heatmap:

A correlation heatmap takes the correlation matrix and visualizes it using colors. The heatmap provides a quick and easy way to identify patterns in the data. Here's how it works:

-   Color Gradient:   The heatmap assigns a color gradient to the correlation values. Commonly, warm colors like red or orange represent positive correlations, while cool colors like blue represent negative correlations.
  
-   Intensity of Color:   The intensity or darkness of the color indicates the strength of the correlation. Stronger correlations (closer to -1 or 1) appear darker, making it easy to spot significant relationships in the data.

-   Axes Labels:   The heatmap has the variables on both the X and Y axes, making it easy to identify which variables are being compared.


![WHORegion Count Plot](media/TBCases_heatmap.png)

## Plot 3

A histogram for the count of years in a dataset visually displays how frequently each year appears. Each bar represents a year, and its height indicates how many times that year occurs in the data. It provides a clear snapshot of the dataset's temporal distribution, helping to identify prevalent years and patterns quickly.
![WHORegion Count Plot](media/TBCases_histogram.png)


## Plot 4

A pair plot is a graphical representation in data analysis, showing scatter plots for variables in a dataset, organized in a grid. It compares every variable with every other variable, displaying correlations and distributions at once. Pair plots help identify patterns, relationships, and outliers in multivariate data, aiding in comprehensive insights.

![WHORegion Count Plot](media/TBCases_pairplot.png)

## Plot 5


A violin plot is a method of plotting numeric data and can be particularly useful when comparing the distribution of a numerical variable across different categories. In wer case, we want to create a violin plot to compare the treatment success rates of HIV-positive cases across different WHO regions. Here's how we can interpret it:

Interpreting a Violin Plot:
1. Y-Axis:
Variable: The Y-axis represents the treatment success rate of HIV-positive cases.

2. X-Axis:
Variable: The X-axis represents the different WHO regions.
Categories: Each category on the X-axis corresponds to a specific WHO region.
3. Violin Shape:
Width: Wider sections indicate a higher density of cases in that treatment success rate range.

![WHORegion Count Plot](media/WHO_Region_vs_TSR_HIV_PTB.png)

## Plot 6

A box plot, also known as a box-and-whisker plot, is a graphical representation of the distribution of a dataset. It shows the minimum, first quartile, median (second quartile), third quartile, and maximum of a dataset. When comparing the treatment success rates of new TB cases across different WHO regions using a box plot, here's how we can interpret:

Box plot:

Height: The box represents the interquartile range (IQR), the range between the first quartile (Q1) and the third quartile (Q3). It contains the middle 50% of the data.

Middle Line: The line inside the box represents the median treatment success rate for each WHO region.

Wider Box (East Asia Region): A wider box indicates a larger interquartile range, suggesting higher variability in treatment success rates among new TB cases in the East Asia region.

Lighter Box (Western Pacific Region): A lighter box implies a smaller interquartile range, indicating more consistency in treatment success rates among new TB cases in 
the Western Pacific region.

![WHORegion Count Plot](media/WHO_Region_vs_TSR_new_TB_cases.png)


## Plot 7

A bar plot is a common way to represent categorical data. In wer case, we want to create a bar plot to compare the treatment success rates of XDR TB (Extensively Drug-Resistant Tuberculosis) cases across different WHO regions. 

Bigger Bar (Western Pacific Region): A bigger bar for the Western Pacific region suggests a higher treatment success rate for XDR TB cases in this region.

Smaller Bar (Europe Region): A smaller bar for the Europe region indicates a comparatively lower treatment success rate for XDR TB cases in this region.


![WHORegion Count Plot](media/WHO_Region_vs_TSR_XDR_TB_cases.png)




