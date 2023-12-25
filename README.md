# Stock Prices Analysis with MapReduce

<!--![Project Image](project_image.png)  Add an image related to your project if available -->

## Overview

This project involves the analysis of historical stock prices of 500 major companies using MapReduce. The data, extracted from Yahoo Finance, spans a period of five years. The main goals are trend analysis, volatility assessment, and predictive modeling.

## Project Structure

- `cleaned_dataset.csv`: The cleaned dataset after data preprocessing.
- `original_dataset.csv`: The original dataset from Yahoo Finance.
- `Stock_Prices_Analysis.ipynb`: Jupyter Notebook containing the main code for data analysis.
- `MapReduceHadoop/`: Folder containing Hadoop MapReduce files for parallel processing.
  - `mapper.py`: Mapper script for Hadoop MapReduce.
  - `reducer.py`: Reducer script for Hadoop MapReduce.
- `report.pdf`: A detailed report on the project, including methodology and findings.

## Instructions

1. **Data Cleaning and Exploration**: Refer to the Jupyter Notebook (`Stock_Prices_Analysis.ipynb`) for data cleaning, exploration, and basic statistics.

2. **MapReduce Implementation**:
   - For local multiprocessing, check the code in the Jupyter Notebook.
   - For Hadoop MapReduce:
     - Upload the cleaned dataset to Hadoop Distributed File System (HDFS).
     - Execute the MapReduce job using `hadoop jar hadoop-streaming.jar -mapper mapper.py -reducer reducer.py -input input_data_path -output output_path`.

3. **Results and Visualizations**: Explore the results and visualizations in the Jupyter Notebook.

## Requirements

- Python 3
- Jupyter Notebook
- Hadoop (if using Hadoop MapReduce)

## Contribution

Feel free to contribute by forking the repository and creating a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

