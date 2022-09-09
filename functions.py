import numpy as np
from math import log as mlog

def bigger_is_better(value, min, max, m=1.0):
    desire = np.zeros_like(value)
    desire[value>=max] = 1.0
    in_threshold= np.argwhere((value>min) & (value<max))
    desire[in_threshold]= (
        (value[in_threshold]-min)
        /(max-min)
    ) ** m
    return desire

def get_bib_m(min, mid, max):
    base = (mid-min)/(max-min)
    return mlog(0.5, base)

def get_bib_mid(min, max, m):
    return (((1/2)**(1/m))*(max-min)) + min


def smaller_is_better(value, min, max, m=1.0):
    desire = np.zeros_like(value)
    desire[value<=min] = 1.0
    in_threshold= np.argwhere((value>min) & (value<max))
    desire[in_threshold]= (
        (value[in_threshold]-max)
        /(min-max)
    ) ** m
    return desire


def get_sib_t(min, mid, max):
    base = (mid-max)/(min-max)
    return mlog(0.5, base)

def get_sib_mid(min, max, t):
    return (((1/2)**(1/t))*(min-max)) + max

def target(value, min, max, target_val, m=1.0, t=1.0):
    desire = np.zeros_like(value)
    desire[value == target_val] = 1.0


    in_threshold = np.argwhere((value > min) & (value < target_val))
    desire[in_threshold] = (
                                   (value[in_threshold] - min)
                                   / (target_val - min)
                           ) ** m

    in_threshold = np.argwhere((value > target_val) & (value < max))
    desire[in_threshold] = (
                                   (value[in_threshold] - max)
                                   / (target_val - max)
                           ) ** t

    return desire
