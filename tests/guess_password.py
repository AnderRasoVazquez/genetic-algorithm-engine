import datetime
import unittest
from genetic.genetic import get_best


class GuessPasswordTests(unittest.TestCase):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def get_fitness(self, genes, target):
        """The only feedback the engine needs to evaluate the genes."""
        return sum(1 for expected, actual in zip(target, genes) if expected == actual)

    def display(self, genes, target, start_time):
        """Show output."""
        time_diff = datetime.datetime.now() - start_time
        fitness = self.get_fitness(genes, target)
        print("{0}\t{1}\t{2}".format(genes, fitness, str(time_diff)))

    def guess_password(self, target):
        start_time = datetime.datetime.now()

        def fn_get_fitness(genes):
            return self.get_fitness(genes, target)

        def fn_display(genes):
            self.display(genes, target, start_time)

        optimal_fitness = len(target)
        get_best(fn_get_fitness, len(target), optimal_fitness, self.gene_set, fn_display)

    def test_hello_world(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_for_i_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)


if __name__ == '__main__':
    unittest.main()
