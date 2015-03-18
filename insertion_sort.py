def sort(list):
    '''Insertion Sort on a list'''
    for i in xrange(1, len(list)):
        x = list[i]
        j = i
        while j > 0 and list[j - 1] > x:
            list[j] = list[j - 1]
            j -= 1
        list[j] = x


