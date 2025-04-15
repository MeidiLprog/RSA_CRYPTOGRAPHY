# RSA_CRYPTOGRAPHY

# Implémentation complète de RSA en Python avec interface Tkinter

Ce projet propose une **implémentation pédagogique de l'algorithme RSA**, incluant :

- Génération de clés RSA (publiques/privées)
- Chiffrement et déchiffrement de texte avec gestion fine des blocs
- Encodage/Conversion de texte vers entiers et inversement
- Déchiffrement optimisé via le **théorème des restes chinois**
- Interface utilisateur interactive via **Tkinter**
- Hashage de fichiers et signature numérique avec vérification

---

## Structure du projet

| Fichier | Description |
|--------|-------------|
| `test.py` | Interface graphique (Tkinter) complète avec toutes les fonctionnalités : génération de clé, chiffrement, déchiffrement |
| `chiffrement.py` | Fonctions RSA principales : chiffrement, déchiffrement standard et avec restes chinois |
| `fonctions.py` | Fonctions mathématiques fondamentales : exposant modulaire, PGCD, Bézout, primalité, génération de clé, factorisation |
| `hash.py` | Hashage de fichiers avec `SHA-256`, signature numérique RSA et vérification |
| `p1.py` | Définition de l’alphabet utilisé et des dictionnaires de conversion (`char` ↔ `int`) |
| `test.txt` | Exemple de fichier utilisé pour la signature (si applicable) |

---

## Fonctionnalités détaillées

### Génération de clés RSA
- Taille configurable en bits (jusqu'à 2048)
- Clés `(e, n)` et `(d, n)` générées dynamiquement
- Calcul de `p`, `q`, `phi(n)`, `d` via Bézout

### Chiffrement et déchiffrement
- Texte converti en blocs numériques selon la taille du module
- Gestion complète du **codage / décodage par blocs**
- Reconversion exacte du message sans tricher (padding implicite géré)
- Déchiffrement optimisé avec le **théorème des restes chinois**

### Signature numérique (hash.py)
- Hash SHA-256 d’un fichier texte
- Signature via clé privée
- Vérification via clé publique

---

## Interface graphique Tkinter
- Entrée de la taille de clé RSA
- Zone pour taper le message à chiffrer
- Bouton de génération, chiffrement, déchiffrement
- Affichage des clefs, temps d'exécution, et résultat chiffré/déchiffré

![image_alt](https://github.com/MeidiLprog/RSA_CRYPTOGRAPHY/blob/main/GUI.png?raw=true)

---

## Exigences

- Python 3.7+
- Aucun package externe requis (`hashlib` et `tkinter` sont standards)

---

## Exécution

```bash
python3 test.py
