import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

def run_query(title, sql):
    print(f"\n{'='*55}\n {title}\n{'='*55}")
    cursor.execute(sql)
    cols = [d[0] for d in cursor.description]
    print("  " + " | ".join(f"{c:<18}" for c in cols))
    print("  " + "-"*55)
    for row in cursor.fetchall():
        print("  " + " | ".join(f"{str(v):<18}" for v in row))

# Q1 — View first 5 orders
run_query("Q1 · First 5 Orders", """
    SELECT OrderID, Product, Quantity, TotalPrice
    FROM orders LIMIT 5
""")

# Q2 — Only Delivered orders
run_query("Q2 · Delivered Orders", """
    SELECT OrderID, Product, OrderStatus, TotalPrice
    FROM orders
    WHERE OrderStatus = 'Delivered'
    LIMIT 10
""")

conn.close()