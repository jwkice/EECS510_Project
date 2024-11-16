#Automaton Tester

from automaton import Automaton

def main():
    print('\n')
    input_string = '1+1'

    machine = Automaton()

    for i in input_string:
        machine.transition(i)
    result = machine.check()
    print(result)

main()