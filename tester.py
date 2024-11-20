#Tester
'''
Name: EECS 510 Formal Language Project Automaton Tester
Author: Jacob Kice
Date Created: 11/16/2024
Date Modified: 11/20/2024
Function test_string uses the provided machine to test the validity of
    the given string. It maintains a list of states, in the order of
    occurance. For each character in the string, test_string first
    checks if the last state reached is a jail state. If so, the loop
    breaks. If not, test_string calls the machine's transition function
    for the current character and the last state, and appends the new
    state returned by transition to the end of the list. Once the string
    is processed, test_string checks if the string was accepted using
    the machine's check function. Then, it prints out the acceptance 
    result and the sequence of state transitions. Finally, test_string
    returns the result to be used for comparison against the expected
    result.
Function main allows the user to specify what type of input mode,
    file or user. File mode reads from inputs from a user 
    specified file. User mode takes direct input from the user for
    testing. Both modes call the test_string function on the string
    to check its validity. File mode also checks the result of each
    test case based on the expected results included in the test
    file. In the expected format of the test file, each line in the
    file is one test, which is treated as a whitespace seperated 
    list. The first index of the list is assumed to be the test string
    and the second index is assumed to be the expected result. Valid
    expected results are 'ACCEPTED' and 'REJECTED'. If the second
    index is not one of those options, the test will always be marked
    as 'Failure' regardless of the machine output. If the second
    index is not found, the result comparison is marked as Inconclusive.
    Any indices after the second are simply ignored.
'''

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