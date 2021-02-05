
import csv
from operator import attrgetter

class Adjacency(object):
    def __init__(self,object_id,priority,distance,tier,attempts,hosr):        
        self.object_Id = object_id
        self.priority = priority
        self.distance = distance
        self.tier = tier
        self.attempts = attempts
        self.hosr = hosr

    def __repr__(self):
        return self.object_Id


def parse():
    with open('adjacencies.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if(i != 0):
                adjacency_list.append(Adjacency(row[0], int(row[1]), row[2], row[3], row[4], row[5]))

adjacency_list = []

parse()

# by priority
adjacency_list.sort(key=lambda x: x.priority)






        


