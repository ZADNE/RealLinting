#!/usr/bin/env python
# Author: Tomas Dubsky

import os, sys, subprocess, multiprocessing, json, functools

# Runs clang-tidy on one entry
def run_one_entry(clang_tidy_filepath, output_filepath, entry):
    filepath = entry['file']
    print("Checking: " + filepath, flush=True)
    command = entry['command']
    proc = subprocess.Popen(f'{clang_tidy_filepath} --quiet {filepath} -- {command} 2>/dev/null | tee -a {output_filepath}', shell=True)
    proc.wait()

if __name__ == '__main__':
    multiprocessing.freeze_support()

    # Get arguments
    clang_tidy_filepath = sys.argv[1]
    json_filepath = sys.argv[2]
    output_filepath = sys.argv[3]

    # Create output file
    open(output_filepath, 'w').close()

    # Parse JSON to dict
    json = json.load(open(json_filepath))

    # Check files
    pool = multiprocessing.Pool(4)
    jub_func = functools.partial(run_one_entry, clang_tidy_filepath, output_filepath)
    pool.map(jub_func, json)
    pool.close()
    pool.join()
