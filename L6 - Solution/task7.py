import os
import csv
import datetime as dt
def preprocessoring(filename):
    if os.path.exists(filename):
        with open(filename, mode="r") as file:
            reader = csv.reader(file, delimiter = ",")
            header = next(reader)
            reader = list(reader)
            with open("format_scrubbed.csv", mode="w") as new_file:
                print("format_scrubbed csv file was created")
                writer = csv.writer(new_file, delimiter = ",")
                writer.writerow(header)
                for index in range(len(reader)):
                    if "24:00" in reader[index][0]:
                        reader[index][0] = reader[index][0].replace("24:00", "00:00")
                    new_date = dt.datetime.strptime(reader[index][0],"%m/%d/%Y %H:%M")
                    reader[index][0] = new_date.strftime("%B %d of %Y at %I:%M %p")
                    writer.writerow(reader[index])
    else:
        print("No such file or directory: 'synthetic_data.csv'")

preprocessoring("scrubbed.csv")