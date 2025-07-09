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
H = ["Property Number", "Property Name", "Price", "Level 1 Rent", "Level 2 Rent", "Level 3 Rent", "Level 4 Rent", "Level 5 Rent"]
Board = [ ["GO", "1", "M", "2", "M", "3", "4", "L", "5", "J"],
          ["22", "", "", "", "", "", "", "", "", "6"],
          ["L", "", "", "", "", "", "", "", "", "M"],
          ["21", "", "", "", "", "", "", "", "", "7"],
          ["M", "", "", "", "", "", "", "", "", "8"],
          ["20", "", "", "", "", "", "", "", "", "9"],
          ["19", "", "", "", "", "", "", "", "", "10"],
          ["M", "", "", "", "", "", "", "", "", "L"],
          ["18", "", "", "", "", "", "", "", "", "11"],
          ["GJ", "17", "L", "16", "15", "14", "13", "M", "12", "FP"],  
            ]


def PrintBoard():
    print()
    B = ColourBoardText(Board)
    B[0][3] = ColourBg(B[0][3], "cream")
    print(tabulate(B, tablefmt = "grid", colalign = ("centre",)*10 ))
    print()


def Colour(T, C):
    code = {
        "brown" : "38;5;130",
        "cyan" : "36",
        "magenta" : "35",
        "orange" : "38;5;208",
        "red" : "31",
        "yellow" : "33",
        "green" : "32",
        "blue" : "34" }
    return f"\033[1;{code[C]}m{T}\033[0m"


def ColourProperties(T):
    match T:
        case "1"|"2" : return Colour(T,"brown")
        case "3"|"4"|"5" : return Colour(T, "cyan")
        case "6"|"7"|"8" : return Colour(T,"magenta")
        case "9"|"10"|"11" : return Colour(T,"orange")
        case "12"|"13"|"14" : return Colour(T, "red")
        case "15"|"16"|"17" : return Colour(T, "yellow")
        case "18"|"19"|"20" : return Colour(T, "green")
        case "21"|"22" : return Colour(T,"blue")
        case _ : return T


def ColourBoardText(B):
    return [[ColourProperties(x) for x in row] for row in B]


def ColourBg(T,C = 'default'):
    code = {
        "cream" : "48;5;230",
        "dark purple" : "48;5;90",
        "light grey" : "48;5;250",
        "olive" : "48;5;100",
        "default" : "0",
    }
    return f"\033[{code[C]}m{T}\033[0m"


def main():
    PrintBoard()


if __name__ == "__main__":
    print()
    main()
    Co.close()