import timeit


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


def radix_string(s_list, i):
    '''MSD radix sort: suitable for sorting strings
    such as workds or fixed length integer representation.
    Referenced from http://en.wikipedia.org/wiki
    Radix_sort#Example_in_Python'''
    if len(s_list) <= 1:
        return s_list
    divided_bucket = []
    buckets = [[] for x in range(27)]
    for string in s_list:
        if i >= len(string):
            divided_bucket.append(string)
        else:
            buckets[ord(string[i]) - ord('a')].append(string)
    buckets = [radix_string(b, i + 1) for b in buckets]
    return divided_bucket + [b for blist in buckets for b in blist]

if __name__ == '__main__':

    best = [i for i in range(1000)]
    worst = [i for i in range(1000)][::-1]  # reverse

    def best_case():
        return radix_int(best)

    def worst_case():
        return radix_int(worst)

    print "Best Case: {}".format(
        timeit.timeit('best_case()', setup='from __main__ import best_case', number=100))

    print "Worst Case: {}".format(
        timeit.timeit('worst_case()', setup='from __main__ import worst_case', number=100))

    # Best Case: 0.126667976379
    # Worst Case: 0.123579025269