# SRP
class Journal: 
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)
    

j = Journal()

j.add_entry('I went to library')
j.add_entry('I ate a burger')
print(f'Journal entries: \n{j}')