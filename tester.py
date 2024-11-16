#Automaton Tester

from automaton import Automaton

def main():
    print('')
    input_string = '1+1'

    machine = Automaton()

    for i in input_string:
        print(machine.transition(i), end=' ')
    print('')
    print(machine.check())

main()