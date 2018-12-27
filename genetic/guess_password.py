import datetime
import genetic


def get_fitness(genes, target):
    """The only feedback the engine needs to evaluate the genes."""
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


def display(genes, target, start_time):
    """Show output."""
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(time_diff)))


def guess_password(target):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    start_time = datetime.datetime.now()

    def fn_get_fitness(genes):
        return get_fitness(genes, target)

    def fn_display(genes):
        display(genes, target, start_time)

    optimal_fitness = len(target)
    genetic.get_best(fn_get_fitness, len(target), optimal_fitness, gene_set, fn_display)


def test_hello_world():
    target = "Hello World!"
    guess_password(target)


if __name__ == '__main__':
    test_hello_world()
