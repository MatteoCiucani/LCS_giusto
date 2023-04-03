def lcs_memoized_cut_rod(X, Y):
    """
    Restituisce la lunghezza della più lunga sottosequenza comune tra X e Y,
    utilizzando l'algoritmo MEMOIZED-CUT-ROD.
    """
    memo = {}
    return lcs_memoized_cut_rod_aux(X, Y, len(X), len(Y), memo)


def lcs_memoized_cut_rod_aux(X, Y, i, j, memo):
    """
    Restituisce la lunghezza della più lunga sottosequenza comune tra X[:i] e Y[:j],
    utilizzando l'algoritmo MEMOIZED-CUT-ROD.
    """
    if (i, j) in memo:
        return memo[(i, j)]
    if i == 0 or j == 0:
        result = 0
    elif X[i-1] == Y[j-1]:
        result = lcs_memoized_cut_rod_aux(X, Y, i-1, j-1, memo) + 1
    else:
        result = max(lcs_memoized_cut_rod_aux(X, Y, i-1, j, memo), lcs_memoized_cut_rod_aux(X, Y, i, j-1, memo))
    memo[(i, j)] = result
    return result