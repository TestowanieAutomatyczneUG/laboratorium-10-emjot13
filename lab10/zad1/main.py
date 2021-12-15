class Note:
    def __init__(self, name, note):
        if type(name) is not str:
            raise Exception("Given name must be a string")
        if type(note) is not float:
            raise Exception("Given note must be a float")
        if note < 2 or note > 6:
            raise Exception("Given note value must be between 2 and 6")
        if name is None:
            raise Exception("Given name cannot be none")
        if len(name) == 0:
            raise Exception("Length of given name cannot be 0")

        self.name = name
        self.note = note

    def getName(self):
        return self.name

    def getNote(self):
        return self.note

# dict = {"spr" + str(k):v for k in range(2, 7) for v in range(10, 20)}

# def makedict(size):
#     dict = {}
#     for k in range(1, size):
#         dict["spr" + str(k)] = rd.randint(2, 6)
#
#     print(dict, round(sum(dict.values())/ len(dict.values()), 2))
#
# makedict(100)