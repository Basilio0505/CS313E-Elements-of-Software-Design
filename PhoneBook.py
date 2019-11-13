#  File: PhoneBook.py

#  Description: This program will retrieve data and create a phone book where the user has the options to search,
# update, or delete a person and their information from the phone book. At the end the text file is rewritten with
# the new data.

#  Student Name: Basilio Bazan III

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 09/20/2018

#  Date Last Modified: 09/21/2018

class ContactInfo (object):
  # constructor
  def __init__ (self, street, city, state, zip_code, country, phone, email):
      self.street = street
      self.city = city
      self.state = state
      self.zip_code = zip_code
      self.country = country
      self.phone = phone
      self.email = email

  # string representation of Contact Info
  def __str__ (self):
      return self.street+"\n"+self.city+"\n"+self.state+"\n"+self.zip_code+"\n"+\
             self.country+"\n"+self.phone+"\n"+self.email

# Define global dictionary to hold all the contact information
phone_book = {}

# This function adds the contact information of a new person in the
# dictionary
def add_person():
  # Prompt the user to enter the name of the new person
  name = input("Enter name: ")
  # Check if name exists in phone book. If it does print a message
  # to that effect and return
  for i in phone_book:
    if i == name or name == "":
      print("That person already exists in the phone book.")
      return

  # Prompt the user to enter the required contact information
  street = input("Enter street: ")
  city = input("Enter city: ")
  state = input("Enter state: ")
  zip_code = input("Enter zip_code: ")
  country = input("Enter country: ")
  phone = input("Enter phone number: ")
  email = input("Enter e-mail address: ")
  # Create the ContactInfo object
  contactObj = ContactInfo (street, city, state, zip_code, country, phone, email)

  # Add the name and the contact information to the phone dictionary
  phone_book[name] = contactObj
  # Print message that the information was added successfully
  print("\n"+name+" was successfully added to the phone book.\n")

# This function deletes an existing person from the phone dictionary
def delete_person():
  # Prompt the user to enter the name of the person
  name = input("Enter name: ")
  deleted = False
  print()
  # If the name exists in phone book delete it.
  # Print message as to the action.
  for i in phone_book:
    if i == name:
      del phone_book[i]
      deleted = True
      print(name + " was deleted from the phone book.\n")
      break
  if not deleted:
    print(name + " does not exist in the phone book.\n")

# This function updates the information of an existing person
def update_person():
  # Prompt the user to enter the name of the person
  name = input("Enter name: ")
  exist = False
  # Check if name exists in phone book. If it does prompt
  # the user to enter the required information.
  for i in phone_book:
    if i == name:
      exist = True
      break

  if exist:
    update = input("Enter street: ")
    if update != "":
      phone_book[name].street = update
    update = input("Enter city: ")
    if update != "":
        phone_book[name].city = update
    update = input("Enter state: ")
    if update != "":
        phone_book[name].state = update
    update = input("Enter zip: ")
    if update != "":
        phone_book[name].zip_code = update
    update = input("Enter country: ")
    if update != "":
        phone_book[name].country = update
    update = input("Enter phone number: ")
    if update != "":
        phone_book[name].phone = update
    update = input("Enter e-mail address: ")
    if update != "":
        phone_book[name].email = update
    # Write a message as to the action
    print("\n"+name+" has been successfully updated in the phone book.\n")
  else:
    print(name+" does not exist in the phone book.\n")

# This function prints the contact information of an existing person
def search_person():
  # Prompt the user to enter the name of the person
  name = input("Enter name: ")
  print()
  found = False
  # Check if name exists in phone book. If it does print the
  # information in a neat format.
  for i in phone_book:
    if i == name:
      found = True
      print(name)
      print(phone_book[name])
      print()
  # If the name does not exist print a message to that effect.
  if not found:
    print(name+" does not exist in the phone book.\n")

# This function open the file for writing and writes out the contents
# of the dictionary.
def save_quit():
  # Open file for writing
  file = open ("./phone.txt", "w")
  # Iterate through the dictionary and write out the items in the file
  for i in phone_book:
    file.write(i+"\n")
    file.write(phone_book[i].street+"\n")
    file.write(phone_book[i].city+"\n")
    file.write(phone_book[i].state+"\n")
    file.write(phone_book[i].zip_code+"\n")
    file.write(phone_book[i].country+"\n")
    file.write(phone_book[i].phone+"\n")
    file.write(phone_book[i].email+"\n")
    file.write("\n")

  # Close file
  file.close()

  # Print  message
  print("Thank you for using the phone book.")

# This function prints the menu, prompts the user for his/her selection
# and returns it.
def menu():
    print("\n1. Add a Person\n")
    print("2. Delete a Person\n")
    print("3. Search for a Person\n")
    print("4. Update Information on a Person\n")
    print("5. Quit\n")
    select = 0
    while select < 1 or select > 5:
        try:
            select = int(input("Enter your selection: "))
        except:
            print("\nOops that input was invalid")
            select = 0
    return select

# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.
def create_phone_book():
  # Open file for reading
  in_file = open ("./phone.txt", "r")

  # Read first line (name)
  line = in_file.readline()
  line = line.strip()

  # Loop through the entries for each person
  while (line != ""):
    name = line

    # Read street
    street = in_file.readline()
    street = street.strip()
    # Read city
    city = in_file.readline()
    city = city.strip()
    # Read state
    state = in_file.readline()
    state = state.strip()
    # Read zip-code
    zip_code = in_file.readline()
    zip_code = zip_code.strip()
    # Read country
    country = in_file.readline()
    country = country.strip()
    # Read phone number
    phone = in_file.readline()
    phone = phone.strip()
    # Read e-mail address
    email = in_file.readline()
    email = email.strip()
    # Read blank line
    in_file.readline()
    # Read first line of the next block of data
    line = in_file.readline()
    line = line.strip()

    # Create ContactInfo object
    contact = ContactInfo(street, city, state, zip_code, country, phone, email)
    # Add to phone dictionary
    phone_book[name] = contact
  # Close file
  in_file.close()

def main():
  # Read file and create phone book dictionary
  create_phone_book()
  while True:
    # Print logo
    print("Phone Book")
    # Print menu and get selection
    selection = menu()

    # Process request, print menu and prompt again and again
    # until the user types 5 to quit.
    if selection == 1:
      add_person()
    elif selection == 2:
      delete_person()
    elif selection == 3:
      search_person()
    elif selection == 4:
      update_person()
    # Save, print goodbye message, quit
    elif selection == 5:
      save_quit()
      break

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()