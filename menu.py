import datetime
from journal import Journal

class Menu():
    def __init__(self, journal):
        self.journal = journal
    
    def showMenu(self):
        journal = self.journal
        while(True):
            journal.displayEntries()
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
                            
                            break
                        except ValueError:
                            handle = input("Invalid date! Try again? [Y/N]: ")
                            if(handle.upper() == 'N'): break
                        except Exception as e:
                            print(e)
                            break
                    entryIn = input("Please type your entry: ")
                    journal.createEntry(entryIn, dateIn)
                    input("Any key to continue: ")

                case 'R':
                    while(True):
                        selection = input("Enter id of entry to read: ")
                        selection = int(selection)-1
                        if(0 <= selection < journal.length()):
                            journal.readEntry(selection)
                            input("Any key to continue: ")
                            break
                        else:
                            handle = input("Entry not available! Try again? [Y/N]: ")
                            if (handle.upper() == "N"): break
                        
                case 'U':
                    while(True):
                        selection = input("Enter id of entry to update: ")
                        selection = int(selection)-1
                        if(0 <= selection < journal.length()):
                            journal.readEntry(selection)
                            entryIn = input("Please enter new entry: ")
                            journal.updateEntry(selection, entryIn)
                            journal.readEntry(selection)
                            input("Any key to continue: ")
                            break
                        else:
                            handle = input("Entry not available! Try again? [Y/N]: ")
                            if (handle.upper() == "N"): break

                case 'D':
                    while(True):
                        selection = input("Enter id of entry to delete: ")
                        selection = int(selection)-1 
                        if(0 <= selection < journal.length()):
                            journal.deleteEntry(selection)
                            
                            input("Any key to continue: ")
                            break
                        else:
                            handle = input("Entry not available! Try again? [Y/N]: ")
                            if (handle.upper() == "N"): break

                case 'E':
                    break
                case _:
                    input("Invalid Selection! Any key to continue: ")