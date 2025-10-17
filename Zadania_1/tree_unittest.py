import unittest
from binary_tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        root = self.tree.addRoot('R')
        A = self.tree.addLeft(root,'A',1)
        B = self.tree.addRight(root,'B',3)
        C = self.tree.addLeft(A,'C',1)
        D = self.tree.addRight(A,'D',1)
        E = self.tree.addLeft(B,'E',3)
        F = self.tree.addRight(B,'F',4)
        G = self.tree.addLeft(E,"G",0)
    def test_checkRoot(self):
        self.assertEqual(self.tree.root.value,'R')
    def test_checkLChild(self):
        self.assertEqual(self.tree.root.left.value,'A')
    def test_checkRChild(self):
        self.assertEqual(self.tree.root.right.value,'B')
    def test_checkRRNode(self):
         self.assertEqual(self.tree.root.right.right.value,'F')
    def test_checkNodeName(self):   
         self.assertIn("-3->B",self.tree.__str__())
    def test_checkRLLNode(self):
         self.assertEqual(self.tree.root.right.left.left.value,'G')
    def test_checkEmptyNode(self):
         self.assertEqual(self.tree.root.left.left.left,None)
    #def test_nodeWeight(self):
     #    self.assertEqual(self.root.)
    

    
if __name__ == "__main__":
        unittest.main()
    