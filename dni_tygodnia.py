def NrDoDnia(a):
    """Funkcja zwraca dzien tygodnia w str"""
    Dni = [
        "Poniedzialek",
        "Wtorek",
        "Środa",
        "Czwartek",
        "Piątek",
        "Sobota",
        "Niedziela"
    ]
    return Dni[a-1]
def KtoryDzien(a):
    """Podajac dzien miesiaca funkcja zwroci jego dzien tygodnia"""
    if a % 7 == 0:
        return "Poniedzialek"
    if a % 7 == 1:
        return "Wtorek"
    if a % 7 == 2:
        return "Środa"
    if a % 7 == 3:
        return "Czwartek"
    if a % 7 == 4:
        return "Piatek"
    if a % 7 == 5:
        return "Sobota"
    if a % 7 == 6:
        return "Niedziela"