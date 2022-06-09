import csv

with open('tasks.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        with open("new_redirects/" + row[0] + ".txt", 'w') as wikipage:
            wikipage.write("#redirect [[" + row[1] + "]]")
print("DONE!")
