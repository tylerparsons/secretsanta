
class Connection:

    def __init__(self, source, target, year):
        self.source = source
        self.target = target
        self.year   = year

    def __str__(self):
        return "{}|{}|{}".format(self.source,
                                 self.target,
                                 self.year)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.source,
                     self.target,
                     self.year))

