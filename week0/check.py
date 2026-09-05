# check.py — run this after every change to see if your functions work.
#   python3 week0/check.py
#
# It imports your functions and calls them with known inputs, so you never have
# to retype a name at the input() prompt just to test something.
import re, os

HERE = os.path.dirname(__file__)
_cache = {}

def module(filename):
    """Run one practice file once, without triggering its main()."""
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
        ok = got == expected
        passed += ok
        print(f'  {"PASS" if ok else "FAIL"}  {func_name}{args!r} -> {got!r}   expected {expected!r}')
    return passed, len(cases)

TESTS = [
    # ---- problems 1 to 5 ----
    ('initials.py', 'initials', [
        (('maia rowe',),    'M.R.'),
        (('ada lovelace',), 'A.L.'),
        (('grace hopper',), 'G.H.'),
    ]),
    ('temperature.py', 'celsius_to_fahrenheit', [
        ((100,), 212.0),
        ((0,),    32.0),
        ((37,),   98.6),
    ]),
    ('receipt.py', 'receipt', [
        (('Coffee', 4.50, 3), '3x Coffee = $13.50'),
        (('Bagel',  2.25, 2), '2x Bagel = $4.50'),
    ]),

    # ---- problems 6 to 10: numbers.py ----
    ('numbers.py', 'double', [
        ((5,),   10),
        ((2.5,), 5.0),
    ]),
    ('numbers.py', 'area_of_rectangle', [
        ((4, 5),   20),
        ((2.5, 4), 10.0),
    ]),
    ('numbers.py', 'seconds_to_minutes', [
        ((90,),  1.5),
        ((120,), 2.0),
    ]),
    ('numbers.py', 'average', [
        ((3, 4, 5),   4.0),
        ((10, 20, 0), 10.0),
    ]),
    ('numbers.py', 'percent_of', [
        ((25, 200), 12.5),
        ((50, 50),  100.0),
    ]),

    # ---- problems 11 to 15: strings.py ----
    ('strings.py', 'full_name', [
        (('maia', 'rowe'),    'Maia Rowe'),
        (('ada', 'lovelace'), 'Ada Lovelace'),
    ]),
    ('strings.py', 'last_word', [
        (('the quick brown fox',), 'fox'),
        (('hello world',),         'world'),
    ]),
    ('strings.py', 'first_and_last', [
        (('python',), 'pn'),
        (('maia',),   'ma'),
    ]),
    ('strings.py', 'username', [
        (('maia@example.com',), 'maia'),
        (('hello@gmail.com',),  'hello'),
    ]),
    ('strings.py', 'word_count', [
        (('the quick brown fox',), 4),
        (('hello world',),         2),
    ]),

    # ---- problems 16 to 20: combine.py ----
    ('combine.py', 'shout', [
        (('hello',),    'HELLO!'),
        (('i did it',), 'I DID IT!'),
    ]),
    ('combine.py', 'initials_three', [
        (('mary jane smith',),    'M.J.S.'),
        (('ada byron lovelace',), 'A.B.L.'),
    ]),
    ('combine.py', 'reverse_name', [
        (('maia rowe',),    'Rowe, Maia'),
        (('ada lovelace',), 'Lovelace, Ada'),
    ]),
    ('combine.py', 'price_with_tax', [
        ((100, 0.0875), '$108.75'),
        ((20, 0.10),    '$22.00'),
    ]),
    ('combine.py', 'format_phone', [
        (('3125551234',), '(312) 555-1234'),
        (('8005551212',), '(800) 555-1212'),
    ]),
]

total_passed = total_cases = 0
for filename, func_name, cases in TESTS:
    p, n = check(filename, func_name, cases)
    total_passed += p
    total_cases += n

print(f'\n{"="*46}\n  {total_passed} of {total_cases} passing\n{"="*46}')
