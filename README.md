# LFPC
LAB1 - DESCRIPTION 
First of all we need to add our grammar to the RG.txt, for me it is:

A B
a b c
S
S->aA|bB
A->bS|cA|aB
B->aB|b 

Next in the compiler itself when we run it we read the grammar from the txt and we can check to see non-terminals, terminals, productions of given non-terminal, all productions,
check if regular, and lastly convert to finite automaton.

