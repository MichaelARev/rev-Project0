from journal import Journal
from menu import Menu
import csv
import datetime


BASE_PATH = "C:/Users/Hunter/Desktop/Revature/Python/Project0/entries"
print("JOURNAL APP")

def create_file(path):
    try:
        file = open(path, "w")
        file.close()
    except FileExistsError:
        print("File already exists")

#name = input("Enter name of journal CSV (without .csv): ")
#path = BASE_PATH + "/" + name + ".csv"
#entries = []

while(True):
    name = input("Enter name of journal CSV (without .csv) or 0 to quit: ")
    if(name == '0'): break
    path = BASE_PATH + "/" + name + ".csv"
    entries = []
    try:
        with open(path, "r+") as file:
            csv_reader = csv.reader(file)
            journal = Journal()
            for entryDate, entry in csv_reader:
                if (entryDate == 'Date'): pass
                else:
                    journal.createEntry(entry, datetime.datetime.strptime(entryDate, '%Y-%m-%d').date())
            menu = Menu(journal)
            menu.showMenu()
            break

    except FileNotFoundError:
        answer = input("This file does not exist. Create a new file? [Y/N]: ")
        if answer.upper() == 'Y': 
            create_file(path)
        continue
        

    except Exception as e:
        print(e)
        break

with open(path, "w", newline = '') as file:
    header = ["Date", "Entry"]
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    for entry in journal.entries:
        csv_writer.writerow([entry.entryDate, entry.entry])
    journal.clear()
    
