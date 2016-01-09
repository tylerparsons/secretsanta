
class ConnectionGraph:

    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return repr(self.vertices)

    def add(self, source, target, year):
        if source not in self.vertices:
            self.vertices[source] = { target: set([year]) }
        elif target not in self.vertices[source]:
            self.vertices[source][target] = set([year])
        else:
            self.vertices[source][target].add(year)
        
    def has(self, source, target):
        return (source in self.vertices
           and  target in self.vertices[source])

    def hasInYear(self, source, target, year):
        return (source in self.vertices
           and  target in self.vertices[source]
           and  year   in self.vertices[source][target])

