def mera_khud_ka_for_loop(iterable):
    iterator = iter(iterable)

    while True:

        try:
            print(next(iterator))
        except StopIteration:
            break


list1 = [1, 2, 3, 4, 5]
dict1 = {'a': 1, 'b': 2, 'c': 3}
set1 = {1, 2, 3, 4, 5}
tuple1 = (1, 2, 3, 4, 5)
mera_khud_ka_for_loop(tuple1)