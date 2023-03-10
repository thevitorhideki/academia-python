import csv

with open('dados.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    with open('dados.tsv', 'w') as tsvfile:
        tsvwriter = csv.writer(tsvfile, delimiter='\t')

        for row in csvreader:
            tsvwriter.writerow(row)
