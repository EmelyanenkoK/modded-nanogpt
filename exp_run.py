# we want run subprocess
# in particular python script train_gpt.py
# but with all 16 combinations of flags:
# --canon_a --canon_b --canon_c --canon_d (16 beacuse each can be present or not)
import subprocess
import itertools
import os
def run_experiment(canon_flags):
    command = ["python", "train_gpt.py"] + canon_flags
    print(f"Running command: {' '.join(command)}")
    subprocess.run(command)

def main():
    # Define the flags
    flags = ["--canon_a", "--canon_b", "--canon_c", "--canon_d"]
    
    # Generate all combinations of flags
    all_combinations = []
    for r in range(len(flags) + 1):
        combinations = itertools.combinations(flags, r)
        all_combinations.extend(combinations)
    
    # Run the experiment for each combination
    for combo in all_combinations:
        run_experiment(list(combo))

if __name__ == "__main__":
    main()