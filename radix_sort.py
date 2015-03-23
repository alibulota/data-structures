# from random import random


def radix_int(array, base=10):
    '''LSD radix sort: short keys come before longer keys
    of the smae length are sorted lexicofraphically.
    Referenced from http://en.wikipedia.org/wiki/
    Radix_sort#Example_in_Python'''
    def string_bucket(array, base, iteration):
        buckets = [[] for i in range(base)]
        for number in array:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets

    def bucket_string(buckets):
        array = []
        for bucket in buckets:
            array.extend(bucket)
        return array

    maxval = 0
    for i in array:
        if i > maxval:
            maxval = i

    iterate = 0
    while ((base ** iterate) <= maxval):
        array = bucket_string(string_bucket(array, base, iterate))
        iterate += 1
    return array


def radix_string(s_list):
    '''MSD radix sort: suitable for sorting strings
    such as workds or fixed length integer representation.
    Referenced from http://en.wikipedia.org/wiki
    Radix_sort#Example_in_Python'''
