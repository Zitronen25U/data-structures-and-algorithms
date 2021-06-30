
from hashtable.hashtable import Hashtable


def left_join(table1,table2):
    answer_key = []

    for bucket in table1._buckets:
        if bucket:
            current = bucket.head
            while current:
                current_key = current.value[0]
                value = current.value[1]
                pairs = [current_key,value]
                if table2.Hastable.contains(current_key):
                    pairs.append(table2.Hashtable.get(current_key))
                    answer_key.append(pairs)

    return answer_key
        



