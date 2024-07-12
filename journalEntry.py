import datetime

class JournalEntry():
    def __init__(self, entry: str = "Empty", entryDate = datetime.date.today()):
        self.entryDate = entryDate
        self.entry = entry
    
    def updateEntry(self, entry):
        self.entry = entry
    
    def updateDate(self, entryDate):
        self.today = entryDate

    def __eq__(self, other):
        return self.entryDate == other.entryDate

    def __lt__(self, other):
        return self.entryDate < other.entryDate