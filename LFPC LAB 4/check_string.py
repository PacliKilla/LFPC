from create_sign_matrix import *

# def get_sign_matrix_obj():
#     with open('sign_matrix.json') as data_file:
#         return json.load(data_file)

def get_final_string(before_str):
    after_str = before_str.replace('$<', '$').replace('>$', '$').replace('$', '>$<')
    after_str = after_str[1:len(after_str) - 1:]
    for rule in data['matrix']:
        before = rule['x1'] + rule['x2']
        after = rule['x1'] + rule['sign'] + rule['x2']
        after_str = after_str.replace(before, after)
    return after_str

def replace_string(final_string, productions):
    end = final_string.index('>')
    cut_string = final_string[0:end + 1:1][::-1]
    begin = cut_string.index('<')
    selected_substring = cut_string[0:begin + 1:1][::-1]
    productions_value = selected_substring.replace('=', '')
    replace_value = ''
    for item in productions:
        for key, value in item.items():
            if '<' + value + '>' == productions_value:
                replace_value = key
    final_string = final_string.replace(selected_substring, replace_value)
    final_string = get_final_string(final_string)
    return final_string.replace('<>', '')


def check_final_string(final_string, productions):
    pprint(final_string)
    while final_string != '$$':
        final_string = replace_string(final_string, productions)
        pprint(final_string)
        if final_string == '$<' + get_start() + '>$':
            return True
    return False

data = get_sign_matrix_obj()
string = get_string()
final_string = get_final_string('$' + string + '$')
productions = get_productions()

# replace_string('d<i=A>v<i<a<a', productions)
# pprint(data)
print("\nYour String is: {}\n".format(string))
# pprint(final_string)
print("Your Productions are:")
pprint(productions)
print("\n Checking final string")
pprint(check_final_string(final_string, productions))
