import csv

with open("dummy.csv", "w") as f:
    f.write('"hello\0", "csv", "world"')

with open("dummy.csv", "f") as f:
    reader = csv.reader((line.replace("\0", "") for line in f))
