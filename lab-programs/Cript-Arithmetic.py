from itertools import permutations

letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for p in permutations(digits, 8):
    S, E, N, D, M, O, R, Y = p

    
    if S == 0 or M == 0:
        continue

    ENSD = 1000*D + 100*E + 10*N + S
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    if ENSD + MORE == MONEY:
        print("Solution Found!\n")
        print(f"S = {S}")
        print(f"E = {E}")
        print(f"N = {N}")
        print(f"D = {D}")
        print(f"M = {M}")
        print(f"O = {O}")
        print(f"R = {R}")
        print(f"Y = {Y}")

        print("\nVerification:")
        print(f" DENS  = {ENSD}")
        print(f" MORE  = {MORE}")
        print("-------")
        print(f" MONEY = {MONEY}")
        break