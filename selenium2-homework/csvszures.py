import csv

with open("table_in.csv", "r", encoding="UTF-8") as table:
    with open("filtered_table.csv", "w", encoding="UTF-8") as filt:
        next(table)
        table_reader = csv.reader(table, delimiter=",")
        for row in table_reader:
            filt.write(row[1])
            filt.write(", ")
            filt.write(row[0])
            filt.write("\n")
