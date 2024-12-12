from runner_and_tournament import Runner, Tournament
import unittest


class TestTournament(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.assertEqual(result[len(result)].name, self.runner3.name, 'Test for last runner - failed!')
        self.assertEqual(result[1].name, self.runner1.name, 'Test for first runner - failed!')
        self.all_results.append(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.assertEqual(result[len(result)].name, self.runner3.name, 'Test for last runner - failed!')
        self.assertEqual(result[1].name, self.runner2.name, 'Test for first runner - failed!')
        self.all_results.append(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        tournament = Tournament(90, self.runner2, self.runner1, self.runner3)
        result = tournament.start()
        self.assertEqual(result[len(result)].name, self.runner3.name, 'Test for last runner - failed!')
        self.assertEqual(result[1].name, self.runner1.name, 'Test for first runner - failed!')
        self.all_results.append(result)


if __name__ == '__main__':
    unittest.main()