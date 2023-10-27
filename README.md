# Tuberculosis Treatment Success Rate 

# Data Set

## Overview 

This dataset contains information about tuberculosis (TB) treatment success rates across different regions and years. It includes data on new TB cases, previously treated TB cases, HIV-positive TB cases, multidrug-resistant TB (MDR-TB) cases, and extensively drug-resistant TB (XDR-TB) cases. The data is organized by the World Health Organization (WHO) regions: Global, Africa, Americas, South-East Asia, Europe, Eastern Mediterranean, and Western Pacific.

## Features Explination 

Features :

1. WHO Region: The region to which the data belongs (e.g., Global, Africa, Americas, etc.).
2. Year: The year in which the data was recorded.
3. Treatment Success Rate for New TB Cases: Percentage of successful treatment outcomes for new TB cases.
4. Treatment Success Rate for Previously Treated TB Cases: Percentage of successful treatment outcomes for previously treated TB cases.
5. Treatment Success Rate for HIV-Positive TB Cases: Percentage of successful treatment outcomes for TB cases in patients who are HIV-positive.
6. Treatment Success Rate for Patients Treated for MDR-TB (%): Percentage of successful treatment outcomes for multidrug-resistant TB (MDR-TB) cases.
7. Treatment Success Rate for XDR-TB Cases: Percentage of successful treatment outcomes for extensively drug-resistant TB (XDR-TB) cases.


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

**Plot 1:**The provided count plot illustrates the distribution of the "WHO region" feature across seven distinct classes: Global, Africa, America, South-East Asia, Europe, Eastern Mediterranean, and Western Pacific. Each class is evenly distributed, indicating an equal representation within the dataset. The x-axis represents the different WHO regions, while the y-axis indicates the count of occurrences for each specific region. This visualization provides a clear overview of the balanced distribution of data points among the WHO regions, highlighting the equal representation of each region within the dataset.

![WHORegion Count Plot](media/WHORegion_countplot.png)



