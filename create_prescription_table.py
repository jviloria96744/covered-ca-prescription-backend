import os
import pandas as pd


def create_prescription_table():
    """
    This function is used to create one central prescription table aggregating all insurer's individual formulary tables
    """

    file_path = "Formularies/Formulary Tables/"

    # Checking if file exists and if so, removing the file to create a new one
    # This can be turned into a function that adds the delta instead
    if os.path.exists(file_path + "Prescription-Tables.csv"):
        os.remove(file_path + "Prescription-Tables.csv")
        print("Old Prescription-Tables file removed")
    else:
        print("Prescription-Tables file does not exist")

    file_list = os.listdir(file_path)

    tables = []

    for file in file_list:
        df = pd.read_csv(file_path + file)

        # The tables all have three columns: Prescription Drug Name, Drug Tier, Coverage Requirements and Responsibilities
        # In the aggregated table, a 4th column is added with the Insurer Name so results of a search can be separated by insurer
        df['Insurer'] = file.split('.csv')[0]
        tables.append(df)

    # Aggregating tables
    prescription_table = pd.concat(tables)
    prescription_table.to_csv(
        file_path + 'Prescription-Tables.csv', index=False)


if __name__ == "__main__":
    create_prescription_table()
