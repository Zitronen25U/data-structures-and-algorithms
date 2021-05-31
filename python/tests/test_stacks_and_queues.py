



def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expectd = "apple"
    assert actual == expectd
