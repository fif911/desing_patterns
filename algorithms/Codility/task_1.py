import traceback
from typing import List

import timeit
import cProfile, pstats, io


def profile(fnc):
    """A decorator that uses cProfile to profile a function

    Adapted from the Python 3.6 docs:
    https://docs.python.org/3/library/profile.html#profile.Profile
    """

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


# PERF_TOTAL_CHARS = 30_000

test_set = [
    # ('abccbd', [0, 1, 2, 3, 4, 5], 2),
    # ('aabbcc', [1, 2, 1, 2, 1, 2], 3),
    # ('aaaa', [6, 5, 4, 3], 12),
    # ('aaaa1', [6, 5, 4, 3, 0], 12),
    # ('aaaa2', [3, 4, 5, 6, 0], 12),
    # ('aaaa3', [3, 5, 4, 6, 0], 12),
    # ('aaaa4', [6, 4, 5, 3, 0], 12),
    # ('baaaab', [1, 3, 4, 5, 6, 7], 12),
    # ('abcde', [1, 3, 4, 5, 6], 0),
    # ('a', [1], 0),
    # ('aa', [1, 2], 1),
    # ('aa', [2, 1], 1),
    # ('nnaaaa', [1, 1, 6, 5, 4, 3], 13),
    # ('nnaaaa', [1, 2, 6, 5, 4, 3], 13),
    # ('nnaaaa', [2, 1, 6, 5, 4, 3], 13),
    # ('nnaaaabb', [2, 1, 6, 5, 4, 3, 12, 20], 13 + 12),
    # ('bnnaaaabba', [100, 2, 1, 6, 5, 4, 3, 12, 20, 100], 13 + 12),
    # ('bnnaaaabba', [100, 2, 1, 3, 5, 4, 6, 12, 20, 100], 13 + 12),
    # ('bnnaaaabba', [100, 2, 1, 5, 4, 3, 6, 12, 20, 100], 13 + 12),

    # FOR PERF:
    ('nnaaaa' * 5000, [1, 1, 6, 5, 4, 3] * 5000, 13),  # total chars = 30k
    # ('nnaaaa' + "b" * 29994, [1, 1, 6, 5, 4, 3] + [9] * 29994, 13), # IS THIS CASE TOO MANY min() would be called 29993
    # times which would lead to bottleneck. It's easier to sort array, get min, find min and add sum of all those other

    ('bnnaaaabba' * 3000, [100, 2, 1, 5, 4, 3, 6, 12, 20, 100] * 3000, 13 + 12),
    ('bnvaaaabba' * 3000, [100, 2, 1, 5, 4, 3, 6, 12, 20, 100] * 3000, 13 + 12),
    ('aabbccddee' * 3000, [100, 2, 1, 5, 4, 3, 6, 12, 20, 100] * 3000, 13 + 12),

    # (
    #     'bnnaaaabba' + 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc',
    #     [100, 2, 1, 5, 4, 3, 6, 12, 20, 100] + [100] * 120, 13 + 12),
    # (
    #     'bnnaaaabba' + 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcaaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcbbabcabcabc',
    #     [100, 2, 1, 5, 4, 3, 6, 12, 20, 100] + [100] * 120, 13 + 12),
]


def get_all_subsequent(char, list_of_chars: List[str]) -> int:
    """calculate amount of chars that follow supplied one"""
    amount = 0
    for i in list_of_chars[1:]:
        if char == i:
            amount += 1
        else:
            break
    return amount


def solution(S: List, C: List[int]):
    i = 0  # loop iterator
    total_cost = 0

    # print(f"S: {S}")
    for j in range(len(S) - 1):
        # Terminating condition for i
        if i >= len(S) - 1:
            break

        if S[i] == S[i + 1]:
            # print("Duplicate found !")
            chars_to_delete = get_all_subsequent(S[i], S[i:])
            # decide what to delete
            # if chars_to_delete == 1:
            #     total_cost += min(C[i], C[i + 1])
            # else:
            c_temp = C[i:i + chars_to_delete + 1]  # +1 as i starts with 0
            # print(f"Chars to delete: {chars_to_delete}. Withing costs: {c_temp}")

            # find min cost
            for cd in range(chars_to_delete):
                c_temp_min = min(c_temp)  # get the min available cost
                c_temp_min_pos = c_temp.index(c_temp_min)
                total_cost += c_temp[c_temp_min_pos]
                c_temp.remove(c_temp_min)  # remove this cost option
            i += chars_to_delete  # add amount of deleted chars
        else:
            i += 1
    return total_cost


@profile
def run_perf_test(input1, input2, n):
    time_t = timeit.timeit('solution(t_input1, t_input2)', globals=globals(), number=n)
    return time_t


if __name__ == '__main__':
    PERF = True
    exec_time = 0
    NUMBER_OF_REPETITIONS = 10
    N = len(test_set) * NUMBER_OF_REPETITIONS

    i = 1
    for test_case in test_set:
        print(f"------- Test {i} ---------")
        t_input1 = test_case[0]
        t_input2 = test_case[1]
        expected = test_case[2]

        if PERF:
            # time_t = timeit.timeit('solution(t_input1, t_input2)', globals=globals(), number=NUMBER_OF_REPETITIONS)
            time_t = run_perf_test(t_input1, t_input2, NUMBER_OF_REPETITIONS)
            exec_time += time_t
            print(f"This perf test run average: {time_t / NUMBER_OF_REPETITIONS} for chars {len(t_input1)}")
            i += 1
        else:
            try:
                res = solution(t_input1, t_input2)
            except Exception as e:
                print("Error !")
                print(e)
                traceback.print_exc()
                i += 1
                continue
            try:
                assert res == expected
                print(f"OK test case: {t_input1}; res: {expected}")
            except AssertionError as ae:
                print(f"ERROR: returned {res}; expected {expected}")
                print(res)
            i += 1
    if PERF:
        print(f"\n TOTAL Perf test run average: {exec_time / N}")
