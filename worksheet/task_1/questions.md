You are working with a database used by a university library system.  
The system tracks library members, books, and borrowing activity.

The database contains the following tables:

members(<u>member_id</u>, member_name, join_date)  
books(<u>book_id</u>, title, author)  
loans(<u>loan_id</u>, member_id, book_id, loan_date, return_date)

---

a) For each pair of tables below, state the type of relationship  
(one-to-one, one-to-many, or many-to-many) and briefly explain your reasoning.

i. Members and loans [2] 
one-to-many
as a member can have many loans but a loan cannot have many members 
ii. Books and loans [2]  
one-to-one
as each book is loaned and each loan is per book used, loan cannot exist without books
iii. Members and books [2]  
one-to-many
as each member can have many books but a book can only be loaned by one person

---

b) A query joins members to loans using an INNER JOIN.

i. Explain what happens to members who have never borrowed a book. [2]  
They are not counted as the inner join does not regard null values
ii. Explain how the results of the query would change if a LEFT JOIN were used instead. [2]  
A left join includes null values of its query, so the members who have never borrowed a book will also be included

---

c) The head librarian would like to see how many books have been borrowed by each library member.

i. Write an SQL query which would show the name of each library member and how many loans they have taken out. [5]  
select M.member, count(L.loan_id) AS Books_Borrowed
from members M 
left join loans L on M.member.id = L.member_id
group by M.member.id

---

d) The head librarian asks:  
“Why don’t you store the book title with the loan? Wouldn’t that make it easier to see the data?”

i. Explain, using appropriate non-technical language, why this would be bad database design. [5]
This is as it can create redundant data which is repeated data or anomalies, as some members may have borrowed the same book title having repeated grouping. Also as this would consume a lot of time to update any new data in the records, as well as, if there is a new book in the library that no one has yet loaned, it would not make sense to store it within the loans section.