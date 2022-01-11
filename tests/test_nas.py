import unittest
import pandas as pd

from src.data_prep.nas import profile_nulls

class TestNas(unittest.TestCase):

    def test_profile_nulls(self):
      df = pd.DataFrame([{'a': [1,2,3,4]}])
      self.assertEqual(profile_nulls(df), 'No Nulls')

if __name__ == '__main__':
    unittest.main()