# test_ercmetadataparser.py
"""
Tests for ErcMetadataParser module.
"""

import unittest
from ercmetadataparser import ErcMetadataParser

class TestErcMetadataParser(unittest.TestCase):
    """Test cases for ErcMetadataParser class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ErcMetadataParser()
        self.assertIsInstance(instance, ErcMetadataParser)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ErcMetadataParser()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
