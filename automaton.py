#Arithmetic Language Automaton

class Automaton:
    def __init__(self):
        self._states = ['s','q1','q2','q3','q4','q5','j']
        self._start_state = 's'
        self._jail_state = 'j'
        self._accepting_states = ['q1','q5']
        self._stack = []
        self._current_state = self._start_state
        self._nums = ['0','1','2','3','4','5','6','7','8','9']
        self._alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self._operators = ['+','-','*','/','%','^']

    def get_current_state(self):
        return self._current_state
    
    def get_start_state(self):
        return self._start_state
    
    def get_jail_state(self):
        return self._jail_state

    def transition(self, character, state):
        if state == 's':
            if (character in self._nums) or (character in self._alpha):
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            elif character == '-':
                return 'q3'
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
            if (character in self._nums) or (character in self._alpha):
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            else:
                return 'j'
        elif state == 'q3':
            if (character in self._nums) or (character in self._alpha):
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            else:
                return 'j'
        elif state == 'q4':
            if (character in self._nums) or (character in self._alpha):
                return 'q1'
            elif character == '(':
                self._stack.append('P')
                return 'q2'
            elif character == '-':
                return 'q3'
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
                
        return state

    def check(self, state):
        if (state in self._accepting_states) and (len(self._stack) == 0):
            return 'ACCEPTED'
        else:
            return 'REJECTED'