import random


def generate_random_list(size, min_val=0, max_val=1000):
    """Creates a list of random numbers between min_val and max_val"""
    return [random.randint(min_val, max_val) for _ in range(size)]
