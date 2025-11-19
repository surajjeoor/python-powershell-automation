import csv

def write_csv(file_path, data, header=None):
    """
    Write data to a CSV file.

    :param file_path: Path to the CSV file.
    :param data: List of rows, where each row is a list of values.
    :param header: Optional list of column headers.
    """
    with open( file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if header:
            writer.writerow(header)
        
        writer.writerows(data)

# Example usage
data = [
    ['Alice', 30, 'Engineer'],
    ['Bob', 25, 'Designer'],
    ['Charlie', 35, 'Teacher']
]
header = ['Name', 'Age', 'Occupation']
write_csv('people.csv', data, header)
