from pyscript import document

class Classmate:
    def __init__(self, name, section, favno):
        self.name = name
        self.section = section
        self.favno = favno

    def introduce(self):
        return f"Hi, I'm {self.name} from {self.section} and my favorite number is {self.favno}."
    
classlist = [
    Classmate("AC", "Sapphire", 9),
    Classmate("Zyan", "Sapphire", 69),
    Classmate("Luis", "Sapphire", 67),
    Classmate("Enzo", "Sapphire", 19),
    Classmate("Cade", "Sapphire", 7),
    Classmate("Hans", "Ruby", 4),

]

def showlist(e):            # shows class list
    output = ""
    for classmate in classlist:
        output += classmate.introduce() + "<br>"
    document.getElementById("output").innerHTML = output

def addclassmate(e):            # Function to add new classmate to list
    nam = document.getElementById("name").value
    sect = document.getElementById("section").value
    fav = int(document.getElementById("favno").value)
    new_classmate = Classmate(name = nam, section = sect, favno = fav)
    classlist.append(new_classmate)
    showlist(e)

    