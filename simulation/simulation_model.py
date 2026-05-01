import random

def stochastic_delay(base, noise=0.2):
    return max(1, int(base + random.uniform(-noise, noise) * base))
