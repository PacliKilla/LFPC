from FiniteAutomata import FiniteAutomat
from RegularGrammar import RegularGrammar


class UI:

    def __init__(self):
        self._regular_grammar = RegularGrammar()
        self._finite_automaton = FiniteAutomat()


    @staticmethod
    def print_rg_menu():
        print("1. Read from file")
        print("2. See non-terminals")
        print("3. See terminals")
        print("4. See productions of given non-terminal")
        print("5. See all productions")
        print("6. Check if regular")
        print("7. Convert to finite automaton")
        print("0. Back")

    def menu(self):
        running = True
        while running:
            self.regular_grammar_menu()

    def regular_grammar_menu(self):
        running = True
        while running:
            self.print_rg_menu()
            user_choice = (int(input("Your choice: ")))
            if user_choice == 1:
                self._regular_grammar.readFromFile()
            elif user_choice == 2:
                print(self._regular_grammar.nonTerminals)
            elif user_choice == 3:
                print(self._regular_grammar.terminals)
            elif user_choice == 4:
                non_terminal = input("Non-terminal: ")
                print(self._regular_grammar.productionsForNonTerminal(non_terminal))
            elif user_choice == 5:
                print(self._regular_grammar.productions)
            elif user_choice == 6:
                print(self._regular_grammar.checkIfRegular())
            elif user_choice == 7:
                self._regular_grammar.convertToAutomata(self._finite_automaton)
                print("Transitions: " + str(self._finite_automaton.transitions))
                print("Alphabet:  " + str(self._finite_automaton.alphabet))
                print("States: " + str(self._finite_automaton.states))
                print("Final states: " + str(self._finite_automaton.final_states))
                print("Initial state: " + str(self._finite_automaton.initial_state))
            elif user_choice == 0:
                running = False
            else:
                print("Invalid input")
