import csv
writer = csv.DictWriter(fp_to_write)
reader = csv.DictReader(fp_to_read)
index = 0
for row in reader:
    row['id'] = index
    writer.write(row)
    index += 1