def sort(list):
    '''Insertion Sort on a list'''
    for i in xrange(1, len(list)):
        x = list[i]
        j = i
        while j > 0 and list[j - 1] > x:
            list[j] = list[j - 1]
            j -= 1
        list[j] = x


if __name__ == '__main__':
    import timeit

    best = [i for i in range(1000)]
    worst = [i for i in range(1000)][::-1]  # reverse

    def best_case():
        return sort(best)

    def worst_case():
        return sort(worst)

    print "Best Case: {}".format(
        timeit.timeit('best_case()', setup='from __main__ import best_case', number=100))

    print "Worst Case: {}".format(
        timeit.timeit('worst_case()', setup='from __main__ import worst_case', number=100))
