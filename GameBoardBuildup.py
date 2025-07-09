import mysql.connector as Con
import sys, time
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
H = ["Property Number", "Property Name", "Price", "Level 1 Rent", "Level 2 Rent", "Level 3 Rent", "Level 4 Rent", "Level 5 Rent"]
R = list()

def CreateTable():
    try:
        C.execute("DROP TABLE IF EXISTS GameBoard")
        C.execute("""CREATE TABLE GameBoard
                (Num   integer     NOT NULL    PRIMARY KEY,
                PName varchar(30) NOT NULL,
                Price integer,
                R1    integer,
                R2    integer,
                R3    integer,
                R4    integer,
                R5    integer)
                """)
    except:
        print("Game Board Table could not be constructed. Please debug")


def main():
    print()
    time.sleep(2)
    print("What action do you wish to perform?")
    print("1. Construct a new game board entirely")
    print("2. Edit an existing game board IF EXISTS")
    print("3. View All Properties")
    print("4. Exit")
    ch = int(input("Enter Choice: "))
    print()
    match ch:
        case 1:
            NewBoardConstruct()
        case 2:
            EditOldBoard()
        case 3:
            ViewBoard()
        case 4:
            sys.exit("Thank You for using Monopoly Game Board Constructor\n")
        case _ : 
            print("Please enter a valid choice")
            main()
    sys.exit("Thank You for using Monopoly Game Board Constructor\n")


def NewBoardConstruct():
    print("A Standard Monopoly Game Board consists of 22 property squares")
    print("You need to enter the details of the 22 properties ONLY")
    print("Rest of the board will be constructed automatically")
    time.sleep(2)
    CreateTable()
    for i in range(22):
        print()
        print(f"Property #{i+1}")
        Name = input("Property Name: ").title()
        P = int(input("Price: "))
        Rent = [int(input(f"Level {j} rent: ")) for j in range(1,6)]
        Q = f"INSERT INTO GameBoard VALUES ({i+1},'{Name}',{P}, {Rent[0]},{Rent[1]},{Rent[2]},{Rent[3]},{Rent[4]})"
        C.execute(Q)
        Co.commit()
    print()
    print("All 22 properties have been feeded into the system, you may begin with MONOPOLY")


def EditOldBoard():
    ViewBoard()
    while True:
        ch = input("Do you wish to edit details of any property? (Y/N)").lower()
        match ch:
            case "y" : EditProperty(R)
            case "n" : sys.exit("\nThank You for using Monopoly Game Board Constructor")
            case _ : print("Please enter a valid character")
        time.sleep(2)


def EditProperty(Rows):
    time.sleep(2)
    N = int(input("Enter the Property Number: "))
    Row = []
    for Row in Rows:
        if Row[0] == N:
            break
    print("Property Found!")
    print(tabulate([Row], headers = H, tablefmt = "grid"))
    time.sleep(2)
    print(f"Enter the new details for property {N}")
    Name = input("Property Name: ").title()
    P = int(input("Price: "))
    Rent = [int(input(f"Level {j} rent: ")) for j in range(1,6)]
    Q1 = f"DELETE FROM GameBoard WHERE Num = {N}"
    Q2 = f"INSERT INTO GameBoard VALUES ({N},'{Name}',{P}, {Rent[0]},{Rent[1]},{Rent[2]},{Rent[3]},{Rent[4]})"
    C.execute(Q1)
    C.execute(Q2)
    Co.commit()
    time.sleep(2)
    print("Property Editted Successfully!!")    


def ViewBoard():
    global R
    print("Printing the Game Board, if one exists")
    try:
        C.execute("SELECT * FROM GameBoard ORDER BY Num")
        R = C.fetchall()
        R = [list(row) for row in R]
    except:
        time.sleep(2)
        print("No Game Board Found, Please check")
        main()
    else:
        time.sleep(2)
        print(tabulate(R, headers = H, tablefmt = "grid"))


if __name__ == "__main__":
    print()
    print("Hello and Welcome to the Monopoly Game Board Constructor")
    main()
    Co.close()