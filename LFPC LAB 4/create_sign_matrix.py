from create_simple_precedence_matrix import *

def get_objects_rule1(right): #A->aB  a=B
    sign_matrix_objects = [] #composed of objects in form of dictionary
    if(len(right)>1):
        for i in range(len(right)-1):
            sign_matrix_object = {}
            sign_matrix_object["x1"] = right[i]
            sign_matrix_object["sign"] = "="
            sign_matrix_object["x2"] = right[i+1]
            sign_matrix_objects.append(sign_matrix_object)
    return sign_matrix_objects

def get_objects_rule2(right): #tN t<First(N)
    sign_matrix_objects = [] #composed of objects in form of dictionary
    if(len(right)>1):
        for i in range(len(right)-1):
            if right[i] in get_terminals() and right[i+1] in get_nonterminals(): #check if tN
                for first in get_first_of_nonterminal(right[i+1]):
                    sign_matrix_object = {}
                    sign_matrix_object["x1"] = right[i]
                    sign_matrix_object["sign"] = "<"
                    sign_matrix_object["x2"] = first
                    sign_matrix_objects.append(sign_matrix_object)
    return sign_matrix_objects

def get_objects_rule3(right): #Nt Last(N)>t
    sign_matrix_objects = [] #composed of objects in form of dictionary
    if(len(right)>1):
        for i in range(len(right)-1):
            if right[i] in get_nonterminals() and right[i+1] in get_terminals(): #check if Nt
                for last in get_last_of_nonterminal(right[i]):
                    sign_matrix_object = {}
                    sign_matrix_object["x1"] = last
                    sign_matrix_object["sign"] = ">"
                    sign_matrix_object["x2"] = right[i+1]
                    sign_matrix_objects.append(sign_matrix_object)
    return sign_matrix_objects

def get_objects_rule4(right): #N1N2 Last(N1)>Last(N2)&T
    sign_matrix_objects = [] #composed of objects in form of dictionary
    if(len(right)>1):
        for i in range(len(right)-1):
            if right[i] in get_nonterminals() and right[i+1] in get_nonterminals(): #check if NN
                for last in get_last_of_nonterminal(right[i]):
                    for specific_first in list(set(get_first_of_nonterminal(right[i+1]))&set(get_terminals())):
                        sign_matrix_object = {}
                        sign_matrix_object["x1"] = last
                        sign_matrix_object["sign"] = ">"
                        sign_matrix_object["x2"] = specific_first
                        sign_matrix_objects.append(sign_matrix_object)
    return sign_matrix_objects

def get_sign_matrix_obj():
    sign_matrix = {}
    sign_matrix["matrix"] = []
    for production in get_productions():
        for left,right in production.items(): # left and right part of production
            sign_matrix["matrix"] += get_objects_rule1(right)
            sign_matrix["matrix"] += get_objects_rule2(right)
            sign_matrix["matrix"] += get_objects_rule3(right)
            sign_matrix["matrix"] += get_objects_rule4(right)

    return sign_matrix

print("\nSigh matrix is given below:")
pprint(get_sign_matrix_obj())
