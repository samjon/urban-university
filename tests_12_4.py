import logging
import unittest
from module_12_1 import TestRunner

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='\n%(asctime)s | %(levelname)s | %(name)s | %(message)s')

unittest.main()