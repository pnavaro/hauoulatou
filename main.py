from __future__ import print_function
import multiprocessing
import time

__author__ = "Pierre Navaro"
__email__ = "pierre.navaro@univ-rennes1.fr"


# Taken and adapted from
# PythonMultiprocessing_Example1.py by D. Thiebaut
# https://pymotw.com/2/threading/
#
# This python program illustrating how threads can
# be created, started in Python and launch the same R script
# with different input files set through the command line.

import os
import subprocess
import csv




def worker(Id):
    """
    Process worker function.  It receives an Id,
    and prints a message indicating it's starting.
    waits 2.5 seconds,
    set input and output file names from Id
    launch R script
    prints another message, and dies.
    """
    print('Worker %d started\n' % Id)

    input_file = "input_"+str(Id)+".csv"

    #Create the csv file from python

    cwd = os.getcwd() +"/"

    with open(input_file, 'w', newline='') as csvfile:
        fwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(['Processor:']+[str(Id)])
        fwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        fwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    output_file = "output_"+str(Id)+".csv"
    rcmd = ["/usr/bin/Rscript",
                "--vanilla",
                cwd + "read_and_write_csv_file.R",
                "-f", cwd + input_file,
                "-o", cwd + output_file]
    subprocess.call (rcmd)
    print('Worker %d finished\n' % Id)
    return



if __name__ == "__main__":
    """
        Spawns 4 processes that will run the worker function.
        Waits for the threads to finish, then stops.
        """
    
    jobs = []
    for i in range(4):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

    print("Main has spawn all the threads")

    # wait for all the threads to finish
    for p in jobs:
        p.join()

    print("Done!")
