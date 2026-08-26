def listeyi_parcala(liste: list, boyut: int) -> list:
    return [liste[i:i + boyut] for i in range(0, len(liste), boyut)]