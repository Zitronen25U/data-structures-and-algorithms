from python.BinaryTree.tree import Queue
import pytest
from BinaryTree.tree import Node, BinaryTree, BinarySearchTree


# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


# @pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


# @pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


# @pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


# @pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


# @pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree


# @pytest.mark.skip("pending")
def test_binary_search_tree_has_root():
    tree = BinarySearchTree()
    assert tree.root is None


# @pytest.mark.skip("pending")
def test_add_to_empty_bst():
    tree = BinarySearchTree()
    tree.add(5)
    actual = tree.root.value
    expected = 5
    assert actual == expected


# @pytest.mark.skip("pending")
def test_add_to_empty_bst_again():
    tree = BinarySearchTree()
    tree.add(7)
    actual = tree.root.value
    expected = 7
    assert actual == expected


# @pytest.mark.skip("pending")
def test_add_lesser_to_not_empty_bst():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(2)
    actual = tree.root.left.value
    expected = 2
    assert actual == expected


def test_max_value():
    tree = BinarySearchTree
    tree.add(5)
    tree.add(20)
    tree.add(3)
    tree.add(45)
    tree.add(50)
    actual = tree.max()
    expected = 50
    assert actual == expected



# ------------------------------ #
# ------------------------------ #
# ------------------------------ #


# Chal 17

def test_to_enqueue():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    actual = BinaryTree.breadth_first(tree)
    expected = [1,2,3]
    assert actual == expected

def test_is_empty():
    tree = BinaryTree()
    actual = BinaryTree.breadth_first(tree)
    expected = []
    assert actual == expected

def test_que_can_add():
    queue = Queue()
    queue.enqueue("apple")
    actual = queue.peek()
    expected = "apple"
    assert actual == expected

