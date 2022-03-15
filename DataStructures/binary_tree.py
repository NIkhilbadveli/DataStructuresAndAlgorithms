"""
In general, nodes in trees can have any number of children. However, for binary trees every node has two or fewer
children. The number of children each node has in a tree is called the branching factor, and each node has exactly
one parent. The branching factor for a binary tree is 2.2.


A full binary tree is a binary tree in which each node has exactly zero or two children.

A complete binary tree is a binary tree in which every level, except possibly the
last, is completely filled, and all nodes are as far left as possible.

# Pre-order traversal - A neat trick for pre-order traversals: starting from the root,
go around the tree counterclockwise. Print each node when you pass its left side.
# In-order traversal - A neat trick for in-order traversals: starting from the root,
go around the tree counterclockwise. Print each node when you pass its bottom side.
# Post-order traversal - A neat trick for pre-order traversals: starting from the root,
# go around the tree counterclockwise. Print each node when you pass its right side.

**** Binary Search Trees
balanced - O(log n)
maximally unbalanced - O(n)

*** Tree balancing algos
AVL algorithm - faster lookup times, slower insertion/deletion
Red black tree - slower lookup times, approximately balanced but faster insertion/deletion
"""