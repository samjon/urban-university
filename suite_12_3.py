import unittest

# Импортируем классы тестов
from module_12_2 import TournamentTest, Runner, Tournament
from module_12_1 import RunnerTest

def skip_if_frozen(test_method):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_walk(self):
        self.runner1.walk()  # После одного walk дистанция должна быть равна скорости (10)
        self.assertEqual(self.runner1.distance, 10)  # Ожидаем 10

    @skip_if_frozen
    def test_run(self):
        self.runner1.run()  # После одного run дистанция должна быть равна скорости * 2 (20)
        self.assertEqual(self.runner1.distance, 20)  # Ожидаем 20

    @skip_if_frozen
    def test_challenge(self):
        # Проверяем неравенство между двумя бегунами
        self.assertNotEqual(self.runner1, self.runner2)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        # Проверяем что последний финишер - Ник
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        # Проверяем что последний финишер - Ник
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        # Проверяем что последний финишер - Ник
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)