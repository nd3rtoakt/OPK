from linkedlists import SList, length, prepend, get, remove, append, get_last, find, remove_first, remove_all, copy, concat, foreach, find_custom

def test_length():
    assert length(None) == 0
    lst = None
    lst = prepend(lst, 1)
    assert length(lst) == 1
    lst = prepend(lst, 2)
    assert length(lst) == 2

def test_prepend():
    lst = None
    lst = prepend(lst, "a")
    assert get(lst, 0) == "a"
    lst = prepend(lst, "b")
    assert get(lst, 0) == "b"
    assert get(lst, 1) == "a"

def test_get():
    lst = None
    lst = prepend(lst, 10)
    lst = prepend(lst, 20)
    assert get(lst, 0) == 20
    assert get(lst, 1) == 10

def test_remove():
    lst = None
    lst = prepend(lst, "x")
    lst = prepend(lst, "y")
    data, lst = remove(lst, 0)
    assert data == "y"
    assert length(lst) == 1
    data, lst = remove(lst, 0)
    assert data == "x"
    assert lst == None

def test_append():
    lst = None
    lst = append(lst, "a")
    assert get(lst, 0) == "a"
    lst = append(lst, "b")
    assert get(lst, 0) == "a"
    assert get(lst, 1) == "b"

def test_get_last():
    lst = None
    lst = append(lst, 1)
    assert get_last(lst) == 1
    lst = append(lst, 2)
    assert get_last(lst) == 2

def test_find():
    lst = None
    lst = append(lst, "a")
    lst = append(lst, "b")
    lst = append(lst, "c")
    assert find(lst, "b") == 1
    assert find(lst, "x") == -1

def test_remove_first():
    lst = None
    lst = append(lst, 1)
    lst = append(lst, 2)
    lst = append(lst, 1)
    lst = remove_first(lst, 1)
    assert get(lst, 0) == 2
    assert get(lst, 1) == 1

def test_remove_all():
    lst = None
    lst = append(lst, 1)
    lst = append(lst, 2)
    lst = append(lst, 1)
    lst = remove_all(lst, 1)
    assert length(lst) == 1
    assert get(lst, 0) == 2

def test_copy():
    lst = None
    lst = append(lst, "a")
    lst_copy = copy(lst)
    assert get(lst_copy, 0) == "a"
    lst = append(lst, "b")
    assert length(lst_copy) == 1

def test_concat():
    lst1 = None
    lst1 = append(lst1, 1)
    lst2 = None
    lst2 = append(lst2, 2)
    lst3 = concat(lst1, lst2)
    assert length(lst3) == 2
    assert get(lst3, 0) == 1
    assert get(lst3, 1) == 2

def test_foreach():
    lst = None
    lst = append(lst, 1)
    lst = append(lst, 2)
    collected = []
    def append_collected(x):
        collected.append(x)
    foreach(lst, append_collected)
    assert collected == [1, 2]

def test_find_custom():
    lst = None
    lst = append(lst, 6)
    lst = append(lst, 10)
    def multiple_5(x):
        return x % 5 == 0
    value, index = find_custom(lst, multiple_5)
    assert value == 10
    assert index == 1
    lst = None
    lst = append(lst, 6)
    lst = append(lst, 10)
    def multiple_7(x):
        return x % 7 == 0
    value, index = find_custom(lst, multiple_7)
    assert value == None
    assert index == -1

test_length()
test_prepend()
test_get()
test_remove()
test_append()
test_get_last()
test_find()
test_remove_first()
test_remove_all()
test_copy()
test_concat()
test_foreach()
test_find_custom()