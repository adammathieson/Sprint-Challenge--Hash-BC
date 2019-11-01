#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        # print(i.source, i.destination)
        hash_table_insert(hashtable, i.source, i.destination)
    

    # print("city----> ", city)
    # print("dest----> ", destination)
    # print("city ++++++> ", city)
    city = "NONE"
    for i in range(length):
        destination = hash_table_retrieve(hashtable, city)
        route[i] = destination
        print("route value at index i", route[i])
        print("city", city)
        city = route[i]


        # print(city)
        # city = hash_table_retrieve(hashtable, destination)
        # destination = hash_table_retrieve(hashtable, city)
    
    # while city is not "NONE":
    #     print("city: ", city)
    #     city = destination
        # print(destination)
            # route.append(city)
            # city = destination
        # print(route)


    # for i in hashtable.storage:
    #     city = None

    #     print(i.key, i.value)


    print(route)
    return route
