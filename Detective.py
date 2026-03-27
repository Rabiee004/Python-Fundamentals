import pickle

def display_menu():
    print("---- Menu ----")
    print("1) Add suspect")           
    print("2) Add accomplice")
    print("3) Display all suspects")
    print("4) Find potential accomplices")
    print("E) Exit")

def display_suspect(suspect, graph):
    print(f"{suspect}:")
    for i in graph[suspect]:
        print(f"    {i}")           


def display_all_suspects(graph):
    print("---- All suspects ----")
    for suspect in graph:
        display_suspect(suspect, graph)
        
               


def find_potential_accomplices(suspect, graph):
    accomplices = graph[suspect]
    friends_of_friends = set()
    for friend in accomplices:
        friends_of_friends.update(graph[friend])
    friends_of_friends = friends_of_friends.difference(accomplices)
    friends_of_friends.discard(suspect)
    potential = {suspect: friends_of_friends}
    return potential


def display_potential_accomplices(suspect, graph):
    potential = find_potential_accomplices(suspect, graph)
    print("---- Potential accomplices ----")
    print("Already known accomplices:")
    display_suspect(suspect, graph)
    print()
    print("Potential new accomplices:")
    display_suspect(suspect, potential)
    print()
    



                
def load_from_file(filename):
    with open(filename, 'rb') as file:
        graph = pickle.load(file)   
    return graph      

def save_to_file(graph, filename):
    with open(filename, 'wb') as file:  
        pickle.dump(graph, file)          
def main():
    filename = input("Enter a filename: ")
    try:
        graph = load_from_file(filename)
        print("*** Graph loaded from file. ***")
    except FileNotFoundError:
        graph = {}
        print("*** File not found. Starting with empty graph. ***")
    keep_running = True
    while keep_running:
        display_menu()
        choice = input("Enter your choice: ").lower()
        if choice == "1":
            suspect = input("Enter a suspect: ")
            graph[suspect] = set()
        elif choice == "2":
            suspect = input("Enter a suspect:")
            accomplice = input("Enter an accomplice: ")
            graph[suspect].add(accomplice)
            graph[accomplice].add(suspect)
        elif choice == "3":
            display_all_suspects(graph)
        elif choice == "4":
            suspect = input("Enter the name of a suspect: ")
            display_potential_accomplices(suspect, graph)
        elif choice == "e":
            keep_running = False   
        
         


if __name__ == '__main__':
    main()
    