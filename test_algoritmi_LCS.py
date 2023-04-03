import timeit
import matplotlib.pyplot as plt
import lcs_CUT_ROD
import lcs_brute_force
import lcs_memorization_CUT_ROD
import lcs_bottom_up





def test_algorithms():
    times_bruteforce = []
    times_cutrod = []
    times_memocutrod = []
    times_bottomup = []

    array1 = "GXTXAYB"
    array2 = ["ACG", "CGGC", "CAGIG", "AGGTAB", "DCGAGCT", "CGCGCGCG"]

    for array1 in array2:
        print(f"String 1: " + array1)
        print(f"String 2: {array2}")
        start = timeit.default_timer()
        lcs_cut_rod = lcs_CUT_ROD.lcs_cut_rod(array1, array2)
        end = timeit.default_timer()
        time_cutrod = end - start
        times_cutrod.append(time_cutrod)
        print(f"CUT-ROD LCS: {lcs_cut_rod}")
        print("Tempo di esecuzione CUT_ROD:", end - start)

        start = timeit.default_timer()
        lcs_BRUTE = lcs_brute_force.lcs_brute_force(array1, array2)
        end = timeit.default_timer()
        time_bruteforce = end - start
        times_bruteforce.append(time_bruteforce)
        print(f"BRUTE FORCE LCS: {lcs_BRUTE}")
        print("Tempo di esecuzione FORZA BRUTA: ", end - start)

        start = timeit.default_timer()
        lcs_memoized_cut_rod = lcs_memorization_CUT_ROD.lcs_memoized_cut_rod(array1, array2)
        end = timeit.default_timer()
        time_memocutrod = end - start
        times_memocutrod.append(time_memocutrod)
        print(f"MEMOIZED CUT-ROD LCS: {lcs_memoized_cut_rod}")
        print("Tempo di esecuzione MEMOIZED_CUT_ROD:", end - start)

        start = timeit.default_timer()
        lcs_bottom_up_cut = lcs_bottom_up.lcs_bottom_up_cut_rod(array1, array2)
        end = timeit.default_timer()
        time_bottomup = end - start
        times_bottomup.append(time_bottomup)
        print(f"BOTTOM-UP CUT-ROD LCS: {lcs_bottom_up_cut}")
        print("Tempo di esecuzione BOTTOM_UP_CUT_ROD:", end - start)


    #LUNGHEZZA = [len(str1) + len(str2) for str1, str2 in zip(array1, array2)]
    size = len(array2)
    n1 = []
    for i in range (size):
        n1.append(len(array2[i]))
    plt.plot(n1, times_cutrod, label='CUT-ROD')
    plt.plot(n1, times_bruteforce, label='BRUTE-FORCE')
    plt.plot(n1, times_memocutrod, label='MEMOIZED-CUT-ROD')
    plt.plot(n1, times_bottomup, label='BOTTOM-UP-CUT-ROD')

    # etichette degli assi
    plt.xlabel('Lunghezza stringhe')
    plt.ylabel('Tempo di esecuzione (secondi)')

    # titolo del grafico
    plt.title('Confronto algoritmi per LCS')

    # legenda
    plt.legend()

    # mostra il grafico
    plt.show()


a = test_algorithms()
print(a)