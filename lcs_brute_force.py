def lcs_brute_force(X, Y):
    """
    Restituisce la lunghezza della più lunga sottosequenza comune tra X e Y,
    utilizzando l'algoritmo BRUTE-FORCE.
    """
    # genera tutte le possibili sottosequenze di X e Y
    X_subs = generate_subsequences(X)
    Y_subs = generate_subsequences(Y)

    # trova la più lunga sottosequenza comune tra le sottosequenze generate
    max_length = 0
    for X_sub in X_subs:
        for Y_sub in Y_subs:
            if X_sub == Y_sub:
                max_length = max(max_length, len(X_sub))
    return max_length

def generate_subsequences(string):
    """
    Restituisce tutte le possibili sottosequenze di una stringa.
    """
    n = len(string)
    subs = set()
    for i in range(2 ** n):
        sub = ""
        for j in range(n):
            if (i >> j) & 1:
                sub += string[j]
        subs.add(sub)
    return subs