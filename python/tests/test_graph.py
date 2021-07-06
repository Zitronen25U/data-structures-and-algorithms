
from graph.graph import Graph

def test_graph():
    assert Graph

def test_add():
    graph = Graph()
    actual = graph.add_node('Brian lemons')
    expected_value = 'Brian Lemons'
    assert actual.value == expected_value

def test_size():
    graph = Graph()
    graph.add_node('Brian Lemons')
    graph.add_node('Lemons Brian')
    actual = graph.size()
    expected = 2
    assert actual == expected

def test_size_empty():
    graph = Graph()
    actual = graph.size()
    expected = None
    assert actual == expected