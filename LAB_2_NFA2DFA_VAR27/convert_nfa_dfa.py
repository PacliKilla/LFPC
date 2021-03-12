
from collections import OrderedDict

# We use the json format as our input and output file format
import json
with open('nfa_input.json') as file:
    data = json.load(file)



dfa_symbols = data["nfa_symbols"]
dfa_start_state = data["start_state"]

Q_set = []
Q_set.append((dfa_start_state,))


# Import and record the transition rules for NFA machine
nfa_trans = {}
for trans in data["sigma_function"]:
    nfa_trans[(trans[0], trans[1])] = trans[2]

dfa_trans = {}

# Iterate through the state-symbol pair in the Q', add new states set into Q' when we never seen it before.
for input_state in Q_set:
    for symbol in dfa_symbols:

        # Adding state-symbol pair transition from NFA to DFA if the input state is already in NFA (not a newly formed state)
        if len(input_state) == 1 and (input_state[0], symbol) in nfa_trans:

            dfa_trans[(input_state, symbol)] = nfa_trans[(input_state[0], symbol)]

            if tuple(dfa_trans[(input_state, symbol)],) not in Q_set:
                Q_set.append(tuple(dfa_trans[(input_state, symbol)]),)

        # else we got a newly-formed state or we never saw this input state-symbol pair before
        else:
            output_set = []
            # Then we will combine all output states as a newly formed states and add it to Q' later
            for n_state in input_state:
                if (n_state, symbol) in nfa_trans and nfa_trans[(n_state, symbol)] not in output_set:
                    output_set.append(nfa_trans[(n_state, symbol)])

            output_set_combined = []
            if output_set:
                for i in output_set:
                    for j in i:
                        if j not in output_set_combined:
                            output_set_combined.append(j)

                dfa_trans[(input_state, symbol)] = list(sorted(output_set_combined))
                if tuple(sorted(output_set_combined),) not in Q_set:
                    Q_set.append(tuple(sorted(output_set_combined),))



dfa_states = set()
for given, out in dfa_trans.items():
    temp_s = given[0]
    if temp_s not in dfa_states:
        dfa_states.add(temp_s)
dfa_num_states = len(dfa_states)



dfa_sigma = []
for given, out in dfa_trans.items():
    temp_l = [[given[0], given[1], out]]
    dfa_sigma.extend(temp_l)


# Identify and add final states for DFA. Using the rule that if a states set in DFA include some final state in NFA, we should mark it as final state for DFA
dfa_final_state = set()
for dfa_states_set in Q_set:
    for nfa_final_state in data["final_state"]:
        if nfa_final_state in dfa_states_set:
            dfa_final_state.add(dfa_states_set)
dfa_final_state = list(dfa_final_state)


# Organize the conversion results and write them to the output csv file
dfa = OrderedDict()
dfa["dfa_states"] = dfa_num_states
dfa["dfa_symbols"] = dfa_symbols
dfa["sigma_function"] = dfa_sigma
dfa["start_state"] = dfa_start_state
dfa["final_state"] = dfa_final_state

output_file = open('dfa_output.json', 'w+')
json.dump(dfa, output_file, separators=(',\t', ':'))



