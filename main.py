"""Project name : Input and Output training
    File name : main.py
    Programmer : Colin B. Chin Choy
"""
#---------------------------Global Resources---------------------------------
f = ""
#noTes = []
ext = ".txt"
#nam = ""
q = True
#----------------------------------------------------------------------------
def initAte():
    fname = input("Please enter the file name to open: ")
    global nam
    nam = fname+ext
    try:
        f = open(nam)
        f.close()
        writMode(nam)
    except FileNotFoundError:
        res = input(fname+" not found, do you want to create or exit:(C/E) ")
        if res == "c":
            f = open(nam, "w")
            f.close()
            writMode(nam)

def opFile():
    fname = input("Please enter the file name to open: ")
    nam = fname+ext
    f = open(nam)
    f.close()
    writMode(nam)

def creAt():
    fname = input("Please enter the file name to create: ")
    global nam
    nam = fname+ext
    f = open(nam, "w")
    f.close()
    writMode(nam)

def writMode(nam):
    an = input("Do you want to open the file for (New/Append/Read/Reaplace 1 line)(N/A/R/RE): ")
    if an == "n":
        neMode(nam)
    if an == "a":
        apMode(nam)
    if an == "r":
        rMode(nam)
    if an == "re":
        reMode(nam)

def neMode(nam):
    f = open(nam, "w")
    strng = str(input("Enter item to be noted: "))
    f.write(strng+"\n")
    f.close()
    rMode(nam)

def apMode(nam):
    print(nam)
    f = open(nam, "a")
    strng = str(input("Enter item to be appended: "))
    f.write(strng+"\n")
    f.close()
    rMode(nam)

def rMode(nam):
    noTes = []
    f = open(nam,"r")
    for itm in f:
        newitm = itm.strip()
        noTes.append(newitm)
    f.close()
    print(noTes)

def reMode(nam):
    noTes = []
    rMode(nam)
    old = input("Which Item to replace: ")
    new = input("What to replace it with: ")
    f = open(nam, "r+")

    for lin in f:
        stripped_lin = lin.strip()
        noTes.append(stripped_lin)
    for lin in noTes:

        if lin == old:
            noTes[noTes.index(old)] = new
    f.close()
    f = open(nam, "w+")
    for lin in noTes:
        f.write(lin+"\n")
#    noTes = f.readlines()
    print(noTes)
    f.close()

print("Welcome to Note")
initAte()

while q == True:
        an1 = input("Do you want to add another note or create another file Replace again or Quit:(A/F/Re/Q) ")
        if an1 == "a":
            apMode(nam)
        if an1 == "c" :
            creAt()
        if an1 == "q" :
            q = False
            break
        if an1 =="re" :
            reMode(nam)
