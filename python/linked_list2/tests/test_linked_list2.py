from linked_list2 import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_kth_from_end():
    list = LinkedList()
    assert list.kth_from_end()
