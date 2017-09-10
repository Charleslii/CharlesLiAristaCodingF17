# Arista Coding Question Fall 2017

##Language Used
Python

## The Question
Given a binary tree, sum all of the numbers created by the paths from the root to each leaf.

For example, the tree below has the following paths:

                            1
                          /   \
                         /     \
                        4       5
                       / \
                      3   7
                           \
                            9

1->4->3, which creates the number 143.
1->4->7->9, which creates the number 1479.
1->5, which creates the number 15.

The sum for this tree is 143 + 1479 + 15 = 1637

## What You'll Do
Your job is to implement the function sumPaths, which given a root to a binary tree, will return the sum of all of the paths. Be sure to write additional tests.

You may assume all node values will be between 0 and 9.
Where applicable, return -1 if sumPaths is called on a null tree.

Please implement your solution in C11, Java 8, or Python 2.7 using only the standard library of these languages. There is skeleton code with a simple test case for each of these languages in this repository.

## Solution

The main idea of this solution is to do a preorder traversal of the tree, keeping track of the value and updating it as we go along each branch of the tree.
We use a helper function to keep track of the value of the function as it recurses, and recurse on the left and right of the tree with our helper function. 