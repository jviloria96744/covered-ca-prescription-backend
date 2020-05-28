import os
import pandas as pd

def create_prescription_table():
    file_path = "Formularies/Formulary Tables/"

    if os.path.exists(file_path + "Prescription-Tables.csv"):
        os.remove(file_path + "Prescription-Tables.csv")
        print("Old Prescription-Tables file removed")
    else:
        print("Prescription-Tables file does not exist")

    file_list = os.listdir(file_path)

    tables = []

    for file in file_list:
        df = pd.read_csv(file_path + file)
        df['Insurer'] = file.split('.csv')[0]
        tables.append(df)
    
    prescription_table = pd.concat(tables)
    prescription_table.to_csv(file_path + 'Prescription-Tables.csv', index=False)


if __name__ == "__main__":
    create_prescription_table()