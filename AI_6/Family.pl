father(santosh, rakul).
father(ramesh, radhika).

mother(radhika, rakul).
mother(anuradha, radhika).

mother_brother(radhika, rama).
mother_sister(tejaswini, radhika).

grand_father(Y,X) :- father(Y,Z), mother(Z,X).
grand_mother(Y,X) :- mother(Y,Z), mother(Z,X).

father_brother(santosh, rajesh).
father_brother(santosh, upendra).

wife(prajakta, rajesh).
wife(lalita, upendra).

uncle(Y,X) :- father_brother(Z,Y), father(Z,X).
aunt(W,X)  :- wife(W,Y), father_brother(Z,Y), father(Z,X).
mama(Y,X) :-  mother_brother(Z, Y), mother(Z, X).
maasi(Y,X) :- mother_sister(Y, Z), mother(Z, X).







