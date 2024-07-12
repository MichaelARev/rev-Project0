from journalEntry import JournalEntry
import datetime

class Journal():
    def __init__(self, entries: list[JournalEntry] = []):
        self.entries = entries

    def length(self):
        return len(self.entries)
    
    def displayEntries(self):
        print("====================================================================")
        print("{} entries available".format(len(self.entries)))
        print("====================================================================")
        for id, entry in enumerate(self.entries): print("{}: {}".format(id+1, entry.entryDate))
        print("====================================================================")
    
    def createEntry(self, entryIn, dateIn: datetime.date):
        newEntry = JournalEntry(entryIn, dateIn)
        self.entries.append(newEntry)
        self.entries.sort()
    
    def readEntry(self, selection):
        print("====================================================================")
        print(self.entries[selection].entryDate)
        print(self.entries[selection].entry)
        print("====================================================================")
        
    
    def updateEntry(self, selection, entryIn):
        self.entries[selection].updateEntry(entryIn)

    
    def deleteEntry(self, selection):
        del self.entries[selection]
        print("Entry {} deleted.".format(selection+1))

    def clear(self):
        self.entries = []
        