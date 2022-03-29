quitar(X, [X|Ys], Ys).
quitar(X, [Y|Ys], [Y|Ys1]) :-
quitar(X,Ys,Ys1).