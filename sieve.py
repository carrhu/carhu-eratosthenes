# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import sys
import math
import numpy as np


def basic(nmax): 
    all_primes = []
    
    if nmax == 2: 
        all_primes = [2]
    else:
        primes_head = [2]
        first = 3
        primes_tail = np.arange(first,nmax+1,2)
        while first <= round(math.sqrt(primes_tail[-1])):
            first = primes_tail[0]
            primes_head.append(first)
            non_primes = first * primes_tail
            primes_tail = np.array([ n for n in primes_tail[1:]
                                    if n not in non_primes ])
    all_primes = primes_head + primes_tail.tolist()
    return all_primes


def efficient(nmax):
    all_primes = []

    if nmax == 2: 
        all_primes = [2]

    else:
        primes_head = [2]
        first = 3

        # The primes tail will be kept both as a set and as a sorted list
        primes_tail_lst = range(first,nmax+1,2)
        primes_tail_set = set(primes_tail_lst)

        # Now do the actual sieve
        while first <= round(math.sqrt(primes_tail_lst[-1])):
            # Move the first leftover prime from the set to the head list
            first = primes_tail_lst[0]
            primes_tail_set.remove(first)  # remove it from the set
            primes_head.append(first) # and store it in the head list

            # Now, remove from the primes tail all non-primes.  For us to be able
            # to break as soon as a key is not found, it's crucial that the tail
            # list is always sorted.
            for next_candidate in primes_tail_lst:
                try:
                    primes_tail_set.remove(first * next_candidate)
                except KeyError:
                    break

            # Build a new sorted tail list with the leftover keys
            primes_tail_lst = list(primes_tail_set)
            primes_tail_lst.sort()

        all_primes = primes_head + primes_tail_lst
    return all_primes


def get_primes(nmax, model): 
    final_list = [] 
    if model == 'basic': 
        final_list = basic(nmax)
    elif model == 'efficiet': 
        final_list = efficient(nmax)
    return final_list
