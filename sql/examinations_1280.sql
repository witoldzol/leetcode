-- my code ( not working )
-- select e.student_id, s.student_name, e.subject_name, count(e.student_id) as attended_exams from Examinations e
-- left join Students s on s.student_id = e.student_id
-- group by e.student_id, e.subject_name, s.student_name
-- order by e.student_id, e.subject_name

-- working solution
SELECT S.student_id, S.student_name, SUB.subject_name, count(e.subject_name) AS attended_exams FROM Students S 
CROSS JOIN  Subjects SUB 
LEFT OUTER JOIN Examinations e ON S.student_id = e.student_id 
AND SUB.subject_name = e.subject_name  
GROUP BY S.student_id, S.student_name,SUB.subject_name 
1ORDER BY S.student_id, SUB.subject_name
