import random
import secretsanta as ss

class SecretSanta:

    def __init__(self, families, members, oldConnections):
        self.families = families
        self.members  = members
        self.oldConnections = oldConnections

    def randomConnection(self, year):

        # Select random members from different families
        source = random.choice(self.families.keys())
        target = random.choice(self.families.keys())
        while self.families[target] == self.families[source]:
            target = random.choice(self.families.keys())

        return ss.Connection(source, target, year)


    def familyValid(self, connection):
        return True


    def genConnections(self, year):
        return {}

