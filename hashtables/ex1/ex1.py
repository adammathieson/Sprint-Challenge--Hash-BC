#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# for i in range(5):
#     print(i)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Create hash table
    for i in range(length):
        # print(i, weights[i])
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        target = limit - weights[i]

        if hash_table_retrieve(ht, target):
            print("-------->", (hash_table_retrieve(ht, target), i))
            return (hash_table_retrieve(ht, target), i)
        # else:
        #     return None


    # # print("hashtable ----> : ", ht.storage)
    # for i in ht.storage:
    #     print("key/value of ht: ", i.key, i.value)

    # return ht


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
