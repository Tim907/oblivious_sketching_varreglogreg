from sketching.datasets import Covertype_Sklearn
from sketching.utils import run_experiments

"""
Min_size, max_size and step_size leads to the grid of different sketch sizes used.
Num_runs defines the number of replications. Quantities for the plots are calculated with the median of all replications.
"""

MIN_SIZE = 1000
MAX_SIZE = 20000
STEP_SIZE = 2000
NUM_RUNS = 21

dataset = Covertype_Sklearn(use_caching=False)

run_experiments(
    dataset=dataset,
    min_size=MIN_SIZE,
    max_size=MAX_SIZE,
    step_size=STEP_SIZE,
    num_runs=NUM_RUNS,
    add=False,
    varreg_lambda=0
)
