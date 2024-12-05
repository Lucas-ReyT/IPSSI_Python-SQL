# Système de gestion de bibliothèque

Ce projet implémente un système de gestion de bibliothèque en Python, en utilisant la programmation orientée objet (OOP). Le système permet aux étudiants d'emprunter et de rendre des livres, de consulter la liste des livres disponibles, de rechercher des livres et de gérer l'état de la bibliothèque de manière persistante.

## Fonctionnalités principales

1. **Gestion des livres** : Ajouter des livres à la bibliothèque, consulter la liste des livres disponibles, rechercher des livres par titre ou auteur.
2. **Emprunt et retour de livres** : Les étudiants peuvent emprunter des livres disponibles et les rendre après lecture. La bibliothèque garde une trace de l'état des livres (emprunté ou disponible).
3. **Limite d'emprunt** : Chaque étudiant peut emprunter un nombre limité de livres (par défaut 3 livres), et il ne peut pas emprunter un livre s'il a atteint cette limite.
4. **Persistance des données** : La bibliothèque sauvegarde l'état des livres dans un fichier et peut recharger les livres depuis ce fichier.
5. **Interface en ligne de commande** : Un menu interactif permet aux utilisateurs de consulter les livres, effectuer des emprunts, retourner des livres, ajouter des livres, et plus encore.

## Prérequis

- Python 3.x

## Structure du projet

- `library_system.py` : Le fichier principal contenant la logique du système de gestion de bibliothèque.
- `library_data.txt` (facultatif) : Un fichier de données pour sauvegarder et charger l'état de la bibliothèque.

## Fonctionnement

### 1. Modélisation des livres

La classe `Book` représente un livre, avec les propriétés suivantes :
- `title` : Titre du livre
- `author` : Auteur du livre
- `is_available` : Indique si le livre est disponible (par défaut à `True`)

### 2. Modélisation de la bibliothèque

La classe `Library` gère la collection de livres. Elle permet d'ajouter des livres, de lister tous les livres et de rechercher des livres par titre ou auteur. Elle permet également de sauvegarder et charger les livres depuis un fichier.

### 3. Modélisation des étudiants

La classe `Student` représente un étudiant qui peut emprunter et rendre des livres. Un étudiant a un attribut `max_borrow_limit` pour définir la limite d'emprunt (par défaut, 3 livres).

### 4. Interface utilisateur

Le système utilise une interface en ligne de commande qui permet à l'utilisateur de :
- Voir la liste des livres disponibles
- Rechercher un livre par titre ou auteur
- Ajouter un nouveau livre
- Emprunter un livre
- Rendre un livre

### 5. Sauvegarde et chargement des livres

Les livres peuvent être sauvegardés dans un fichier pour persister l'état de la bibliothèque. Le fichier `library_data.txt` est utilisé pour stocker les livres sous forme de texte.

### 6. Exemple d'utilisation

```python
# Exemple d'ajout de livres et de gestion de prêts

library = Library()

# Ajout de livres
library.add_book("1984", "George Orwell")
library.add_book("Animal Farm", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

# Création d'un étudiant
student = Student("John Doe", max_borrow_limit=3)

# Emprunt de livres
student.borrow_book("1984", library)
student.borrow_book("Animal Farm", library)
student.borrow_book("To Kill a Mockingbird", library)

# Tentative d'emprunter plus de livres que la limite autorisée
student.borrow_book("The Great Gatsby", library)

# Retourner un livre
student.return_book("1984", library)

7. Commande de menu

Un menu interactif permet à l'utilisateur de choisir parmi les options suivantes :

    Voir tous les livres
    Rechercher un livre
    Ajouter un livre
    Emprunter un livre
    Rendre un livre
    Quitter le programme

$ python library_system.py
--- Menu de gestion de la bibliothèque ---
1. Voir tous les livres
2. Rechercher un livre
3. Ajouter un nouveau livre
4. Emprunter un livre
5. Rendre un livre
6. Quitter
Veuillez choisir une option (1-6):

Fonctionnalités futures (Améliorations possibles)

    Ajouter un système de catégories de livres (fiction, non-fiction, etc.).
    Implémenter un système d'abonnement pour les étudiants.
    Ajouter des notifications pour les livres en retard.

Installation

    Clonez ce repository ou téléchargez les fichiers.

    Assurez-vous d'avoir Python 3 installé sur votre machine.

    Exécutez le fichier principal avec la commande suivante :

    python library_system.py

Contribuer

Si vous souhaitez contribuer à ce projet, vous pouvez soumettre une pull request avec vos modifications.
