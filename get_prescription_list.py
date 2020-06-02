import os
import json


def get_drug_list():
    """
    This function is used to get the overall list of prescriptions that populates the select component in the front-end.  These lists are scraped from the index portion of the PDFs in a manual ad-hoc manner.  Similar to the prescription tables, in an ideal world, this function should not exist.
    """
    file_path = "Formularies/Unprocessed Drug Lists/"

    file_list = os.listdir(file_path)

    lines = []

    for file in file_list:
        open_file = open(file_path + file, 'r')
        lines.extend(open_file.readlines())

    prescription_list = []
    temp = ""
    for line in lines:
        stripped_line = line.strip()
        stripped_line = stripped_line.replace('\n', ' ')

        # This line combined with the elif block handles the scenario where the prescription name wraps into two lines
        prescription_to_add = temp + stripped_line

        # This line exists because of the CCHP page structure and should be modified accordingly
        if stripped_line[0:1] == "I-":
            pass
        elif stripped_line[-1].isdigit() and '.' in stripped_line:
            # This conditional block is for the case where the prescription name wrapped into two lines
            if '..' in stripped_line:
                prescription_list.append(
                    prescription_to_add.split('..')[0].strip())
            else:
                prescription_list.append(
                    prescription_to_add.split('.')[0].strip())
            temp = ""
        else:
            temp = stripped_line

    sorted_prescription_list = sorted(
        list(set(prescription_list)), key=str.casefold)

    prescription_options = [{"Label": rx, "Value": rx}
                            for rx in sorted_prescription_list]

    with open('Formularies/Processed Drug Lists/prescription_options.json', 'w') as fp:
        json.dump({"Prescription Options": prescription_options}, fp)


if __name__ == "__main__":
    get_drug_list()
