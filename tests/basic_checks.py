import unittest
import os
import importlib.util

class TestFalcon7b(unittest.TestCase):

    def test_library_torch_installed(self):
        """ Test if pytorch library is installed """
        torch_installed = importlib.util.find_spec("torch") is not None
        self.assertTrue(torch_installed, "torch is not installed")

    def test_library_pytorch_lightning_installed(self):
        """ Test if pytorch lightning library is installed """
        lightning_installed = importlib.util.find_spec("lightning") is not None
        self.assertTrue(lightning_installed, "pytorch lightning library is not installed")
        
    def test_library_bitsandbytes_installed(self):
        """ Test if bitsandbytes library is installed """
        bitsandbytes_installed = importlib.util.find_spec("bitsandbytes") is not None
        self.assertTrue(bitsandbytes_installed, "bitsandbytes is not installed")

    def test_data_file_exists(self):
        """ Test if the data file exists """
        data_file_path = '/mnt/code/lit-gpt/conversation_data/data.json'
        self.assertTrue(os.path.isfile(data_file_path), "Data file does not exist")

if __name__ == '__main__':
    unittest.main()
