import csv

filepath = './test_data.csv'

def get_csv_data(filepath: str):
    data = []
    with open(filepath, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            data.append(row)
    return data

if __name__ == '__main__':
    data = get_csv_data()
    print(data)
