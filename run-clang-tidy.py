#!/usr/bin/env python

# Author:

import os, sys, subprocess, multiprocessing, json

# Get arguments
clangTidyFilepath = sys.argv[1]
jsonFilepath = sys.argv[2]
outputFilepath = sys.argv[3]

open(outputFilepath, 'w').close()

# Parse JSON to dict
json = json.load(open(jsonFilepath))

# Runs clang-tidy on one entry
def runClangTidy(entry):
    filepath = entry['file']
    print("Checking: " + filepath, flush=True)
    command = entry['command']
    proc = subprocess.Popen(f'{clangTidyFilepath} --quiet {filepath} -- {command} 2>/dev/null | tee -a {outputFilepath}', shell=True)
    proc.wait()

# Check files
pool = multiprocessing.Pool(4)
pool.map(runClangTidy, json)
pool.close()
pool.join()
