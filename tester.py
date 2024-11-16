#Automaton Tester

from automaton import Automaton

def main():
    print('')
    input_string = '1+1'

    machine = Automaton()

    for i in input_string:
        print(machine.get_current_state() + ", " + i + " -> ", end='')
        print(machine.transition(i))
    print(machine.check())

main()