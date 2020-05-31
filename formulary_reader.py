import tabula
import pandas as pd
import json


def anthem():
    # Anthem Blue Cross Formulary Processing
    file = "Formularies/Formulary PDFs/Anthem-Blue-Cross.pdf"
    df = tabula.read_pdf(file, output_format='dataframe', pages='11-93')
    table = df[0]

    # Removing rows that were grouping prescriptions into categories, e.g. Asthma medicines
    formulary = table[table['Drug Tier'].notnull()]

    # Removing repeated column headers at the top of new pages
    formulary = formulary.loc[formulary['Prescription Drug Name']
                              != 'Prescription Drug Name']

    # Resetting index after filtering table, may not be necessary depending on use
    formulary.reset_index(drop=True, inplace=True)

    # Removing carriage return from column names and table entries
    formulary.columns = [s.replace('\r', ' ') for s in formulary.columns]
    formulary = formulary.replace('\r', ' ', regex=True)

    # Example query
    #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    # May change to JSON output depending on research
    formulary.to_csv(
        'Formularies/Formulary Tables/Anthem-Blue-Cross.csv', index=False)


def cchp():
    file = "Formularies/Formulary PDFs/cchp.pdf"
    df = tabula.read_pdf(file, output_format='dataframe',
                         pages='4-147', lattice=True)
    table = df[0]

    del table["Unnamed: 3"]

    # Removing rows that were grouping prescriptions into categories, e.g. Asthma medicines
    formulary = table[table['Status'].notnull()]

    # Removing repeated column headers at the top of new pages
    formulary = formulary.loc[formulary['Drug'] != 'Drug']

    # Resetting index after filtering table, may not be necessary depending on use
    formulary.reset_index(drop=True, inplace=True)

    # # Removing carriage return from column names and table entries
    formulary.columns = ["Prescription Drug Name",
                         "Drug Tier", "Coverage Requirements and Limits"]
    formulary = formulary.replace('\r', ' ', regex=True)

    # # Example query
    #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    # May change to JSON output depending on research
    formulary.to_csv('Formularies/Formulary Tables/cchp.csv', index=False)


def healthnet():
    file = "Formularies/Formulary PDFs/HealthNet.pdf"
    df = tabula.read_pdf(file, output_format='dataframe',
                         pages='10-132', lattice=True, multiple_tables=True)

    formulary = df[0]
    formulary.columns = ["Prescription Drug Name",
                         "Drug Tier", "Coverage Requirements and Limits"]
    formulary = formulary.replace('\r', ' ', regex=True)

    formulary = formulary[formulary['Drug Tier'].notnull()]
    formulary = formulary.loc[formulary['Drug Tier'] != 'Drug Tier']

    formulary.reset_index(drop=True, inplace=True)

    #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    formulary.to_csv('Formularies/Formulary Tables/healthnet.csv', index=False)


def kaiser():
    file = "Formularies/Formulary PDFs/Kaiser-Permanente.pdf"
    df = tabula.read_pdf(file, output_format='dataframe',
                         pages='12-112', lattice=True)
    # pages='12-112'

    formulary = df[0]

    # The Kaiser PDF gets read in as 7 columns so we take the first four columns (index is column 0)
    formulary = formulary.iloc[:, 0:3]

    # Column names are read in improperly so we change the column names to our common table names
    formulary.columns = ["Prescription Drug Name",
                         "Drug Tier", "Coverage Requirements and Limits"]

    # Dropping rows that had NaN values in the first two columns as those two columns should always have values
    formulary = formulary.dropna(
        subset=(['Prescription Drug Name', 'Drug Tier']))

    # Removing escape characters
    formulary = formulary.replace('\r', ' ', regex=True)

    # Resetting index
    formulary.reset_index(drop=True, inplace=True)

    # Sample Search
    # print(
    #    formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    formulary.to_csv('Formularies/Formulary Tables/kaiser.csv', index=False)


# No lines make processing Molina's PDF difficult
""" def molina():
    file = "Formularies/Formulary PDFs/Molina.pdf"
    df = tabula.read_pdf(file, output_format='dataframe', pages='16', stream=True)
    print(type(df))
    print(len(df))

    #formulary = df[0]
    #print(formulary.head())
    # formulary.columns = ["Prescription Drug Name", "Drug Tier", "Coverage Requirements and Limits"]
    # formulary = formulary.replace('\r', ' ', regex=True)
    
    # formulary = formulary[formulary['Drug Tier'].notnull()]
    # formulary = formulary.loc[formulary['Drug Tier'] != 'Drug Tier']

    # formulary.reset_index(drop=True, inplace=True)

    # #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    # formulary.to_csv('Formularies/Formulary Tables/healthnet.csv', index=False) """


# Issue processing PDF table, columns are being combined into one column
# def valley_health():
#     file = "Formularies/Formulary PDFs/Valley-Health.pdf"
#     df = tabula.read_pdf(file, output_format='dataframe', pages='21', lattice=True)

#     formulary = df[0]
#     print(formulary.head())
#     # formulary.columns = ["Prescription Drug Name", "Drug Tier", "Coverage Requirements and Limits"]
#     # formulary = formulary.replace('\r', ' ', regex=True)

#     # formulary = formulary[formulary['Drug Tier'].notnull()]
#     # formulary = formulary.loc[formulary['Drug Tier'] != 'Drug Tier']

#     # formulary.reset_index(drop=True, inplace=True)

#     # #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

#     # formulary.to_csv('Formularies/Formulary Tables/healthnet.csv', index=False)


if __name__ == "__main__":
    # anthem()
    # cchp()
    # healthnet()
    kaiser()
    # molina()
    # valley_health()

    pass
