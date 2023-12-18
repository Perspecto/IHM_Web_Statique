def rectangle(nbr_longueur,nbr_largeur):
    print('#'*nbr_longueur)
    for _ in range(nbr_largeur-2):
        print(f"#{' '*(nbr_longueur-2)}#")
    print('#'*nbr_longueur)

rectangle(6,9)
