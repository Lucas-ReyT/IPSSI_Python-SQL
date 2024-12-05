
#TACHE 3

SELECT s.student_id, s.name AS student_name, c.course_name, c.credits
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c ON e.course_id = c.course_id;

SELECT s.student_id, s.name AS student_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;


#TACHE 4

SELECT c.course_id, c.course_name, c.capacity, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.capacity;

SELECT c.course_id, c.course_name, c.capacity, COUNT(e.student_id) AS enrolled_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.capacity
HAVING COUNT(e.student_id) > c.capacity / 2;

#TACHE 5
#Query 5

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

#QUERY 6
SELECT s.student_id, s.name, SUM(c.credits) AS total_credits
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
GROUP BY s.student_id, s.name;

#QUERY 7
SELECT c.course_id, c.course_name
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
WHERE e.student_id IS NULL;


#tache 6

#Je ne sais pas comment faire.

#TACHE 7



DELETE FROM Enrollments
WHERE course_id = 101;

DELETE FROM Students
WHERE student_id NOT IN (
    SELECT DISTINCT student_id
    FROM Enrollments
);
