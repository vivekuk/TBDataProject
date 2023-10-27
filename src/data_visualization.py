import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    """
    A class for visualizing the plots to explain relationship between features in the data set

    Parameters:
        data: dataframe
    """
    
    def __init__(self,data):
        self.data_frame = data
    @staticmethod
    def _print_section_header(header: str):
        """Helper function to print section headers."""
        print("\n\n", "* " * 10, header, "* " * 10)

    def create_countplot(self, column: str, output_path: str):
        """Create a count plot for a specific column and save it as an image."""
        plt.figure(figsize=(15, 15))
        sns.countplot(x=column, data=self.data_frame)
        plt.title(f'Count of Data Points for {column}')
        plt.xticks(rotation=45)
        plt.savefig(output_path)
        plt.close()
    
    def create_histogram(self, column: str, output_path: str):
        """Create a histogram for a numeric column and save it as an image."""
        plt.figure(figsize=(15, 15))
        sns.histplot(x=column, data=self.data_frame, bins=10)
        plt.title(f'Distribution of {column}')
        plt.savefig(output_path)
        plt.close()
    
    def create_pairplot(self, columns: list, output_path: str):
        """Create a pair plot for selected numeric columns and save it as an image."""
        plt.figure(figsize=(15, 15))
        sns.pairplot(self.data_frame[columns])
        plt.title('Pair Plot for Selected Numeric Columns')
        plt.savefig(output_path)
        plt.close()

    def create_boxplot(self, x_column: str, y_column: str, output_path: str):
        """Create a box plot and save it as an image."""
        plt.figure(figsize=(15, 15))
        sns.boxplot(x=x_column, y=y_column, data=self.data_frame)
        plt.title(f'Box Plot for {x_column} vs {y_column}')
        plt.xticks(rotation=45)
        plt.savefig(output_path)
        plt.close()

    def create_violinplot(self, x_column: str, y_column: str, output_path: str):
        """Create a violin plot and save it as an image."""
        plt.figure(figsize=(15, 15))
        sns.violinplot(x=x_column, y=y_column, data=self.data_frame)
        plt.title(f'Violin Plot for {x_column} vs {y_column}')
        plt.xticks(rotation=45)
        plt.savefig(output_path)
        plt.close()

    def create_barplot(self, x_column: str, y_column: str, output_path: str):
        """Create a bar plot and save it as an image."""
        plt.figure(figsize=(15, 15))
        sns.barplot(x=x_column, y=y_column, data=self.data_frame)
        plt.title(f'Bar Plot for {x_column} vs {y_column}')
        plt.xticks(rotation=45)
        plt.savefig(output_path)
        plt.close()

    def create_heatmap(self, output_path: str):
        """Create a correlation heatmap and save it as an image."""
        numeric_columns = self.data_frame.select_dtypes(include=['float64', 'int64']).columns
        numeric_data = self.data_frame[numeric_columns]
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap (Numeric Columns Only)')
        plt.savefig(output_path)
        plt.close()

    def done(self):
        self._print_section_header("Data Visualization Completed, Check media folder")
        print("\n\n")
