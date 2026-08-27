# test_crestgaze.py
"""
Tests for CrestGaze module.
"""

import unittest
from crestgaze import CrestGaze

class TestCrestGaze(unittest.TestCase):
    """Test cases for CrestGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestGaze()
        self.assertIsInstance(instance, CrestGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
