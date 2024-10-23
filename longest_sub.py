import random
import time
import os
from Bio.Seq import Seq
from concurrent.futures import ProcessPoolExecutor
from seq_longest_contiguous import longest_contiguous
from seq_all_longest import all_longest


def generate_random_test_data(num_seq=100_000, seq_length=1000):
    """
    Generate a large amount of example data to test the above functions.

    Args:
        num_seq (int): The number of sequnces to return.
        seq_length (int): The length of each individual sequence.
    """
    
    sequences = []
    
    for i in range(num_seq):
        
        sequences.append(Seq("".join(random.choices(["g", "a", "t", "c"], k=seq_length))))
        
    return sequences


def run_large_test_serial(sequences):
    """
    Run through a list of provided sequences in series and return the result.
    """
    
    longest_each_sequence = []
    
    for seq in sequences:
    
        longest_each_sequence.append(longest_contiguous(seq))

    answer = all_longest(longest_each_sequence)

    return answer


def run_large_test_parallel(sequences):
    """
    Run through a list of provided sequences in parallel and return the result.
    """
    
    with ProcessPoolExecutor(max_workers = os.cpu_count()) as pool:
        
        results = pool.map(longest_contiguous, sequences, chunksize=10)
        
        answer = all_longest(results)
    
    return answer


if __name__ == "__main__":
    print("Generating test squences")
    sequences = generate_random_test_data()

    print("Running serial test")
    start = time.perf_counter()  
    answer1 = run_large_test_serial(sequences)  
    duration_seconds = time.perf_counter() - start  
    print(f"Serial: {duration_seconds:.2f} seconds - {answer1}")

    print("Running parallel test")
    start = time.perf_counter()
    answer2 = run_large_test_parallel(sequences) 
    duration_seconds = time.perf_counter() - start
    print(f"Parallel: {duration_seconds:.2f} seconds - {answer2}")
