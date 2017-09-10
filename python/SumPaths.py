#!/usr/bin/env python

import unittest

class TestSumPaths(unittest.TestCase):

  def testSanity(self):
    n1 = Node(value=1)
    self.assertEqual(n1.sumPaths(), 1)
    n2 = Node(value=2)
    n3 = Node(value=3)
    n4 = Node(value=4)
    n5 = Node(value=5)
    n6 = Node(value=6)
    n7 = Node(value=7)
    n1.left = n2
    self.assertEqual(n1.sumPaths(), 12)
    n1.right = n3
    self.assertEqual(n1.sumPaths(), 25)
    n2.left = n4
    self.assertEqual(n1.sumPaths(), 137)
    n2.right = n5
    self.assertEqual(n1.sumPaths(), 262)
    n3.left = n6
    self.assertEqual(n1.sumPaths(), 385)
    n3.right = n7
    self.assertEqual(n1.sumPaths(), 522)

  # Write some more test cases

def sumPathsHelper(root, val):
  if root is None:                   
    return 0     

  val = val*10 + root.value

  if root.left is None and root.right is None:
    return val

  return (sumPathsHelper(root.left, val) + sumPathsHelper(root.right, val))

class Node:
  def __init__(self, value=0, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value


  def sumPaths(self):
    if self is None:     #This case is unnecessary, as we wouldn't be able to call the function on a ull tree.
      return -1
    return sumPathsHelper(self, 0)



if __name__ == "__main__":
  unittest.main()
