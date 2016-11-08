from connection import Connection
import random
import collections


class SecretSanta:


    def __init__(self, families, members, oldConnections):
        self.families = families
        self.members  = members
        self.oldConnections = oldConnections

    
    def connectionValid(self, conn):

        sourceFam = self.families[conn.source]
        targetFam = self.families[conn.target]

        return (sourceFam != targetFam
            and not self.oldConnections.has(
                        conn.source,
                        conn.target) 
            and not self.oldConnections.has(
                        conn.target,
                        conn.source))


    def randomConnection(self, sourceQueue, targetQueue, year):

        s = len(sourceQueue) - 1
        t = len(targetQueue) - 1
        
        changeSources = True

        while s >= 0 and t >= 0:

            source = sourceQueue[s]
            target = targetQueue[t]

            conn = self.oldConnections.makeWeightedConn(
                source,
                target,
                year
            )
        
            if self.connectionValid(conn):

                if s < len(sourceQueue) - 1:
                    sourceQueue[s] = sourceQueue.pop()
                else:
                    sourceQueue.pop()

                if t < len(targetQueue) - 1:
                    targetQueue[t] = targetQueue.pop()
                else:
                    targetQueue.pop()

                return conn

            if changeSources:
                s -= 1
            else:
                t -= 1

            changeSources = not changeSources
                
        # Cannot generate valid connection
        return None                


    def genConnections(self, year):
        
        connections = []

        members = list(self.families.keys())
        random.shuffle(members)
        sourceQueue = collections.deque(members)
        random.shuffle(members)
        targetQueue = collections.deque(members)

        matchedSources = set()
        matchedTargets = set()

        while len(sourceQueue) > 0 and len(targetQueue) > 0:

            # Attempt to generate random connection
            # using unmatched nodes from queues
            conn = self.randomConnection(sourceQueue,
                                         targetQueue,
                                         year)
            if conn is not None:
                matchedSources.add(conn.source)
                matchedTargets.add(conn.target)

            connections.append(conn)

            if len(connections) == len(members):
                break
                        

        return connections

    

