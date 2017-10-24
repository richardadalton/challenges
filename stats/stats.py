import json

def show_menu():
    print()
    print("------------")
    print("    Menu")
    print("------------")
    print()
    print("1. Add a person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")
    print()
    option = input("Enter Option\n>")
    return option
  
def add_a_person():
    person = {}
    person['first_name'] = input("Enter first name: ")
    person['last_name'] = input("Enter last name: ")
    person['age'] = input("Enter age: ")
    person['team'] = input("Enter team: ")
    
    with open("people.txt", "a") as people_file:
        people_file.write(json.dumps(person) + "\n")

def load_people():
    people = []
    with open("people.txt", "r") as people_file:
        lines = people_file.read().splitlines()
        for line in lines:
            person = json.loads(line)
            people.append(person)
    return people    
  
  
def view_people():
    people = load_people()
    print("List Of People")  
    print("--------------")
    for person in people: 
        print ("{1}, {0} ({2}), Team: {3}".format(person['last_name'], person['first_name'], person['age'], person['team']))
    
def view_stats():
    people = load_people()
    
    team_lists = {}
    
    total_age = 0
    for person in people:
        total_age += int(person['age'])
    
        list = team_lists.get(person['team'], [])
        list.append(person)
        team_lists[person['team']] = list
    
    average_age = total_age / len(people)
    
    print("The number of people is {0}".format(len(people)))
    print("The average age is {0}".format(average_age))
    
    for team, players in team_lists.items():
        print(team)
        print(players)

def program_loop():
    while True:
        option = show_menu()
        
        if option == "1":
            add_a_person()
        elif option == "2":
            view_people()
        elif option == "3":
            view_stats()
        elif option == "4":
            break
        else:
            print("Invalid Option")
        
program_loop()
        
        
        