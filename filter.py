import pandas as pd

def filter(input, output):
    excel = pd.read_excel(input)
    suffixes = ('@domain.com', '@domain.eu')
    excel_filtered = excel[~excel['email'].str.endswith(suffixes)]
    excel_filtered.to_excel(output, index=False)

if __name__ == "__main__":
    input_name = 'your_excel_file.xlsx'
    output_name = 'new_excel_file.xlsx'
    filter(input_name, output_name)