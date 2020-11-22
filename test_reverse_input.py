from reverse_input import reverse_dict
import unittest

class TestReverseDict(unittest.TestCase):
    
    def setUp(self):
        self.input_value = {
          'hired': {
            'be': {
              'to': {
                'deserve': 'I'
              }
            }
          }
        }
        
        self.output_value = {
          'I': {
            'deserve': {
              'to': {
                 'be': 'hired'
              }
            }
          }
        }
        
    def test_reverse(self):
        self.assertEqual(reverse_dict(self.input_value), self.output_value)
        
if __name__ == '__main__':
    unittest.main() # pragma: no cover
    
    