from rt_with_exceptions import Runner
import unittest
import logging


class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.runner = Runner(50)
            for i in range(10):
                self.runner.run()
            self.assertEqual(self.runner.distance, 1000, 'Test Runner.run() - failed!')
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверное значение скорости для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.runner = Runner('test', -10)
            for i in range(10):
                self.runner.walk()
            self.assertEqual(self.runner.distance, 100, 'Test Runner.walk() - failed!')
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверное значение скорости для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.runner = Runner('test')
        test_obj2 = Runner('test2')
        for i in range(10):
            self.runner.walk()
            test_obj2.run()
        self.assertNotEqual(self.runner.distance, test_obj2.distance,
                            'Combined test Runner.walk() & Runner.run()- failed!')


if __name__ == '__main__':
    unittest.main()