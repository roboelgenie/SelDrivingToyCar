import os
import csv

input_csv_path = 'timestamps_raw.csv'
output_csv_path = 'timestamps.csv'

with open(input_csv_path, 'r', newline='') as input_file, open(output_csv_path, 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    for row in csv_reader:
        if len(row) == 5:
            csv_writer.writerow(row)

        else:
            if row and row[0]:
                first_row = row[:0]
                file_to_delete = os.path.join('captured_frames', row[0])
                if os.path.exists(file_to_delete):
                    os.remove(file_to_delete)
                else:
                    print(f"File: {row} doesn't exist")

                print(f"Row: {row} deleted")
            else:
                print(f"Empty firs column: {row}")

