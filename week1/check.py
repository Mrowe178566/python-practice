# check.py — run this after every change to see if your functions work.
#   python3 week1/check.py
import re, os

HERE = os.path.dirname(__file__)
_cache = {}

def module(filename):
    if filename in _cache:
        return _cache[filename]
    path = os.path.join(HERE, filename)
    ns = {}
    if os.path.exists(path):
        src = re.sub(r'(?m)^\s*main\(\)\s*$', '', open(path).read())
        try:
            exec(src, ns)
        except Exception as e:
            print(f'  {filename} could not run: {type(e).__name__}: {e}')
    _cache[filename] = ns
    return ns

def check(filename, func_name, cases):
    func = module(filename).get(func_name)
    print(f'\n{func_name}')
    if func is None:
        print('  not written yet')
        return 0, len(cases)
    passed = 0
    for args, expected in cases:
        try:
            got = func(*args)
        except Exception as e:
            print(f'  ERROR  {func_name}{args!r} raised {type(e).__name__}: {e}')
            continue
        # True == 1 and "7" != 7 in Python, so for bools and strings we also
        # require the TYPE to match. That way returning 1 instead of True,
        # or 7 instead of "7", shows up as a FAIL instead of slipping by.
        ok = got == expected
        if isinstance(expected, (bool, str)):
            ok = ok and type(got) == type(expected)
        passed += ok
        print(f'  {"PASS" if ok else "FAIL"}  {func_name}{args!r} -> {got!r}   expected {expected!r}')
    return passed, len(cases)

TESTS = [
    # ---- 21 to 25: basics.py ----
    ('basics.py', 'is_positive', [((5,), True), ((-5,), False), ((0,), False)]),
    ('basics.py', 'is_even',     [((4,), True), ((7,), False)]),
    ('basics.py', 'bigger',      [((3, 7), 7), ((10, 2), 10)]),
    ('basics.py', 'is_adult',    [((18,), True), ((17,), False)]),
    ('basics.py', 'sign',        [((5,), 'positive'), ((-5,), 'negative'), ((0,), 'zero')]),

    # ---- 26 to 30: ranges.py ----
    ('ranges.py', 'letter_grade',  [((95,), 'A'), ((85,), 'B'), ((75,), 'C'), ((65,), 'D'), ((50,), 'F')]),
    ('ranges.py', 'is_passing',    [((60,), True), ((59,), False)]),
    ('ranges.py', 'classify_temp', [((20,), 'freezing'), ((45,), 'cold'), ((70,), 'warm'), ((95,), 'hot')]),
    ('ranges.py', 'is_between',    [((5, 1, 10), True), ((15, 1, 10), False), ((1, 1, 10), True)]),
    ('ranges.py', 'bmi_category',  [((17,), 'underweight'), ((22,), 'normal'), ((27,), 'overweight'), ((32,), 'obese')]),

    # ---- 31 to 35: logic.py ----
    ('logic.py', 'can_vote',     [((18, True), True), ((17, True), False), ((30, False), False)]),
    ('logic.py', 'is_weekend',   [(('saturday',), True), (('Sunday',), True), (('monday',), False)]),
    ('logic.py', 'same_sign',    [((3, 5), True), ((-2, -8), True), ((3, -5), False)]),
    ('logic.py', 'is_leap_year', [((2024,), True), ((1900,), False), ((2000,), True), ((2023,), False)]),
    ('logic.py', 'fizzbuzz',     [((3,), 'Fizz'), ((5,), 'Buzz'), ((15,), 'FizzBuzz'), ((7,), '7')]),

    # ---- 36 to 40: apply.py ----
    ('apply.py', 'shipping_cost',   [((60,), 0), ((30,), 5.99)]),
    ('apply.py', 'ticket_price',    [((8,), 8), ((30,), 15), ((70,), 10)]),
    ('apply.py', 'discount',        [((100, True), 90.0), ((100, False), 100)]),
    ('apply.py', 'parking_fee',     [((1,), 0), ((2,), 3), ((4,), 9)]),
    ('apply.py', 'describe_number', [((4,), 'even and positive'), ((-3,), 'odd and negative'),
                                     ((-8,), 'even and negative'), ((0,), 'zero')]),
]

total_passed = total_cases = 0
for filename, func_name, cases in TESTS:
    p, n = check(filename, func_name, cases)
    total_passed += p
    total_cases += n

print(f'\n{"="*46}\n  {total_passed} of {total_cases} passing\n{"="*46}')
