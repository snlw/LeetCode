-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/1299860271
SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
