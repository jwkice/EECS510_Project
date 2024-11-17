#Automaton Tester

from automaton import Automaton

def test_string(string, machine):
    print(string)
    state_sequence = []
    state_sequence.append(machine.get_start_state())
    for i in string:
        if (state_sequence[-1] == machine.get_jail_state()):
            break
        else:
            state_sequence.append(machine.transition(i, state_sequence[-1]))
    
    if (machine.check(state_sequence[-1])):
        print('Accepted')
        for i in range(len(state_sequence)-1):
            print(f'{state_sequence[i]}, {string[i]} -> {state_sequence[i+1]}')
    else:
        print('Rejected')
        for i in range(len(state_sequence)-1):
            print(f'{state_sequence[i]}, {string[i]} -> {state_sequence[i+1]}')

def main():
    mode = input("Select mode - (f)ile or (u)ser:")
    if mode == 'f':
        input_file = open(input("Enter file name: "), 'r')
        for line in input_file:
            test_string(line.strip(), Automaton())
    elif mode == 'u':
        continue_loop = True
        while continue_loop:
            input_string = input("Enter test string (to quit, enter 'quit'):")
            if input_string == 'quit':
                continue_loop = False
            else:
                test_string(input_string, Automaton())
    else:
        print("Invalid mode selection.")

main()