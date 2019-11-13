#  File: BabyNames.py

#  Description: This program will take name data with their rankings and allow the user to perform different options
#   such as searching for a name, display data for a name, display all names ranked in a certain decade, display all
#   names that are ranked in all decades, display all names that are more popular in every decade, and display all
#   names that are less popular every decade.

#  Student Name:  Basilio Bazan III

#  Student UT EID:  bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 09/12/2018

#  Date Last Modified: 09/15/2018

#Searches if a name is ranked in any decade
def name_search(names, pick):
    for i in names:
        if i == pick:
            return True
    return False

#Displays the data of a name
def data_display(names, pick):
    setstring = pick +":"
    for i in names[pick]:
        if i == 1001:
            setstring += " 0"
        else:
            setstring += " "+str(i)
    print(setstring)

#Finds all names ranked in a certain decade and sorts them on rank
def decade_names(names,dec):
    decnames = {}
    for i in names:
        if names[i][dec] != 1001:
            decnames[i] = names[i][dec]
    sorted_dec = sorted(decnames.items(), key=lambda x: x[1])
    for a in sorted_dec:
        print(a[0] + ": "+ str(a[1]))

#This function will find all the names that are ranked each decade
def decades_all(names):
    allnames = []
    for i in names:
        haszero = False
        for x in names[i]:    #Checks if there is no rank in any decade
            if x == 1001:
                haszero = True
                break
        if haszero == False:
            allnames.append(i)
        allnames.sort()
    return allnames

#This function will find all the names that are more popular each decade
def more_pop(names):
    morenames = []
    for i in names:
        more = True
        temp = 1001
        for x in names[i]:
            if temp > x:
                temp = x
            else: #Breaks once it finds that a name was less popular in checked decade
                more = False
                break
        if more == True:
            morenames.append(i)
    morenames.sort()
    return morenames

#This function will find all names that are less popular with each decade.
def less_pop(names):
    lessnames = []
    for i in names:
        less = True
        temp = 0
        for x in names[i]:
            if temp < x:
                temp = x
            else: #Breaks once it finds that a name was more popular in checked decade
                less = False
                break
        if less == True:
            lessnames.append(i)
    lessnames.sort()
    return lessnames

def main():
    names = {}
    menu = {}
    menu['1'] = "to search for a name."
    menu['2'] = "to display data for a name."
    menu['3'] = "to display all the names in a certain decade."
    menu['4'] = "to display all the names that appear in all decades."
    menu['5'] = "to display all the names that are more popular in every decade."
    menu['6'] = "to display all the names that are less popular in every decade."
    menu['7'] = "to quit"
    choices = menu.keys()

    while True:
        try:
            file = open("./names.txt", "r")
        except:
            print("Sorry could not read file.")
            exit()
        finally:
            for line in file:
                #line = str(line, encoding = 'utf8')
                line = line.strip()
                line = line.split()
                ranks = []
                for i in range(1,len(line)):
                    if int(line[i]) == 0:
                        line[i] = 1001
                    ranks.append(int(line[i]))
                names[line[0]] = ranks

            print("Options:")   #Prints out the menu
            for e in choices:
                print(e, menu[e])
            print()
            num = int(input("Enter choice: "))

            if num == 1:       #Search name in any decade
                pick = input("Enter a name: ").capitalize()
                temp = 1001
                if name_search(names, pick):
                    print("The matches with their highest ranking decade are:")
                    for x in range(len(names[pick])):  #Finds the best rank of a certain name.
                        if names[pick][x] < temp:
                            index = x
                            temp = names[pick][x]
                    print(""+pick+" "+str(1900+(10*index)))
                    print()
                else:
                    print(""+pick+" does not appear in any decade.")
                    print()

            elif num == 2:
                pick = input("Enter a name: ").capitalize()
                if name_search(names,pick):
                    print()
                    data_display(names, pick)
                    for i in range(len(names[pick])):   #Prints rank for each decade
                        if names[pick][i] == 1001:
                            print(str(1900+(10*i))+": 0")
                        else:
                            print(str(1900 + (10 * i)) + ": "+str(names[pick][i]))
                    print()
                else:
                    print("" + pick + " does not appear in any decade.")
                    print()

            elif num == 3:
                dec = int(input("Enter decade: "))
                dec = int((dec-1900)/10)  #changes decade to the corresponding index in deictionary
                print("The names are in order of rank:")
                decade_names(names, dec)
                print()

            elif num == 4:
                alldecades = decades_all(names)
                print(str(len(alldecades))+" names appear in every decade. The names are:")
                for n in alldecades:
                    print(n)
                print()

            elif num == 5:
                popular = more_pop(names)
                print(str(len(popular))+" names are more popular in every decade.")
                for n in popular:
                    print(n)
                print()

            elif num == 6:
                lesspopular = less_pop(names)
                print(str(len(lesspopular)) + " names are less popular in every decade.")
                for n in lesspopular:
                    print(n)
                print()

            elif num >= 7:
                print("/n/nGoodbye.")
                break
            else:
                print("")
                print("Invalid selection please try again.")

            file.close()
main()