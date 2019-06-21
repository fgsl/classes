:- initialization(main).

main :-
    put(27),write('[2J'),ttyflush,
    write('Olá, eu sou Alfredo, em que posso ajudar?'),nl,
    get_code(C),
    write('Você disse:'),
    format('~c',C),nl, 
    halt.
