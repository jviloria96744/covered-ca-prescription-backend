import tabula
import pandas as pd
import json

def proc_drug_list(provider_name):
    file = "Formularies/Unprocessed Drug Lists/" + provider_name + ".txt"
    open_file = open(file, 'r') 
    lines = open_file.readlines()

    drug_list = []
    temp = ""
    for line in lines:
        stripped_line = line.strip()
        stripped_line = stripped_line.replace('\n', ' ')

        drug_to_add = temp + stripped_line

        if stripped_line[0:1] == "I-": # This line exists because of the CCHP page structure and should be modified accordingly
            pass
        elif stripped_line[-1].isdigit() and '.' in stripped_line:
            drug_list.append(drug_to_add.split('.')[0].strip())
            temp = ""
        else:
            temp = stripped_line
    
    sorted_drug_list = sorted(drug_list, key=str.casefold)

    drug_options = []
    for drug in sorted_drug_list:
        drug_options.append({"Label": drug, "Value": drug})

    with open('Formularies/Processed Drug Lists/' + provider_name + '.json', 'w') as fp:
        json.dump({"Drug List": drug_options}, fp)


def anthem():
    # Anthem Blue Cross Formulary Processing
    file = "Formularies/Formulary PDFs/Anthem-Blue-Cross.pdf"
    df = tabula.read_pdf(file, output_format='dataframe', pages='11-93')
    table = df[0]

    # Removing rows that were grouping prescriptions into categories, e.g. Asthma medicines
    formulary = table[table['Drug Tier'].notnull()]

    # Removing repeated column headers at the top of new pages
    formulary = formulary.loc[formulary['Prescription Drug Name'] != 'Prescription Drug Name']

    # Resetting index after filtering table, may not be necessary depending on use
    formulary.reset_index(drop=True, inplace=True)

    # Removing carriage return from column names and table entries
    formulary.columns = [s.replace('\r', ' ') for s in formulary.columns]
    formulary = formulary.replace('\r', ' ', regex=True)

    # Example query
    #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    # May change to JSON output depending on research
    formulary.to_csv('Formularies/Formulary Tables/Anthem-Blue-Cross.csv', index=False)


def cchp():
    file = "Formularies/Formulary PDFs/cchp.pdf"
    df = tabula.read_pdf(file, output_format='dataframe', pages='4-147', lattice=True)
    table = df[0]

    del table["Unnamed: 3"]

    # Removing rows that were grouping prescriptions into categories, e.g. Asthma medicines
    formulary = table[table['Status'].notnull()]

    # Removing repeated column headers at the top of new pages
    formulary = formulary.loc[formulary['Drug'] != 'Drug']

    # Resetting index after filtering table, may not be necessary depending on use
    formulary.reset_index(drop=True, inplace=True)

    # # Removing carriage return from column names and table entries
    formulary.columns = ["Prescription Drug Name", "Drug Tier", "Coverage Requirements and Limits"]
    formulary = formulary.replace('\r', ' ', regex=True)

    # # Example query
    #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    # May change to JSON output depending on research
    formulary.to_csv('Formularies/Formulary Tables/cchp.csv', index=False)


def healthnet():
    file = "Formularies/Formulary PDFs/HealthNet.pdf"
    df = tabula.read_pdf(file, output_format='dataframe', pages='10-132', lattice=True, multiple_tables=True)

    formulary = df[0]
    formulary.columns = ["Prescription Drug Name", "Drug Tier", "Coverage Requirements and Limits"]
    formulary = formulary.replace('\r', ' ', regex=True)
    
    formulary = formulary[formulary['Drug Tier'].notnull()]
    formulary = formulary.loc[formulary['Drug Tier'] != 'Drug Tier']

    formulary.reset_index(drop=True, inplace=True)

    #print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    formulary.to_csv('Formularies/Formulary Tables/healthnet.csv', index=False)


# Issue with Kaiser PDF not reading column heading correctly
""" def kaiser():
    file = "Formularies/Formulary PDFs/Kaiser-Permanente.pdf"
    df = tabula.read_pdf(file, output_format='dataframe', pages='12')

    print(type(df))
    print(len(df))

    table = df[0]
    print(table.head())

    # formulary = df[0]
    # formulary.columns = ["Prescription Drug Name", "Drug Tier", "Coverage Requirements and Limits"]
    # formulary = formulary.replace('\r', ' ', regex=True)
    
    # formulary = formulary[formulary['Drug Tier'].notnull()]
    # formulary = formulary.loc[formulary['Drug Tier'] != 'Drug Tier']

    # formulary.reset_index(drop=True, inplace=True)

    # print(formulary[formulary['Prescription Drug Name'].str.contains('montelukast')])

    #formulary.to_csv('Formularies/Formulary Tables/kaiser.csv', index=False)"""


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
    #anthem()
    #cchp()
    #healthnet()
    #kaiser()
    #molina()
    #valley_health()

    #proc_drug_list('CCHP')