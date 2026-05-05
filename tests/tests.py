import types

# imports for testing
from classes.caesar_cipher import CaesarCipher

def add_test(tests, func, expected_output=None, *args):
    """
    Adds test in correct format to some test list.
    :param tests: list of tests set as test dir
    :param func: func or method to test
    :param expected_output: expected output
    :param args: list of arguments to be passed into func
    :return:
    """
    if type(func) != types.FunctionType and type(func) != types.MethodType:
        print("failed to add function")
        return

    partial_func = {
        "func": func,
        "args": args,
        "expected_output": expected_output
    }
    tests.append(partial_func)

def run_tests(tests):
    """
    Runs tests and displays results
    :param tests:
    :return:
    """
    tests_ran = 0
    tests_passed = 0

    for partial_fn in tests:
        tests_ran += 1

        func = partial_fn.get("func")
        args = partial_fn.get("args")
        out = partial_fn.get("expected_output")

        try:
            res = func(*args)
            success = res == out
            if success:
                tests_passed += 1
                print("passed test: {0}{1} -> {2} == {3}".format(func.__name__, args, res, out))
            else:
                print("failed test: {0}{1} -> {2} != {3}".format(func.__name__, args, res, out))
        except Exception as err:
            print("errored test: {0} -> {1}".format(func.__name__, err))

    print("{0}/{1} TESTS PASSED!".format(tests_passed, tests_ran))

def main():
    """
    Setup and execution of tests.
    :return:
    """
    tests = []

    # caser-cipher tests
    caser = CaesarCipher(5)
    add_test(tests, caser.encode, "fgh CDE!", "abc XYZ!")
    add_test(tests, caser.decode, "abc XYZ!", "fgh CDE!")


    run_tests(tests)
    pass

if __name__ == "__main__":
    main()
