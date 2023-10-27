import pandas as pd

class DataLoader:
    """
    A class for loading, describing, and manipulating data from a CSV file.

    Parameters:
        path (str): The file path to the CSV file.

    Attributes:
        path (str): The file path to the CSV file.
        data_frame (pd.DataFrame): The DataFrame containing the loaded data.
    """
    
    def __init__(self, path: str):
        self.path = path 
        self.data_frame = pd.read_csv(self.path)

    @staticmethod
    def _print_section_header(header: str):
        """Helper function to print section headers."""
        print("\n", "* " * 10, header, "* " * 10)
    
    def load_data(self):
        """Load and display the first 5 rows and information about the data."""
        self._print_section_header("Data Info")
        print("\nFirst 5 rows of the data:")
        print(self.data_frame.head())
        print("\nData Info:")
        print(self.data_frame.info())
    
    def describe_data(self):
        """Display summary statistics of the data."""
        self._print_section_header("Data Description")
        print("\nData Description:")
        print(self.data_frame.describe())
    
    def get_column_names(self) -> list:
        """Get column names of the DataFrame."""
        print("\nColumn Names:",self.data_frame.columns.tolist())
    
    def missing_values_count(self) -> pd.Series:
        """Count missing values in each column."""
        print("\n Missing Values :",self.data_frame.isnull().sum())

    
    def drop_columns(self, columns_to_drop: list):
        """
        Drop specified columns from the DataFrame.

        Parameters:
            columns_to_drop (list): A list of column names to be dropped from the DataFrame.
        """
        self.data_frame.drop(columns=columns_to_drop, inplace=True)
        print("Columns", columns_to_drop, "have been dropped.")

    def get_data(self):
        return self.data_frame
        