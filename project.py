#This is a python codes that shows the real time appended names of the list 

#create a main() function
def names():
    names_list = []
    
#create "again" variable to control the loop
    again = 1
    
    
#create a while loop    
    while again == 1:
        name = input('Enter a name: ')
        names_list.append(name)
        again = int(input("Do you want to append another name? Enter 1 for yes and any other integral for no: "))
        
    print("Here are the names you entered.")
    
#create a loop that assign the names from the "names_list" to "name" and then print it
    for name in names_list:
        print(name)

#call the main function
names()
