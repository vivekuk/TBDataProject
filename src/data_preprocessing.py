import sys
import pandas as pd

class DataPreprocessor:

    
    def __init__(self, data):
        self.data_frame = data
    def get_data(self):
        return self.data_frame
    @staticmethod
    def _print_section_header(header: str):
        """Helper function to print section headers."""
        print("\n\n", "* " * 10, header, "* " * 10)
    def preprocess_data(self):
        """Preprocess the data by handling missing values, data type conversions, and more."""
        self._print_section_header("Data Preprocessing")
        print("\n\n BEFORE : ")
        print(self.data_frame.info())
        print("\n\n")
        # Handling missing values
        self._handle_missing_values()
        
        self._print_section_header("Filled Null Values")
        print("\n\n BEFORE : ")
        print(self.data_frame.info())
        print("\n\n")
        # Convert columns to appropriate data types if needed
        self.data_frame['Year'] = self.data_frame['Year'].astype(int)
        # Add more type conversions as necessary
        print("Data preprocessing completed.")
    
    def _handle_missing_values(self):
        """Handle missing values in the DataFrame."""
        # Filling missing values in numeric columns with mean value
        numeric_columns = self.data_frame.select_dtypes(include=['float64', 'int64']).columns
        self.data_frame[numeric_columns] = self.data_frame[numeric_columns].fillna(self.data_frame[numeric_columns].mean())
        # Filling missing values in object column with most frequent value
        object_columns = self.data_frame.select_dtypes(include=['object']).columns
        self.data_frame[object_columns] = self.data_frame[object_columns].fillna(self.data_frame[object_columns].mode().iloc[0])
    
    def get_data(self):
        return self.data_frame

    def _normalize_numeric_data(self):
        """Normalize numeric columns to scale values between 0 and 1."""
        numeric_columns = self.data_frame.select_dtypes(include=['float64', 'int64']).columns
        self.data_frame[numeric_columns] = (self.data_frame[numeric_columns] - self.data_frame[numeric_columns].min()) / \
                                           (self.data_frame[numeric_columns].max() - self.data_frame[numeric_columns].min())

df = pd.read_csv("/Users/varunreddyseelam/TBDataProject-main/data/TB_c_new_tsr,TB_c_ret_tsr,TB_c_tbhiv_tsr,TB_c_mdr_tsr,TB_c_xdr_tsr.csv")
pp = DataPreprocessor(df)
pp.preprocess_data()