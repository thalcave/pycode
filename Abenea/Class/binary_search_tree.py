#!/usr/bin/env python

"""
Simple implementation of a Binary search tree
"""

from functools import wraps

class TreeNode():
    """Class defining a tree"""
    def __init__(self, value, left_subtree = None, right_subtree= None):
        self.value = value
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree

    def insert(self, value):
        """Add a child"""
        if self.value == value:
            return

        if self.value > value:
            self.left_subtree = TreeNode(value)
        else:
            self.right_subtree = TreeNode(value)

    def search_value(self, value):
        """Search and return value (None if non-existing)"""
        if self.value == value:
            return value

        if self.value > value:
            if self.left_subtree == None:
                return None
            return self.left_subtree.search_value(value)
        else:
            if self.right_subtree == None:
                return None
            return self.right_subtree.search_value(value)

    def search_insert(self, value):
        """Search for a value; if non-existant, insert it"""
        if self.value == value:
            print "Value already in tree: {0}".format(value)
            return

        if self.value > value:
            if not self.left_subtree:
                print "Value added in left tree: {0}".format(value)
                self.left_subtree = TreeNode(value)
            else:
                self.left_subtree.search_insert(value)
        else:
            if not self.right_subtree:
                print "Value added in right tree: {0}".format(value)
                self.right_subtree = TreeNode(value)
            else:
                self.right_subtree.search_insert(value)

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print "--------------------"
        print "Tree traversal {0}".format(func.__name__)
        ret = func(*args)
        return ret
    return wrapper


def pre_order(tree_node, level):
    """Pre order traversal"""

    if tree_node:
        print "{0} on level {1}".format(tree_node.value, level)
        pre_order(tree_node.left_subtree, level+1)
        pre_order(tree_node.right_subtree, level+1)

def process_node(tree_node, level):
    print "{0} on level {1}".format(tree_node.value, level)

def iterative_pre_order(tree_node):
    """Depth-first (pre-order) traversal"""

    if not tree_node:
        return

    level = 1

    #use list for stack
    parent_stack = []
    while tree_node:
        process_node(tree_node, level)

        if tree_node.right_subtree:
            parent_stack.append((level+1, tree_node.right_subtree))

        if tree_node.left_subtree:
            tree_node = tree_node.left_subtree
            level = level + 1
        else:
            if parent_stack:
                node_tuple = parent_stack.pop()
                tree_node = node_tuple[1]
                level = node_tuple[0]
            else:
                tree_node = None



if __name__ == '__main__':
    bin_tree = TreeNode(10)

    bin_tree.insert(11)
    bin_tree.insert(5)

    found = bin_tree.search_value(11)
    print "search {0} found: {1}".format(11, found)

    found = bin_tree.search_value(5)
    print "search {0} found: {1}".format(5, found)

    found = bin_tree.search_value(100)
    print "search {0} found: {1}".format(100, found)

    bin_tree.search_insert(100)
    found = bin_tree.search_value(100)
    print "search {0} found: {1}".format(100, found)

    bin_tree.search_insert(12)
    bin_tree.search_insert(1200)
    bin_tree.search_insert(1)
    bin_tree.search_insert(8)
    bin_tree.search_insert(14)

    log_func = logging_decorator(pre_order)
    log_func(bin_tree, 1)


    lfunc = logging_decorator(iterative_pre_order)
    lfunc(bin_tree)
