def new_single_node(element):
    return {"info": element, "next": None}  



def new_list():
    
    newlist = {
        "first": None,
        "last": None,
        "size": 0
    }
    return newlist
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count
def add_first(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list["first"] is None:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
    my_list["size"] += 1
    return my_list
def add_last(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list["first"] is None:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list
def size(my_list):
    return my_list["size"]  

def first_element(my_list):
    return my_list["first"]["info"] if my_list["first"] is not None else None   

def last_element(my_list):
    return my_list["last"]["info"] if my_list["last"] is not None else None


def is_empty(my_list):
    return my_list["size"] == 0 

def delete_element(my_list, pos):
    if pos == 0: 
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        if my_list["first"] is None:
            my_list["last"] = None
    else: 
        current = my_list["first"]
        for _ in range(pos - 1):
            current = current["next"]
        current["next"] = current["next"]["next"]
        my_list["size"] -= 1
        if current["next"] is None:
            my_list["last"] = current
    return my_list

        
        
        
def remove_first(my_list):
    if my_list["first"] is None:
        return None
    removed_node = my_list["first"]
    my_list["first"] = removed_node["next"]
    if my_list["first"] is None:
        my_list["last"] = None
    my_list["size"] -= 1
    return removed_node["info"]

def remove_last(my_list):
    if my_list["first"] is None:
        return None
    if my_list["first"] == my_list["last"]:
        removed_node = my_list["first"]
        my_list["first"] = None
        my_list["last"] = None
    else:
        prev_node = my_list["first"]
        while prev_node["next"] != my_list["last"]:
            prev_node = prev_node["next"]
        removed_node = my_list["last"]
        prev_node["next"] = None
        my_list["last"] = prev_node
    my_list["size"] -= 1
    return removed_node["info"]
#TODO arreglar insert element. 

def insert_element(my_list, pos, element):
    if pos < 0 or pos > my_list["size"]:
        return my_list
    if pos == 0:
        return add_first(my_list, element)
    elif pos == my_list["size"]:
        return add_last(my_list, element)
    else: 
        new_node = new_single_node (element)
        current = my_list["first"]
        for _ in range(pos - 1):
            current = current["next"]
        new_node["next"] = current["next"]
        current["next"] = new_node
        my_list["size"] += 1
        return my_list
    
    
    
    
    
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        return None
    current_node = my_list["first"]
    for _ in range(pos):
        current_node = current_node["next"]
    current_node["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        return None
    if pos1 == pos2:
        return my_list
    node1 = my_list["first"]
    for _ in range(pos1):
        node1 = node1["next"]
    node2 = my_list["first"]
    for _ in range(pos2):
        node2 = node2["next"]
    node1["info"], node2["info"] = node2["info"], node1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):
    sublist = new_list()
    current = my_list["first"]
    for _ in range(pos):
        current = current["next"]
    for _ in range(num_elements):
        if current is not None: 
            add_last(sublist, current["info"])
            current = current["next"]
        else: 
            break
    return sublist