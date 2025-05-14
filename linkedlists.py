class SList:
    next = None
    pass

def length(lst):
    count = 0
    current = lst
    while current != None:
        count += 1
        current = current.next
    return count

def prepend(lst, data):
    new_node = SList()
    new_node.data = data
    new_node.next = lst
    return new_node

def get(lst, index):
    if index < 0 or lst is None:
        print('ошибка')
        return None
    current = lst
    for i in range(index):
        if current.next is None:
            print('ошибка')
            return None
        current = current.next
    return current.data

def remove(lst, index):
    if index < 0 or lst == None:
        print('список пуст или неверный индекс')

    if index == 0:
        removed_data = lst.data
        new_head = lst.next
        return removed_data, new_head

    current = lst
    for i in range(index - 1):
        if current.next == None:
            print('ошибка')
            return None
        current = current.next

    if current.next == None:
        print('ошибка')
        return None

    removed_data = current.next.data
    current.next = current.next.next
    return removed_data, lst

def append(lst, data):
    new_node = SList()
    new_node.data = data
    new_node.next = None
    if lst == None:
        return new_node
    current = lst
    while current.next != None:
        current = current.next
    current.next = new_node
    return lst

def get_last(lst):
    if lst == None:
        print('пусто')
        return None
    current = lst
    while current.next is not None:
        current = current.next
    return current.data

def find(lst, data):
    index = 0
    current = lst
    while current != None:
        if current.data == data:
            return index
        current = current.next
        index += 1
    return -1

def remove_first(lst, data):
    if lst == None:
        return None
    if lst.data == data:
        return lst.next
    current = lst
    while current.next != None:
        if current.next.data == data:
            current.next = current.next.next
            return lst
        current = current.next
    return lst

def remove_all(lst, data):
    if lst == None:
        return None
    while lst != None and lst.data == data:
        lst = lst.next
    if lst == None:
        return None
    current = lst
    while current.next != None:
        if current.next.data == data:
            current.next = current.next.next
        else:
            current = current.next
    return lst

def copy(lst):
    if lst == None:
        return None
    new_head = SList()
    new_head.data = lst.data
    new_current = new_head
    current = lst.next

    while current != None:
        new_node = SList()
        new_node.data = current.data
        new_current.next = new_node
        new_current = new_current.next
        current = current.next
    return new_head

def concat(lst1, lst2):
    if lst1 == None:
        return copy(lst2)
    new_list = copy(lst1)
    current = new_list
    while current.next != None:
        current = current.next
    current.next = copy(lst2)
    return new_list

def foreach(lst, func):
    current = lst
    while current != None:
        func(current.data)
        current = current.next

def find_custom(lst, predicate):
    index = 0
    current = lst
    while current != None:
        if predicate(current.data):
            return current.data, index
        current = current.next
        index += 1
    return None, -1