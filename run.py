import sys
import os
import src.data_loading
import src.data_preprocessing 
import src.data_visualization 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <csv_file_path> <output_images_directory>")
    else:
        #file_path = "/Users/varunreddyseelam/TBDataProject-main/data/TB_c_new_tsr,TB_c_ret_tsr,TB_c_tbhiv_tsr,TB_c_mdr_tsr,TB_c_xdr_tsr.csv"  # Replace this with the actual file path

        file_path = sys.argv[1]
        output_directory = sys.argv[2]
        data_loader = src.data_loading.DataLoader(file_path)
        data_loader.load_data()
        data_loader.describe_data()
        data_loader.get_column_names()
        data_loader.missing_values_count()
        data_preprocessor = src.data_preprocessing.DataPreprocessor(data_loader.get_data())
        data_preprocessor.preprocess_data()
        df = data_preprocessor.get_data()
        # Create visualizations and save them as images
        data_visualizer = src.data_visualization.DataVisualizer(df)
        data_visualizer.create_countplot('WHO region', os.path.join(output_directory, 'WHORegion_countplot.png'))
        data_visualizer.create_histogram('Year', os.path.join(output_directory, 'TBCases_histogram.png'))
        data_visualizer.create_pairplot(['Year', 'Treatment success rate: new TB cases', 
                                            'Treatment success rate: previously treated TB cases'],
                                            os.path.join(output_directory, 'TBCases_pairplot.png'))
        data_visualizer.create_heatmap(os.path.join(output_directory,'TBCases_heatmap.png'))
        data_visualizer.create_violinplot('WHO region', 'Treatment success rate: HIV-positive TB cases',
                                            os.path.join(output_directory, 'WHO_Region_vs_TSR_HIV_PTB.png'))
        data_visualizer.create_barplot('WHO region', 'Treatment success rate: XDR-TB cases',
                                        os.path.join(output_directory, 'WHO_Region_vs_TSR_XDR_TB_cases.png'))
        data_visualizer.create_boxplot('WHO region', 'Treatment success rate for patients treated for MDR-TB (%)',
                                        os.path.join(output_directory, 'WHO_Region_vs_TSR_XDR_TB_%_cases.png'))
        data_visualizer.create_boxplot('WHO region', 'Treatment success rate: new TB cases',
                                        os.path.join(output_directory, 'WHO_Region_vs_TSR_new_TB_cases.png'))
        data_visualizer.done()