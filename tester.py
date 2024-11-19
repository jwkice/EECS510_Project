#Automaton Tester

from automaton import Automaton

def test_string(string, machine):
    print(f'\nInput string: {string}')
    state_sequence = []
    state_sequence.append(machine.get_start_state())
    for i in string:
        if (state_sequence[-1] == machine.get_jail_state()):
            break
        else:
            state_sequence.append(machine.transition(i, state_sequence[-1]))
    
    result = machine.check(state_sequence[-1])
    print(f'Result: {result}')
    print('State sequence:')
    for i in range(len(state_sequence)-1):
        print(f'\t{state_sequence[i]}, {string[i]} -> {state_sequence[i+1]}')
    return result

def main():
    mode = input("Select mode - (f)ile or (u)ser:")
    if mode == 'f':
        input_file = open(input("Enter file name: "), 'r')
        for line in input_file:
            line_list = line.split()
            if len(line_list) >= 2:
                if test_string(line_list[0], Automaton()) == line_list[1]:
                    print('Test Result: Success')
                else:
                    print('Test Result: Failure')
            else:
                test_string(line_list[0], Automaton())
                print('Test Result: Inconclusive: No expected result')
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