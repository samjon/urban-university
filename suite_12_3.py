import unittest
import module_12_1
import module_12_2


test_suite = unittest.TestSuite()

test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.TestRunner))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TestTournament))

runner_test = unittest.TextTestRunner(verbosity=2)
runner_test.run(test_suite)