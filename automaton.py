#Arithmetic Language Automaton
'''
Name: EECS 510 Formal Language Project Automaton - Arithmetic Language
Author: Jacob Kice
Date Created: 11/16/2024
Date Modified: 11/19/2024
Function __init__ defines the state details: a list of all states, the start state,
    the jail state, and the accepting states. It also initializes the stack and
    defines the three character sets: numeral, alphabetic, and operator.
Function get_start_state returns the start state of the machine.
Function get_jail_state returns the jail state of the machine.
Function transition defines the transitions of the machine. It consists of a two
    level nested if-statement. The outer level identifies the current state, as
    passed by the caller. The inner level identifies the input character, also
    passed by the caller. Each case of the outer level represents the output
    transitions for its state in the machine, by defining the transitions from that
    state for each allowed input character, as well as handling the stack maintainance as
    needed. The nested if-statements also define jail state transitions for the
    input characters that do not have a specifically defined transition from the current
    state, using the else case on the inner if-statement.
Function check determines if the string is accepted or rejected by the machine by checking
    if the provided state is an accepting state and the stack is empty.
'''

class Automaton:
    def __init__(self):
        self._states = ['s','q1','q2','q3','q4','q5','q6','j']
        self._start_state = 's'
        self._jail_state = 'j'
        self._accepting_states = ['q1','q5']
        self._stack = []
        self._nums = ['0','1','2','3','4','5','6','7','8','9']
        self._alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self._operators = ['+','-','*','/','%','^']
    
    def get_start_state(self):
        return self._start_state
    
    def get_jail_state(self):
        return self._jail_state

    def transition(self, character, state):
        if state == 's':
            if character in self._nums:
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            elif character == '-':
                return 'q3'
            elif character in self._alpha:
                return 'q6'
            else:
                return 'j'
        elif state == 'q1':
            if character in self._nums:
                return 'q1'
            elif character in self._operators:
                return 'q4'
            elif (character == ')') and (len(self._stack) > 0) and (self._stack[-1] == 'P'):
                self._stack.pop()
                return 'q5'
            else:
                return 'j'
        elif state == 'q2':
            if character in self._nums:
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            elif character in self._alpha:
                return 'q6'
            else:
                return 'j'
        elif state == 'q3':
            if character in self._nums:
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            elif character in self._alpha:
                return 'q6'
            else:
                return 'j'
        elif state == 'q4':
            if character in self._nums:
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            elif character == '-':
                return 'q3'
            elif character in self._alpha:
                return 'q6'
            else:
                return 'j'
        elif state == 'q5':
            if character in self._operators:
                return 'q4'
            elif (character == ')') and (len(self._stack) > 0) and (self._stack[-1] == 'P'):
                self._stack.pop()
                return 'q5'
            else:
                return 'j'
        elif state == 'q6':
            if character in self._operators:
                return 'q4'
            elif (character == ')') and (len(self._stack) > 0) and (self._stack[-1] == 'P'):
                self._stack.pop()
                return 'q5'
            else:
                return 'j'
                
        return state

    def check(self, state):
        if (state in self._accepting_states) and (len(self._stack) == 0):
            return 'ACCEPTED'
        else:
            return 'REJECTED'