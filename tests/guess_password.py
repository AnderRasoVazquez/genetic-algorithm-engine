import datetime
import unittest
import random
from genetic.genetic import get_best, Benchmark


class GuessPasswordTests(unittest.TestCase):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def get_fitness(self, genes, target):
        """The only feedback the engine needs to evaluate the genes."""
        return sum(1 for expected, actual in zip(target, genes) if expected == actual)

    def display(self, candidate, start_time):
        """Show output."""
        time_diff = datetime.datetime.now() - start_time
        print("{0}\t{1}\t{2}".format(candidate.genes, candidate.fitness, str(time_diff)))

    def guess_password(self, target):
        start_time = datetime.datetime.now()

        def fn_get_fitness(genes):
            return self.get_fitness(genes, target)

        def fn_display(candidate):
            self.display(candidate, start_time)

        optimal_fitness = len(target)
        best = get_best(fn_get_fitness, len(target), optimal_fitness, self.gene_set, fn_display)
        self.assertEqual(best.genes, target)

    @unittest.skip("Not important.")
    def test_hello_world(self):
        target = "Hello World!"
        self.guess_password(target)

    @unittest.skip("Not important.")
    def test_for_i_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    @unittest.skip("Not important.")
    def test_random(self):
        length = 150
        target = ''.join(random.choice(self.gene_set) for _ in range(length))
        self.guess_password(target)

    @unittest.skip("Not important.")
    def test_benchmark(self):
        Benchmark.run(self.test_random)


if __name__ == '__main__':
    unittest.main()
