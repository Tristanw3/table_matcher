import csv


def get_csv_data(filepath: str):
    data = []
    with open(filepath, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            data.append(row)
    return data

def match_tables(table_1: list, table_2: list):
    if(table_1 == table_2):
        print("Matched")

if __name__ == '__main__':
    filepath_1 = './test_data.csv'
    table_1 = get_csv_data(filepath_1)

    filepath_2 = './test_data.csv'
    table_2 = get_csv_data(filepath_2)
    
    match_tables(table_1, table_2)
