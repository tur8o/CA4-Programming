#attach_csv function breaks the testing, NameError: commits not defined
import unittest

from simple_RF import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python_RF.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['Author'])
        self.assertEqual('r1551925', commits[0]['Revision'])
        self.assertEqual('1', commits[0]['Number_of_lines'])
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', commits[0]['Date'])

if __name__ == '__main__':
    unittest.main()
