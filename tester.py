#Automaton Tester

from automaton import Automaton

def test_string(string):
    print(string)
    machine = Automaton()
    for i in string:
        print(machine.get_current_state() + ", " + i + " -> ", end='')
        print(machine.transition(i))
    print(machine.check())
    print('')

def main():
    mode = input("Select mode - (f)ile or (u)ser:")
    if mode == 'f':
        input_file = open(input("Enter file name: "), 'r')
        for line in input_file:
            test_string(line.strip())
    elif mode == 'u':
        continue_loop = True
        while continue_loop:
            input_string = input("Enter test string (to quit, enter 'quit'):")
            if input_string == 'quit':
                continue_loop = False
            else:
                test_string(input_string)
    else:
        print("Invalid mode selection.")

main()