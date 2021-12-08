# pylint: skip-file

import csv

with open('results/calc_log.csv', 'w') as new_file:
    fieldnames = ['unix_time', 'filename', 'record_number', 'operation', 'calc_result']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow([notgonnawork])

