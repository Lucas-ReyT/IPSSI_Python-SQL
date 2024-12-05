# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:58:29 2024

@author: lucas
"""
#TÂCHE 1 

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True  

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"'{self.title}' by {self.author} - {availability}"



book1 = Book("1984", "George Orwell")
print(book1)  


#TÂCHE 2

class Library:
    def __init__(self):
        self.books = []  
        
    def add_book(self, title: str, author: str):
        new_book = Book(title, author) 
        self.books.append(new_book)  
        
    def list_books(self) -> list:
        return [str(book) for book in self.books]  
 #T^Âche 3   
    def load_books(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line.strip(): 
                        title, author, is_available = line.split(',')
                        is_available = is_available.strip().lower() == 'true'  
                        self.add_book(title.strip(), author.strip())  
                        for book in self.books:
                            if book.title == title.strip() and book.author == author.strip():
                                book.is_available = is_available
            print(f"Les livres ont été chargés depuis '{file_path}'.")
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        except Exception as e:
            print(f"Erreur lors du chargement des livres : {e}")
            
    # Tâche 5 
    """
    def lend_book(self, book_title: str, student: 'Student') -> bool:
        for book in self.books:
            if book.title == book_title and book.is_available:
                book.is_available = False  
                student.borrowed_books.append(book_title)  
                print(f"Le livre '{book_title}' a été prêté à {student.name}.")
                return True
        print(f"Le livre '{book_title}' n'est pas disponible.")
        return False
    """
    #Tâche 6
    def lend_book(self, book_title: str, student: 'Student') -> bool:
        if book_title in student.borrowed_books:
            print(f"{student.name} a déjà emprunté '{book_title}'.")
            return False
        for book in self.books:
            if book.title == book_title:
                if book.is_available:
                    book.is_available = False
                    student.borrowed_books.append(book_title)
                    print(f"Le livre '{book_title}' a été prêté à {student.name}.")
                    return True
                else:
                    print(f"Le livre '{book_title}' n'est pas disponible.")
                    return False
        print(f"Le livre '{book_title}' n'existe pas dans la bibliothèque.")
        return False
    
    
    
    def accept_return(self, book_title: str, student: 'Student'):
        if book_title not in student.borrowed_books:
            print(f"{student.name} n'a pas emprunté le livre '{book_title}'.")
            return
        for book in self.books:
            if book.title == book_title:
                book.is_available = True
                student.borrowed_books.remove(book_title)
                print(f"Le livre '{book_title}' a été retourné par {student.name}.")
                return

        print(f"Le livre '{book_title}' n'existe pas dans la bibliothèque.")
    #Tache 7
    def search_books(self, query: str) -> list:
        query = query.lower() 
        results = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():  
                results.append(str(book))  
        return results
    #TACHE 8
    def save_books(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.is_available}\n")
            print(f"Les livres ont été sauvegardés dans '{file_path}'.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des livres : {e}")
    
            
#TÂCHE 2 EXECUTION 

library = Library()
library.add_book("1984", "George Orwell")
library.add_book("1984 - Edition Commenté", "George Orwell")

print("Books in the library:")
for book_info in library.list_books():
    print(book_info)
print("------------------")
#TÂCHE 3 EXECUTION

library = Library()
library.load_books('library_data.txt')

print("Liste des livres de la bibliothèque:")
for book_info in library.list_books():
    print(book_info)
print("-----------------------------")

#TÂCHE4
class Student:
    def __init__(self, name: str, max_borrow_limit: int = 3):
        self.name = name
        self.borrowed_books = []  
        self.max_borrow_limit = max_borrow_limit 

    def borrow_book(self, book_title: str, library: Library):

        if len(self.borrowed_books) >= self.max_borrow_limit:
            print(f"{self.name} ne peut pas emprunter plus de {self.max_borrow_limit} livres.")
            return

        for book in library.books:
            if book.title == book_title and book.is_available:
                book.is_available = False  
                self.borrowed_books.append(book_title)  
                print(f"{self.name} a emprunté '{book_title}'.")
                return

        print(f"Le livre '{book_title}' n'est pas disponible ou n'existe pas.")

    def return_book(self, book_title: str, library: Library):
        if book_title in self.borrowed_books:
            for book in library.books:
                if book.title == book_title:
                    book.is_available = True  
                    self.borrowed_books.remove(book_title)  
                    print(f"{self.name} a rendu '{book_title}'.")
                    return
        print(f"{self.name} n'a pas emprunté le livre '{book_title}'.")
   


#TÂCHE 4 TEST

student = Student("John Doe")
student2 = Student("Lucas Rey")
student.borrow_book("1984", library)

student.borrow_book("To Kill a Mockingbird", library)

student2.borrow_book("1984", library)

##########################################

print("\nLivre disponible :")
for book_info in library.list_books():
    print(book_info)
    
print("-------------")
student.return_book("1984", library)

student.return_book("The Great Gatsby", library)
student2.borrow_book("1984", library)
student.borrow_book("1984", library)

print("-----")
print("\nLivre Disponible:")
for book_info in library.list_books():
    print(book_info)
    
    
#Test tache 7
print("--------------")
search_results = library.search_books("George Orwell")

print("Résultats de la recherche pour 'George Orwell':")
for result in search_results:
    print(result)
    
#Test tache 8
print("--------------")
library = Library()
library.add_book("1984", "George Orwell")
library.add_book("1984 - Edition Commenté", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

library.save_books("library_data.txt")

new_library = Library()
new_library.load_books("library_data.txt")

print("Livres chargés de la bibliothèque:")
for book_info in new_library.list_books():
    print(book_info)

print("-----------------")
#TEST TACHE 9

def run_library_system():
    library = Library()
    
    library.add_book("1984", "George Orwell")
    library.add_book("1984 - Edition Commenté", "George Orwell")
    library.add_book("Apprendre Python", "Lucas Rey")
    library.add_book("To Kill a Mockingbird", "Harper Lee")

    student1 = Student("John Doe")
    student2 = Student("Lucas Rey")
    
    while True:
        print("\n--- Menu de gestion de la bibliothèque ---")
        print("1. Voir tous les livres")
        print("2. Rechercher un livre")
        print("3. Ajouter un nouveau livre")
        print("4. Emprunter un livre")
        print("5. Rendre un livre")
        print("6. Quitter")
        choice = input("Veuillez choisir une option (1-6): ")
    
        if choice == "1":
            print("\nListe des livres disponibles:")
            for book_info in library.list_books():
                print(book_info)
        
        elif choice == "2":
            query = input("\nEntrez le titre ou l'auteur du livre à rechercher: ")
            search_results = library.search_books(query)
            if search_results:
                print("\nRésultats de la recherche:")
                for result in search_results:
                    print(result)
            else:
                print(f"Aucun livre trouvé pour '{query}'.")
        
        elif choice == "3":
            title = input("\nEntrez le titre du livre: ")
            author = input("Entrez l'auteur du livre: ")
            library.add_book(title, author)
            print(f"Le livre '{title}' a été ajouté à la bibliothèque.")
        
        elif choice == "4":
            book_title = input("\nEntrez le titre du livre à emprunter: ")
            student_name = input("Entrez le nom de l'étudiant: ")
            student = student1 if student_name.lower() == "john doe" else student2
            student.borrow_book(book_title, library)
        
        elif choice == "5":
            book_title = input("\nEntrez le titre du livre à rendre: ")
            student_name = input("Entrez le nom de l'étudiant: ")
            student = student1 if student_name.lower() == "john doe" else student2
            student.return_book(book_title, library)
        
        elif choice == "6":
            print("Fermeture du logiciel")
            break
        
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 6.")
            
if __name__ == "__main__":
    run_library_system()
