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
        print('Matched')
        print('Number of Rows - ' + len(table_1))
    else:
        print('Not Matched')

if __name__ == '__main__':
    filepath_1 = './tests/test_data_files/test_data_1.csv'
    table_1 = get_csv_data(filepath_1)

    filepath_2 = './tests/test_data_files/test_data_2.csv'
    table_2 = get_csv_data(filepath_2)
    
    match_tables(table_1, table_2)
