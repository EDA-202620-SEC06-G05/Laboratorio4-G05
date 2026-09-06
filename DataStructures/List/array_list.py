def new_list():
    newlist= {
        "elements": [],
        "size": 0
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list  

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0] if my_list["size"] > 0 else None

def is_empty(my_list):
    return my_list["size"] == 0 

def size(my_list):
    return my_list["size"]  

def last_element(my_list): 
    return my_list["elements"][my_list["size"] - 1] if my_list["size"] > 0 else None

def delete_element(my_list, pos):
    if pos < my_list["size"]:
        del my_list["elements"][pos]
        my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    element = my_list["elements"][0] 
    my_list["elements"] = my_list["elements"][1:]
    my_list["size"] -= 1
    return element 
    
    
    
def remove_last(my_list):
    element = my_list["elements"][my_list["size"] - 1]
    my_list["elements"] = my_list["elements"][:-1]
    my_list["size"] -= 1
    return element

def insert_element(my_list, pos, element):
    if pos <= my_list["size"]:
        my_list["elements"].insert(pos, element)
        my_list["size"] += 1
    return my_list

def change_info(my_list, pos, element):
    if pos < my_list["size"]:
        my_list["elements"][pos] = element
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < my_list["size"] and pos2 < my_list["size"]:
        temp = my_list["elements"][pos1]
        my_list["elements"][pos1] = my_list["elements"][pos2]
        my_list["elements"][pos2] = temp
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < my_list["size"]:
        end_pos = min(pos + num_elements, my_list["size"])
        sublist = {
            "elements": my_list["elements"][pos:end_pos],
            "size": end_pos - pos
        }
        return sublist
    return None