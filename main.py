""" Calculate Highest Non-Adjacent-Sums """

test_list = [2, 4, 6, 2, 5]
#test_list = [5, 1, 1, 5]
#test_list = [1, 1, 1, 5]
#test_list = [1, -1, 1, -1, 5]

def r_sum(the_list):
    """ recursive calculation of sum """
    if not the_list:
        return 0
    if len(the_list) == 1:
        return the_list[0]

    return max(the_list[0] + r_sum(the_list[2:]),
               the_list[1] + r_sum(the_list[3:]))

def main():
    """ Main driver """
    print(test_list, r_sum(test_list))


if __name__ == "__main__":
    main()
