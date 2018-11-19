import re

def dictify_csv(f):
    fstring = f.read().decode("utf-8")
    array = fstring.splitlines()
    csv_dict = []
    headers = []
    for i, row in enumerate(array):
        split_row = row.split(',')
        if i == 0:
            for column in split_row:
                headers.append(column)
        else:
            row_dict = {}

            for i, column in enumerate(split_row):
                row_dict[headers[i]] = column
            csv_dict.append(row_dict)
    return csv_dict
