"""
Also on SOLID with Python examples
https://habr.com/ru/company/otus/blog/651753/
"""


# Single responsibility = Separation of concerns
# You don't want to overload objects with too many responsibilities. Anti pattern - God Object.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # braking SPR by giving the journal the additional responsibilities
    # This is a bad idea
    # Cause all of that types may have it's own load and save
    # So if you will need to change load method you will have to change it in every class
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('Hello!')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = r'C:\temp\journal.txt'
# serializing to a file and reading from it
PersistenceManager.save_to_file(j, file)

with open(file) as fh:  # fh = file handle
    print(fh.read())
