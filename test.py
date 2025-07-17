
import unittest
import pandas as pd
from assignment import manipulate_data

class TestDataManipulation(unittest.TestCase):
    def test_manipulate_data(self):
        # Create a sample dataframe
        data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                'Age': [25, 35, 45, 28]}
        df = pd.DataFrame(data)

        result_df = manipulate_data(df)

        # Check the shape of the output
        self.assertEqual(result_df.shape, (2, 3))

        # Check the column names
        self.assertListEqual(list(result_df.columns), ['Name', 'Age', 'Age_in_Months'])

        # Check the filtering
        self.assertTrue((result_df['Age'] > 30).all())

if __name__ == '__main__':
    unittest.main()
