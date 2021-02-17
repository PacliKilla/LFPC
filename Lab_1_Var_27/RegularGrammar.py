class RegularGrammar:

    def __init__(self):
        self._nonTerminals = []
        self._terminals = []
        self._productions = {}
        self._startingSymbol = None

    @property
    def nonTerminals(self):
        return self._nonTerminals

    @property
    def terminals(self):
        return self._terminals

    @property
    def productions(self):
        return self._productions

    @property
    def startingSymbol(self):
        return self._startingSymbol

    def productionsForNonTerminal(self, non_terminal):
        if non_terminal in self._productions.keys():
            return self._productions[non_terminal]

    def checkIfRegular(self):
        res = True
        is_in_starting = False
        if 'epsilon' in self._productions[self._startingSymbol]:
            is_in_starting = True
        for key, value in self._productions.items():
            for rhs in value:
                if key != self._startingSymbol and rhs == 'epsilon' and is_in_starting:
                    res = False
                elif key != self._startingSymbol and len(rhs) == 2 and rhs[1] == self.startingSymbol and is_in_starting:
                    res = False
                elif len(rhs) == 1 and rhs.isupper():
                    res = False
                elif len(rhs) == 2 and (rhs[0].isupper() or rhs[1].islower()):
                    res = False
                elif len(rhs) > 2 and rhs != 'epsilon':
                    res = False
        return res

    def convertToAutomata(self, finiteAut):
        if not self.checkIfRegular():
            print("The grammar is not regular")
            return
        states = self._nonTerminals
        states.append('K')
        alphabet = self._terminals
        finiteAut.initial_state = self.startingSymbol
        print(self.startingSymbol)
        finiteAut.final_states = ['K']
        transitions = {}
        for key, value in self._productions.items():
            for rhs in value:
                if key == finiteAut.initial_state and rhs == 'epsilon':
                    finiteAut.final_states.append(finiteAut.initial_state)
                elif len(rhs) == 2:
                    k = (key, rhs[0])
                    temp = [rhs[1]]
                    transitions[k] = temp
                elif len(rhs) == 1:
                    k = (key, rhs)
                    temp = ['K']
                    transitions[k] = temp

        finiteAut.transitions = transitions
        finiteAut.states = states
        finiteAut.alphabet = alphabet

        return finiteAut


    @staticmethod
    def productionToDictionary(productions):
        temp = {}
        for production in productions:
            production_split = production.split('->')
            non_terminal = production_split[0]
            rhs = production_split[1].split('|')
            temp[non_terminal] = rhs
        return temp

    def readFromFile(self, filename='rg.txt'):
        with open(filename, 'r') as f:
            lines = f.readlines()
            stripped_lines = []
            for line in lines:
                stripped_lines.append(line.strip('\n'))
            lines = stripped_lines
            self._nonTerminals = lines[0].split(' ')
            self._terminals = lines[1].split(' ')
            self._startingSymbol = lines[2].strip()
            productions = lines[3:]
            self._productions = self.productionToDictionary(productions)
            self._nonTerminals.append(self._startingSymbol)

    @startingSymbol.setter
    def startingSymbol(self, value):
        self._startingSymbol = value

    @nonTerminals.setter
    def nonTerminals(self, value):
        self._nonTerminals = value

    @terminals.setter
    def terminals(self, value):
        self._terminals = value

    @productions.setter
    def productions(self, value):
        self._productions = value
