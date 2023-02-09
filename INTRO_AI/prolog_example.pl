padre(juan,ana).
padre(juan,pedro).
padre(pedro,sofia).
hijo(H,P) :- padre(P,H).
abuelo(A,N) :- padre(P,N), padre(A,P).