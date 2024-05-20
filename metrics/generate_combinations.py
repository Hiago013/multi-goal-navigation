import itertools

class generate_combinations():
    @staticmethod
    def generate_combinations(lengths):
        # Create a list of ranges based on the input lengths
        ranges = [range(length) for length in lengths]
        # Use itertools.product to generate all combinations
        combinations = list(itertools.product(*ranges))
        return combinations

