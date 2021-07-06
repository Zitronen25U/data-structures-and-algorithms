import pytest
from graph.graph import Graph, Vertex, Edge
from graph_business_trip.graph import business_trip

def test_get_neighbors():
    g = Graph()