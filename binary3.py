from automata.fa.dfa import DFA

if __name__ == '__main__':
    dfa = DFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q1', '1': 'q2'}
        },
        initial_state='q0',
        final_states={'q0'}
    )

    inp_user = input()

    if dfa.accepts_input(inp_user) or inp_user == 'e':
        print('The DFA accepts the string ’'+inp_user+'’')
    else:
        print('The DFA rejects the string ’' + inp_user + '’')
