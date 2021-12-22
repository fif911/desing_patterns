"""
In prev example we had problem that API of decorator did allow the access to underlying shape
Even though the circle had a method to resize the Circle decorators didnt allowed u to resize that shape
which was a bit annoying

How we fix it:
1)Replicate every single inteface in decorator but thats not really practical
2) :
"""


class FileWithLogging:
    """
    We want to perform some logging after few lines processed
    We want to treat FileWithLogging as if it were a file!
    Typically u had to redefine every single method on file and have it be proxy over to self.file

    So what we trying to do here: we trying to get the file with logging class to masquerade as if it were A File
    And its not a File/ But we want all the attribute request be redirected into the underlying file

    And how we can do this - easy
    We override get attr set attr del attr to actually point into that file that we are storing
    !!!!!!!!!!!! GENIUS !!!!!!!!!!!!
    """

    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    # if somebody will want to iter though the file we should also proxy the behaviour
    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    # this is how we proxy over
    def __getattr__(self, item):
        # return getattr(self.__dict__['file'], item)
        return getattr(self.file, item)

    def __setattr__(self, key, value):
        if key == "file":
            self.__dict__[key] = value
        else:
            # setattr(self.__dict__['file'], key)
            setattr(self.file, key)

    def __delattr__(self, item):
        delattr(self.file, item)


if __name__ == '__main__':
    # file = open("hello.txt")
    file = FileWithLogging(open("hello.txt", mode="w+"))
    file.writelines(["hello", " ", "world"])  # we will use our custom method
    file.write('\ntesting')  # will also work cause file.write will get us to getattr and we are going to get
    # the underlying stuff
    # from the file itself and call file.write on the underlying
    file.close()
