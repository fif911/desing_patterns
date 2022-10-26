import traceback

test_set = [
    ([1, 2], 3),
    ([1, "Sum"], 3),
    ([1, "Su1m"], 3),
    ([1, 4], 5)
]


def solution(A):
    return sum(A)


if __name__ == '__main__':
    i = 1
    for test_case in test_set:
        print(f"------- Test {i} ---------")
        t_input = test_case[0]
        expected = test_case[1]
        try:
            res = solution(t_input)
        except Exception as e:
            print("Error !")
            print(e)
            traceback.print_exc()
        try:
            assert res == expected
            print("OK")
        except AssertionError as ae:
            print(ae)

        i += 1
