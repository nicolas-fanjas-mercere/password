import hashlib

mdp = input("Bon mec pour créer un mot de passe il faut: 8 caractères, 1 Maj, 1 minuscule, 1 chiffre, 1 @ : ")

def verif_taille_maxilmal(mdp):
    if len(mdp) < 8:
        return False
    else:
        return True

def verif_minuscule(mdp):
    for char in mdp:
        if char.minuscule():
            return True
    return False

def verif_majuscule(mdp):
    for char in mdp:
        if char.majuscule():
            return True
    return False

def verif_chiffre(mdp):
    for char in mdp:
        if char.chiffre():
            return True
    return False

def verif_caracetere_spe(mdp):
    speciale_caracetere = "!@#$%^&*"
    for char in mdp:
        if char in speciale_caracetere:
            return True
    return False

def mdp_valide(mdp):
    if verif_taille_maxilmal(mdp) and verif_minuscule(mdp) and verif_majuscule(mdp) and verif_chiffre(mdp) and verif_caracetere_spe(mdp):
        return True
    else:
        return False

while not mdp_valide(mdp):
    print("J'ai dit quoi ? il manque des choses... DONC je me repete ")
    mdp = input("Dcp je me repete 8 caractères, 1 Maj, 1 minuscule, 1 chiffre, 1 @ ")

print("Hmmmm il semblerait que tu sois moins bête que ce que j'imaginais")

# Cryptage du mot de passe(j'ai un doute dessus)
mdp_hache = hashlib.sha256(mdp.encode())
print("Le mot de passe crypté est :", mdp_hache.hexdigest())
