import pandas as pd
import json

def search_prescription_table(terms):
    file_path = 'Formularies/Formulary Tables/Prescription-Tables.csv'
    table = pd.read_csv(file_path, na_filter=False)

    frames = []
    for term in terms:
        frames.append(table[table['Prescription Drug Name'].str.contains(term)])
    
    search_results_table = pd.concat(frames)

    insurers = search_results_table['Insurer'].unique()

    json_object = {}

    for item in insurers:
        json_object[item] = search_results_table[search_results_table['Insurer'] == item].to_dict('records') 
    
    with open('test_search_response.json', 'w') as fp:
        json.dump({"Data": json_object}, fp)

if __name__ == "__main__":
    test_values = ['montelukast sodium', 'atorvastatin']
    search_prescription_table(test_values)