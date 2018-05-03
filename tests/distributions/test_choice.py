import random
import unittest
from autoopt.distributions import WeightedChoice, Choice


class WeightedChoiceTestCase(unittest.TestCase):

    @staticmethod
    def _create_choices():
        choices = set()
        for i in range(random.randint(1, 10)):
            choices.add("".join([chr(random.randint(ord("A"), ord("Z"))) for _ in range(5)]))
        return {c: random.randint(1, 100) for c in choices}

    def setUp(self):
        self.choices = self._create_choices()
        self.dist = WeightedChoice(parameter_name="test", choices=self.choices)

    def test_choice(self):
        for name, weight in self.choices.items():
            self.assertIn(name, self.dist.choices)
            self.assertEqual(self.dist.choices[name], weight)

    def test_pdf(self):
        weight_sum = sum(self.choices.values())
        prob_choices = map(lambda c: (c[0], c[1] / weight_sum), self.choices.items())
        for name, prob in prob_choices:
            self.assertEqual(self.dist.pdf(name), prob)

    def test_pdf_not_in(self):
        self.assertEqual(self.dist.pdf("__not_in_set__"), 0.0)

    def test_plot(self):
        try:
            import matplotlib
            matplotlib.use("AGG")
            from matplotlib import pyplot as plt
            plt.ioff()
            plot = self.dist.plot()
            self.assertIsInstance(plot, plt.figure().__class__)
        except ImportError:
            self.assertIsNone(plot)


class ChoiceTestCase(unittest.TestCase):

    def test_choice(self):
        choices = ["a", "b", "c"]
        dist = Choice(parameter_name="test", choices=choices)
        for name in choices:
            self.assertIn(name, dist.choices)

    def test_single_choice(self):
        choice = "fuu"
        dist = Choice(parameter_name="test", choices=choice)
        self.assertIn(choice, dist.choices)
        self.assertEqual(len(dist.choices), 1)