import pandas as pd


def get_generics(terms):
    """
    :terms  list of search terms sent in body of API call from front-end
    This function looks up a table of generic prescriptions mapped to brand-name prescriptions to get alternatives when a brand-name is searched
    """
    file = 'generic-map.txt'

    open_file = open(file, 'r')
    lines = open_file.readlines()

    generic_search_results = {}

    for term in terms:
        if term.isupper():
            generic_search_results[term] = []
            for line in lines:
                values = line.strip().split(',')

                # Currently a simple search of the term/brand-name being substrings of each other is used
                # This can be replaced with a fuzzy match based search
                if term.lower() in values[-1].lower() or values[-1].lower() in term.lower():
                    generic_search_results[term].extend(values[:-1])

    return generic_search_results


if __name__ == '__main__':
    get_generics(['FOSAMAX PLUS D', 'EXFORGE'])
