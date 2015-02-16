import unittest
from proper_parens import prop_parens


class prop_parens_test(unittest.TestCase):


    def test_balanced(self):
        self.assertTrue(prop_parens('(((())))') == 0)


    def test_open(self):
        self.assertTrue(prop_parens('((((((()') == 1)


    def test_broken(self):
        self.assertTrue(prop_parens('())))') == -1)


    def test_wrong_order(self):
        self.assertTrue(prop_parens('))()((') == -1)


    def test_empty_string(self):
        self.assertTrue(prop_parens('') == 0)


    def test_parens1(self):
        self.assertTrue(prop_parens('(') == 1)


    def test_parens2(self):
        self.assertTrue(prop_parens(')') == -1)


    def test_no_parens(self):
        self.assertTrue(prop_parens('parentheses') == 0)

if __name__ == '__main__':
    unittest.main()