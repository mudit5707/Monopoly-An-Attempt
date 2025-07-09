import mysql.connector as Con
import sys
from tabulate import tabulate

Co = Con.connect(
    host = "localhost", 
    user = "root", 
    passwd = "mudit@MySQL", 
    database = "monopoly",
    )

if not Co.is_connected():
    sys.exit("The Connection between python and MySQL was not established. Please debug")

C = Co.cursor()

C.execute(""" 
          ALTER TABLE GameBoard
          ADD Price integer DEFAULT 0
          AFTER PName
          """)
Co.commit()

for i in range(22):
    P = int(input(f"Enter the price of Property {i+1}: "))
    C.execute(f"""
              UPDATE GameBoard
              SET Price = {P}
              WHERE Num = {i+1} """)
    Co.commit()

H = ["Property Number", "Property Name", "Price", "Level 1 Rent", "Level 2 Rent", "Level 3 Rent", "Level 4 Rent", "Level 5 Rent"]
try:
    C.execute("SELECT * FROM GameBoard ORDER BY Num")
    R = C.fetchall()
    R = [list(row) for row in R]
except:
    print("No Game Board Found, Please check")
else:
    print(tabulate(R, headers = H, tablefmt = "grid"))