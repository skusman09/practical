man(lou).
man(pete).
man(ian).
man(peter).
man(ross).

woman(pauline).
woman(cathy).
woman(lucy).
woman(amy).

parent(ian,lucy).
parent(ian,peter).
parent(cathy,ian).
parent(pete, ian).
parent(lou,pete).
parent(lou,pauline).
parent(ross,amy).

mother(X, Y) :- woman(X), parent(X, Y), (X\=Y).
father(X, Y) :- man(X), parent(X, Y), (X\=Y).

sibling(X, Y) :- parent(Z, X),parent(Z, Y), (X\=Y).
brother(X, Y) :- man(X), sibling(X, Y), (X\=Y).
sister(X, Y) :- woman(X), sibling(X, Y), (X\=Y).

grandfather(X, Y) :- father(X, Z),parent(Z, Y), (X\=Y).
grandmother(X, Y) :- mother(X, Z),parent(Z, Y), (X\=Y).

ancestor(X, Y) :- parent(X, Y), (X\=Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y), (X\=Y).





################## OUTPUT ##################

Welcome to SWI-Prolog (threaded, 64 bits, version 9.2.5) SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software. Please run?- license. for legal details.

For online help and background, visit https://www.swi-prolog.org For built-in help, use?- help(Topic). or?- apropos(Word).

?-

% c:/role.pl compiled 0.00 sec, 25 clauses

?- father(A.ian).

A = pete.

?- mother(B,ian).

B = cathy.

?- grandfather(C,ian).

C = lou.

?- sibling(A.cathy).

false.

?- sibling(A,pauline).

A = pete.

?-brother(B.pauline).

B = pete