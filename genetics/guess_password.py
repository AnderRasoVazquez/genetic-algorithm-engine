import random
import datetime

# genes to use for building guesses
geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"



def generate_parent(length):
    """Generate a random string (with no duplicates) from the gene set."""
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)


def get_fitness(guess):
    """The only feedback the engine needs to evaluate the guess."""
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)


def mutate(parent):
    """Mutate one letter from parent."""
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return "".join(childGenes)


def display(guess, startTime):
    """Show output."""
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))


def main():
    random.seed()
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent, startTime)

    while True:
        child = mutate(bestParent)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child, startTime)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child


if __name__ == '__main__':
    main()
