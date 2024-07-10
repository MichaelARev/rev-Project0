from journalEntry import JournalEntry
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

def perform_action(entries):
    while(True):
        print("====================================================================")
        print("{} entries available".format(len(entries)))
        print("====================================================================")
        for id, entry in enumerate(entries): print("{}: {}".format(id+1, entry.entryDate))
        print("====================================================================")
        print("Please select an option: ")
        print("[C]reate Entry")
        print("[R]ead Entry")
        print("[U]pdate Entry")
        print("[D]elete Entry")
        print("[E]xit")
        action = input("Selection: ")
        match action.upper():
            case 'C':
                while(True):
                    try:
                        date = input("Enter Date in MM-DD-YYYY Format or 0 for today: ")
                        if (date == '0'): dateIn = datetime.date.today()
                        else: dateIn = datetime.datetime.strptime(date, '%m-%d-%Y').date()

                        entryIn = input("Please type your entry: ")

                        newEntry = JournalEntry(entryIn, dateIn)
                        entries.append(newEntry)
                        entries.sort(key = lambda x: x.entryDate)
                        print("Entry created!")
                        input("Any key to continue: ")
                        break

                    except ValueError:
                        handle = input("Invalid date! Try again? [Y/N]: ")
                        if(handle.upper() == 'N'): break

                    except Exception as e:
                        print(e)
                        break
                    
            case 'R':
                while(True):
                    selection = input("Enter id of entry to read: ")
                    selection = int(selection)-1
                    if(0 <= selection < len(entries)):
                        print("====================================================================")
                        print(entries[selection].entryDate)
                        print(entries[selection].entry)
                        print("====================================================================")
                        input("Any key to continue: ")
                        break
                    else:
                        handle = input("Entry not available! Try again? [Y/N]: ")
                        if (handle.upper() == "N"): break
                    
            case 'U':
                while(True):
                    selection = input("Enter id of entry to update: ")
                    selection = int(selection)-1
                    if(0 <= selection < len(entries)):
                        print("====================================================================")
                        print(entries[selection].entryDate)
                        print("Current entry: {}".format(entries[selection].entry))
                        print("====================================================================")
                        entryIn = input("Please enter new entry: ")
                        entries[selection].entry = entryIn
                        print("Entry updated!")
                        input("Any key to continue: ")
                        break
                    else:
                        handle = input("Entry not available! Try again? [Y/N]: ")
                        if (handle.upper() == "N"): break

            case 'D':
                while(True):
                    selection = input("Enter id of entry to delete: ")
                    selection = int(selection)-1
                    if(0 <= selection < len(entries)):
                        del entries[selection]
                        print("Entry {} deleted.".format(selection))
                        input("Any key to continue: ")
                        break
                    else:
                        handle = input("Entry not available! Try again? [Y/N]: ")
                        if (handle.upper() == "N"): break
            case 'E':
                break
            case _:
                print("Invalid Selection!")

                
            





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
            for entryDate, entry in csv_reader:
                print(entry)
                if (entryDate == 'Date'): pass
                else:
                    entry = JournalEntry(entry, datetime.datetime.strptime(entryDate, '%Y-%m-%d').date())
                    entries.append(entry)
            perform_action(entries)

    except FileNotFoundError:
        answer = input("This file does not exist. Create a new file? [Y/N]: ")
        if answer.upper() == 'Y': 
            create_file(path)
            continue
        else: continue

    except Exception as e:
        print(e)
        break

    with open(path, "w", newline = '') as file:
        header = ["Date", "Entry"]
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        for entry in entries:
            csv_writer.writerow([entry.entryDate, entry.entry])
    
