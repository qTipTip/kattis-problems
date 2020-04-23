import sys


def mod_mult(a, b):
    return (a * b) % 1000000007


def mod_add(a, b):
    return (a + b) % 1000000007


def rebound_function_1(S, N, *args):
    return mod_add(S, N)


def rebound_function_2(S, N, pow_2_prev, pow_2, L):
    return mod_add(S,
                   mod_add(
                       mod_mult(N, pow_2),
                       mod_mult(pow_2_prev, L)))


def swap_count(sequence):
    L = 0  # question marks
    N = 0  # ones
    S = 0  # swaps

    pow_2 = 1
    pow_2_prev = 1

    zero_branch_func = rebound_function_1
    for c in sequence:

        if c == 49:
            # Adding a one to the end of the string
            # leaves it in a sorted state, hence no
            # additional swaps occur.
            N += 1

        elif c == 63:
            # Adding a question mark at the end of the string. We need to account for the two cases, 0 and 1.
            #
            S = mod_add(mod_add(S, S), mod_mult(N, pow_2))
            S = mod_add(S, mod_mult(L, pow_2_prev))

            L += 1
            pow_2_prev = pow_2
            pow_2 = mod_add(pow_2, pow_2)
            zero_branch_func = rebound_function_2


        else:
            # Adding a question mark to the end of the string. Two cases, one where no question marks has been seen, and
            # one where question marks has been seen.
            S = zero_branch_func(S, N, pow_2_prev, pow_2, L)

    return S


if __name__ == '__main__':
    sequence = sys.stdin.buffer.read()
    S_mod = swap_count(sequence)
