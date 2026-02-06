"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

#Name: Mahmoud Mustafa - ID: 201868040

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = """
            SELECT F.title, S.screen, T.price
            FROM tickets T 
            JOIN screenings S ON S.screening_id = T.screening_id
            JOIN films F ON F.film_id = S.film_id
            WHERE T.customer_id = ?
            ORDER BY F.title
            """
    
    cursor = conn.execute(query, (customer_id,))

    return cursor.fetchall()

def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    query = """
            SELECT S.screening_id, F.title, count(T.ticket_id) AS Tickets_Sold
            FROM Screenings S
            JOIN films F ON F.film_id = S.film_id
            LEFT JOIN tickets T ON T.screening_id = S.screening_id
            GROUP BY S.screening_id, F.title
            ORDER BY Tickets_Sold DESC
            """

    cursor = conn.execute(query)

    return cursor.fetchall()

def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    query = """
            SELECT C.customer_name, sum(T.price) AS Total_Spent
            FROM customers C
            JOIN tickets T ON T.customer_id = C.customer_id
            GROUP BY C.customer_name
            ORDER BY Total_Spent DESC
            LIMIT ?
            """
    
    cursor = conn.execute(query, (limit,))

    return cursor.fetchall()