
INSERT INTO Students (student_id, name, age, gender)
VALUES 
(1, 'Antoine Dupont', 22, 'Garçon'),
(2, 'Dwayne Johnson', 22, 'Garçon'),
(3, 'Elisabeth Borne', 60, 'Fille'),
(4, 'Mickael Jackson', 23, 'Garçon'),
(5, 'Taylor Swift', 22, 'Fille'),
(6, 'François Hollande', 45, 'Garçon');


INSERT INTO Courses (course_id, course_name, credits, capacity)
VALUES 
(101, 'Informatique', 3, 2),
(102, 'Math', 4, 25), 
(103, 'Histoire', 3, 20),  
(104, 'SVT', 4, 15); 


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