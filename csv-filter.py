from os.path import exists

def main():
    # Variables
    first_name = []
    last_name = []
    dob = []
    indices = []

    # Finds file
    name = input("Enter name of file: ")
    if not(exists(name)):
        print("File does not exist")
        return
    f = open(name, "r")
    f.readline()

    # Splits file into first_name, last_name, and dob array
    for x in f:
        temp = x.strip().split(",")
        first_name.append(temp[0])
        last_name.append(temp[1])
        dob.append(temp[2])
    
    # Filters indexes of searched terms
    filter_type = input("Enter first name (first), last name (last), date of birth (dob): ").lower()
    term_search = input("Enter term to search for: ").lower()
    if (filter_type == "first"):
        append_search_index_to_list(first_name, term_search, indices)
    elif (filter_type == "last"):
        append_search_index_to_list(last_name, term_search, indices)
    else:
        dob_year_only = []
        for x in range(len(dob)):
            dob_year_only.append(dob[x][0:4])
        append_search_index_to_list(dob_year_only, term_search, indices)
    
    # If search not found
    if len(indices) == 0:
        print("No results found")
        return 

    # Prints searched indexes
    for x in indices:
        print(first_name[x] + " " + last_name[x] + " " + dob[x])

def append_search_index_to_list(list_to_search, search_term, list_to_add):
    for x in range(len(list_to_search)):
        if list_to_search[x].lower() == search_term:
            list_to_add.append(x)

main()
