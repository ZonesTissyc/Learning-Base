def gc_count(str1):
    A = str1.count("A")
    C = str1.count("C")
    G = str1.count("G")
    T = str1.count("T")
    gc_rate = (G+C) / (A+C+G+T)
    return gc_rate