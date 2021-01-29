import string
import numpy as np

purse_fname = "./coin_purse.staticum"
n_staticums = 1000000
staticum_length = 1000

charset = string.ascii_letters + string.digits + string.punctuation
n_charset = len(charset)

def make_staticum():
    rands = np.random.randint( n_charset, size=(staticum_length,))
    return "".join([charset[k] for k in rands])

def all_the_way_to_the_bank():
    return "\n".join([make_staticum() for _ in range(n_staticums)])

def main():
    staticums = all_the_way_to_the_bank()
    with open(purse_fname, 'w') as f:
        f.write(staticums)

if __name__ == "__main__":
    main()
