# SRP
from pathlib import Path


class Journal: 
    
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text: str):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos: int):
        del self.entries[pos]

    
    # def save(self, filename: str):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass
    
    
    def __str__(self) -> str:
        return '\n'.join(self.entries)
    

class PersistenceManager:

    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()



j = Journal()

j.add_entry('I went to library')
j.add_entry('I ate a burger')
print(f'Journal entries: \n{j}')

file = f'{Path.cwd()}/journal.txt'
PersistenceManager.save_to_file(j, file)
