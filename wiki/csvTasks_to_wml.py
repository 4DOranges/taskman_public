import csv

with open('tasks.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        with open("new_pages/" + row[1] + ".txt", 'w') as wikipage:
            wikipage.write('''{{stub}}
      {{Infobox Task
|description=''')
            wikipage.write(row[2] + "\n")
            try:                
                wikipage.write("|tier=" + row[4].capitalize() + "\n")
            except IndexError:
                print(row)
            wikipage.write("|id=" + row[0] + "\n")
            wikipage.write("|wiki=" + row[3] + "\n")
            wikipage.write("|wikialt=" + row[3].replace("_", " ") + "\n")
            wikipage.write("}}")
print("DONE!")
