import unittest
import HtmlTestRunner

from Examples import Example


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self) -> None:
        print("This will run after every method")

    def test_add(self):
        result = Example.add(self,10,20)
        self.assertEqual(result,30)

    def test_sub(self):
        result = Example.sub(self, 20,10)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))