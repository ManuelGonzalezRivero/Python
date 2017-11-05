#!/user/bin/env python

'''
This is a template file to get your project on the road quickly!
Last updated: July 27th, 2017
'''

__author__  = 'Manuel Gonzalez-Rivero'
__email__   = 'mgr2786@gmail.com'
__version__ = '0.0.1'
__status__  = 'development'

# General imports
import argparse
import numpy as np
import os, sys, time, json, re

# Cryptography imports
import hashlib

# Visual Graphing Utilities
import matplotlib.pyplot as plt
plt.ion()

# Debugging Utilities
import ipdb as pdb

# Add other folders to path for easy importing
PWD = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(PWD, 'python')))

def parse_args():
    ''' Parse CLI arguments into an object and a dictionary '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--string_example', '-s', type=str, default='meow',
            help='Shoutout to SimpleFlips')
    parser.add_argument('--flag_example', action='store_true',
            help='This value is true when passed in, otherwise false')
    args = parser.parse_args()
    dargs = vars(args)
    return (args, dargs)

def main():
    args, dargs = parse_args()
    #rest of code goes here!
    print('Cool {}!'.format('project'), flush=True)
    pdb.set_trace()

if __name__=='__main__':
    main()
