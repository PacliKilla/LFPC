from read_string_and_grammar import *

def extract_first_from_right(first_array,symbol): #finds a first from first symbol of the right part
    if symbol in get_terminals() and symbol not in first_array:
        first_array.append(symbol) #symbol should be terminal and not present in first_array
    elif symbol in get_nonterminals() and symbol not in first_array:
        first_array.append(symbol)
        find_first(first_array,symbol) #symbol should be nonterminal and not present in first array

def find_first(first_array,nonterminal): # finds all firsts refering to a nonterminal
    for production in get_productions():
        for left, right in production.items(): #left and right side of production
            if(left == nonterminal):
                extract_first_from_right(first_array,right[0])

def extract_last_from_right(last_array,symbol): #finds a last from last symbol of the right part
    if symbol in get_terminals() and symbol not in last_array:
        last_array.append(symbol) #symbol should be terminal and not present in last_array
    elif symbol in get_nonterminals() and symbol not in last_array:
        last_array.append(symbol)
        find_last(last_array,symbol) #symbol should be nonterminal and not present in first array

def find_last(last_array,nonterminal): # finds all lasts refering to a nonterminal
    for production in get_productions():
        for left, right in production.items(): #left and right side of production
            if(left == nonterminal):
                extract_last_from_right(last_array,right[-1])

def get_simple_precedent_matrix(): # creates and return it
    simple_presedence_matrix = {}
    for nonterminal in get_nonterminals():
        first_array = []
        last_array = []
        find_first(first_array,nonterminal)
        find_last(last_array,nonterminal)
        simple_presedence_matrix[nonterminal] = {"first": first_array,"last": last_array}
    return simple_presedence_matrix

def get_first_of_nonterminal(nonterminal):
    return get_simple_precedent_matrix()[nonterminal]["first"]

def get_last_of_nonterminal(nonterminal):
    return get_simple_precedent_matrix()[nonterminal]["last"]


# pprint(get_productions())
print("First Last Matrix is given below")
pprint(get_simple_precedent_matrix())
# array = []
# find_first(array,"A")
# find_last(array,"A")
# pprint(array)
