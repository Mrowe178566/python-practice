# check.py — run this after every change to see if your functions work.
#   python3 week0/check.py
#
# It imports your functions and calls them with known inputs, so you never have
# to retype a name at the input() prompt just to test something.
import re, os

HERE = os.path.dirname(__file__)

def load(filename, func_name):
    """Import one function from a practice file without running its main()."""
    path = os.path.join(HERE, filename)
    if not os.path.exists(path):
        return None
    src = re.sub(r'(?m)^\s*main\(\)\s*$', '', open(path).read())
    ns = {}
    try:
        exec(src, ns)
    except Exception as e:
        print(f'  {filename} could not run: {type(e).__name__}: {e}')
        return None
    return ns.get(func_name)

def check(label, func, cases):
    print(f'\n{label}')
    if func is None:
        print('  not written yet')
        return
    for args, expected in cases:
        try:
            got = func(*args)
        except Exception as e:
            print(f'  ERROR {label}{args} raised {type(e).__name__}: {e}')
            continue
        mark = 'PASS' if got == expected else 'FAIL'
        print(f'  {mark}  {label}{args!r} -> {got!r}   expected {expected!r}')

check('initials', load('initials.py', 'initials'), [
    (('maia rowe',),    'M.R.'),
    (('ada lovelace',), 'A.L.'),
    (('grace hopper',), 'G.H.'),
])

check('celsius_to_fahrenheit', load('temperature.py', 'celsius_to_fahrenheit'), [
    ((100,), 212.0),
    ((0,),    32.0),
    ((37,),   98.6),
])

check('receipt', load('receipt.py', 'receipt'), [
    (('Coffee', 4.50, 3), '3x Coffee = $13.50'),
    (('Bagel',  2.25, 2), '2x Bagel = $4.50'),
])
