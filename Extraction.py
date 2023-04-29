import csv
import gzip

with gzip.open('amazon0302.txt.gz', 'rt') as f:
    reader = csv.reader(f, delimiter='\t')
    with open('amazon0302.csv', 'w') as fout:
        writer = csv.writer(fout)
        for row in reader:
            writer.writerow(row)
