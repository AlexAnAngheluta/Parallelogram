def paralellogram(): # alumn@ 4 Alex A
    print("Càlcul de l'àrea i del perímetre d'un paral·lelogram ")
    a = float(input("Costat major a = "))
    b = float(input("Coatat menor b = "))
    h = float(input("Alçada = "))
    area = b * h
    perimetre = 2 * (a + b)
    return area, perimetre
