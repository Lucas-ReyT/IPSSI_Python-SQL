Documentation pour la base de données universitaire

Ce projet contient une base de données pour gérer des étudiants, des cours et les inscriptions des étudiants dans ces cours. Elle permet de suivre les informations des étudiants, les détails des cours, ainsi que les inscriptions des étudiants dans ces derniers.
Structure de la base de données
Tables

    Students (Étudiants)
        student_id (INT) : Identifiant unique de l'étudiant (clé primaire).
        name (VARCHAR(50)) : Nom de l'étudiant.
        age (INT) : Âge de l'étudiant.
        gender (VARCHAR(10)) : Genre de l'étudiant (par exemple : "Garçon", "Fille").

    Courses (Cours)
        course_id (INT) : Identifiant unique du cours (clé primaire).
        course_name (VARCHAR(50)) : Nom du cours.
        credits (INT) : Nombre de crédits associés au cours.
        capacity (INT) : Capacité maximale d'inscriptions pour ce cours.

    Enrollments (Inscriptions)
        enrollment_id (INTEGER) : Identifiant unique de l'inscription (clé primaire).
        student_id (INTEGER) : Identifiant de l'étudiant (clé étrangère, référence à Students).
        course_id (INTEGER) : Identifiant du cours (clé étrangère, référence à Courses).

Données de démonstration

INSERT INTO Students (student_id, name, age, gender)
VALUES 
(1, 'Antoine Dupont', 22, 'Garçon'),
(2, 'Dwayne Johnson', 22, 'Garçon'),
(3, 'Elisabeth Borne', 60, 'Fille'),
(4, 'Mickael Jackson', 23, 'Garçon'),
(5, 'Taylor Swift', 22, 'Fille'),
(6, 'François Hollande', 45, 'Garçon');
Table Courses

INSERT INTO Courses (course_id, course_name, credits, capacity)
VALUES 
(101, 'Informatique', 3, 2),
(102, 'Math', 4, 25), 
(103, 'Histoire', 3, 20),  
(104, 'SVT', 4, 15);

Table Enrollments

INSERT INTO Enrollments (student_id, course_id)
VALUES 
(1, 101),
(2, 101),
(3, 101),
(4, 101),
(5, 101),
(1, 102),
(2, 102),
(3, 103);

Requêtes SQL
Tâche 3 : Récupération des informations des étudiants et des cours

    Afficher les étudiants et leurs cours avec les crédits associés
    Cette requête sélectionne les étudiants, les cours auxquels ils sont inscrits et le nombre de crédits de chaque cours.

SELECT s.student_id, s.name AS student_name, c.course_name, c.credits
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c ON e.course_id = c.course_id;

Afficher les étudiants non inscrits à un cours
Cette requête liste les étudiants qui ne sont inscrits à aucun cours.

    SELECT s.student_id, s.name AS student_name
    FROM Students s
    LEFT JOIN Enrollments e ON s.student_id = e.student_id
    WHERE e.enrollment_id IS NULL;

Tâche 4 : Nombre d'étudiants inscrits dans chaque cours

    Afficher la capacité et le nombre d'inscriptions pour chaque cours
    Cette requête renvoie la capacité de chaque cours ainsi que le nombre d'étudiants inscrits.

SELECT c.course_id, c.course_name, c.capacity, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.capacity;

Afficher les cours avec un nombre d'inscriptions supérieur à la moitié de leur capacité
Cette requête permet de filtrer les cours où le nombre d'inscriptions dépasse la moitié de leur capacité.

    SELECT c.course_id, c.course_name, c.capacity, COUNT(e.student_id) AS enrolled_students
    FROM Courses c
    LEFT JOIN Enrollments e ON c.course_id = e.course_id
    GROUP BY c.course_id, c.course_name, c.capacity
    HAVING COUNT(e.student_id) > c.capacity / 2;

Tâche 5 : Statistiques sur les étudiants et leurs inscriptions

    Afficher l'étudiant inscrit au plus grand nombre de cours
    Cette requête trouve l'étudiant ayant le plus grand nombre d'inscriptions.

SELECT s.student_id, s.name, COUNT(e.course_id) AS num_courses
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name
HAVING COUNT(e.course_id) = (
    SELECT MAX(course_count)
    FROM (
        SELECT COUNT(course_id) AS course_count
        FROM Enrollments
        GROUP BY student_id
    ) AS course_counts
);

Afficher le total des crédits pour chaque étudiant
Cette requête calcule le total des crédits obtenus par chaque étudiant en fonction de ses inscriptions.

SELECT s.student_id, s.name, SUM(c.credits) AS total_credits
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
GROUP BY s.student_id, s.name;

Afficher les cours sans étudiants inscrits
Cette requête permet d'afficher les cours auxquels aucun étudiant n'est inscrit.

    SELECT c.course_id, c.course_name
    FROM Courses c
    LEFT JOIN Enrollments e ON c.course_id = e.course_id
    WHERE e.student_id IS NULL;

Tâche 7 : Suppression des inscriptions et des étudiants

    Supprimer toutes les inscriptions pour le cours d'informatique
    Cette requête supprime toutes les inscriptions des étudiants au cours avec course_id = 101.

DELETE FROM Enrollments
WHERE course_id = 101;

Supprimer les étudiants non inscrits à des cours
Cette requête supprime les étudiants qui ne sont inscrits à aucun cours.

DELETE FROM Students
WHERE student_id NOT IN (
    SELECT DISTINCT student_id
    FROM Enrollments
);
