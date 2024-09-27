import csv

STATE_FIELD_INDEX = 4

with open('DATA/presidents.csv') as old_pres_in:
    with open('presidents_temp.csv', "w") as new_pres_out:
        rdr = csv.reader(old_pres_in)
        wtr = csv.writer(new_pres_out)
        for record in rdr:
            if record[STATE_FIELD_INDEX] == "Virginia":
                record[STATE_FIELD_INDEX] = "North Dakota"
            wtr.writerow(record)
