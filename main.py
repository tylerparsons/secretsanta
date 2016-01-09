import random
import secretsanta as ss


# CSV column mappings 
FAM_MEMBER_COL  = 0
FAM_FAMILY_COL  = 1

CONN_SOURCE_COL = 0
CONN_TARGET_COL = 1
CONN_YEAR_COL   = 2


def loadFamilyMembers(csvPath):
    '''
    Returns families, a map of members to their
    associated families, and members, a map of 
    families to a set of its members.
    '''
    with open(csvPath, 'r') as file:

        families = {}
        members = {}

        for line in file:
            data = line.strip().split(',')
            member = data[FAM_MEMBER_COL]
            family = data[FAM_FAMILY_COL]
            
            families[member] = family
            if family not in members:
                members[family] = set()
            members[family].add(member)

    return families, members


def loadConnections(csvPath):
    with open(csvPath, 'r') as file:

        connections = ss.ConnectionGraph()

        for line in file:
            data = line.strip().split(',')
            source = data[CONN_SOURCE_COL]
            target = data[CONN_TARGET_COL]
            year   = data[CONN_YEAR_COL]

            connections.add(source, target, year)

    return connections


def main():

    families, members = loadFamilyMembers('families.csv')
    print(families)
    print(members)

    oldConnections = loadConnections('connections.csv')
    print(oldConnections)

    santa = ss.SecretSanta(oldConnections, families, members)

    newConnections = santa.genConnections(2016)
    print(newConnections)


if __name__ == '__main__':
    main()


