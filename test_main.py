
import unittest
import pandas as pd
from main import app

class TestLocationParsing(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_location_parsing(self):
        # Create test data
        test_data = {
            'Date': ['2024-01-01'],
            'Location': ['California > Eastern Sierra > Mammoth Lakes Area > Clark Canyon > Area 13 > Area 13 - Right Side'],
            'Route': ['Test Route'],
            'Your Stars': [3],
            'Route Type': ['Sport']
        }
        df = pd.DataFrame(test_data)
        
        # Save to temp CSV
        df.to_csv('test.csv', index=False)
        
        # Test the upload endpoint
        with open('test.csv', 'rb') as f:
            response = self.app.post('/upload', data={
                'csvFile': (f, 'test.csv')
            })
            
        self.assertIn(b'Area 13 - Right Side', response.data)
        
    def test_simple_location(self):
        test_data = {
            'Date': ['2024-01-01'],
            'Location': ['Simple Crag'],
            'Route': ['Test Route'],
            'Your Stars': [3],
            'Route Type': ['Sport']
        }
        df = pd.DataFrame(test_data)
        df.to_csv('test.csv', index=False)
        
        with open('test.csv', 'rb') as f:
            response = self.app.post('/upload', data={
                'csvFile': (f, 'test.csv')
            })
            
        self.assertIn(b'Simple Crag', response.data)

if __name__ == '__main__':
    unittest.main()
