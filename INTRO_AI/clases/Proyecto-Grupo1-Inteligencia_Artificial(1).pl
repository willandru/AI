% Estados
% R: Robot
% A: Caja 1
% a: Caja 1
% V: Caja 2
% v: Caja 2
% P: Pinza
% h1: Habitacion 1, si el objeto o robot se encuentra en la izquierda
% h2: Habitacion 2, si el objeto o robot se encuentra en la derecha
% e: La pinza no sostiene ningún elemento


%Estados
state_record(State, Parent, G, H, F, [State, Parent, G, H, F]).
precedes([_,_,_,_,F1], [_,_,_,_,F2]) :- F1 =< F2.

go(Start, Goal) :-
    empty_set(Closed),
    empty_sort_queue(Empty_open),
    heuristica(Start, Goal, H,_,_,_,_),
    state_record(Start, nil, 0, H, H, First_record),
    insert_sort_queue(First_record, Empty_open, Open),
    path(Open,Closed, Goal).

%Open está vacío; no se encontro solución
path(Open_pq, _,_) :-
       empty_sort_queue(Open_pq),
       write('No hay solucion.').


%El siguiente record es la meta, 
%Imprime la lista de los estados que han sido visitados
path(Open, Closed, Goal) :-
    remove_sort_queue(First_record, Open, _),
    state_record(State, _, _, _, _, First_record),
    State = Goal,
    write('Solucion: '), nl,
    imprimir(First_record, Closed).


%El siguiente record no es igual a la meta
%Genera el hijo, se agrega a Open y continúa 
path(Open, Closed, Goal) :-
    remove_sort_queue(First_record, Open, Rest_of_open),
    (bagof(Child, moves(First_record, Open, Closed, Child, Goal), Children);Children = []),
    insert_list(Children, Rest_of_open, New_open),
    add_to_set(First_record, Closed, New_closed),
    imprimir(First_record, Closed),
    path(New_open, New_closed, Goal),!.


%Movimientos generan todos los hijos de un estado que no están listos aún
%Es usado para ver si los siguientes estados ya han pasado por Open o Closed
moves(State_record, Open, Closed,Child, Goal) :-
    state_record(State, _, G, _,_, State_record),
    pasar(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).

moves(State_record, Open, Closed,Child, Goal) :-state_record(State, _, G, _,_, State_record),
    cogerA(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).

moves(State_record, Open, Closed,Child, Goal) :-
    state_record(State, _, G, _,_, State_record),
    soltarA(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).

moves(State_record, Open, Closed,Child, Goal) :-
    state_record(State, _, G, _,_, State_record),
    cogerV(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).


moves(State_record, Open, Closed,Child, Goal) :-
    state_record(State, _, G, _,_, State_record),
    soltarV(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).


%Inserta una lista de estados obtenidos por un llamado
%Y los inserta en un queue, una a la vez
insert_list([], L, L).
insert_list([State | Tail], L, New_L) :-
    insert_sort_queue(State, L, L2),
    insert_list(Tail, L2, New_L).

empty_set([]).  
empty_sort_queue([]). 
insert_sort_queue(State, [], [State]).
insert_sort_queue(State, [H | T], [State, H | T]) :-
    precedes(State, H).
insert_sort_queue(State, [H|T], [H | T_new]) :-
    insert_sort_queue(State, T, T_new).
remove_sort_queue(First, [First|Rest], Rest).
add_to_set(X, S, [X|S]).
add_to_set(X, S, S) :- member(X, S), !.  
member_sort_queue(E, S) :- member(E, S). 
member_set(E, S) :- member(E, S). 


%imprime la solucion
imprimir(Next_record, _):-
    state_record(State, nil, _, _,_, Next_record),
    write(State), nl.

imprimir(Next_record, Closed) :-
    state_record(State, Parent, _, _,_, Next_record),
    state_record(Parent, _, _, _, _, Parent_record),
    member_set(Parent_record, Closed),
    imprimir(Parent_record, Closed),
    write(State), nl.




%Plan de acción que tiene el robot (Pasar, Coger y Soltar) para alcanzar una situación final deseada 
%El robot R debe trasladar cajas de colores (Caja A, Caja V declaradas como en el taller realizado en la clase)
%entre dos habitaciones (h1 y h2) que están conectadas por una puerta
%Pasar
pasar([R,A,V,P],In):-(R==h1), (P==a),In = [h2,h2,V,P];(R==h1), (P==v), In = [h2,A,h2,P];(R==h1), (P==e), In = [h2,A,V,P].
pasar([R,A,V,P],In):-(R==h2), (P==a),In = [h1,h1,V,P];(R==h2), (P==v), In = [h1,A,h1,P];(R==h2), (P==e), In = [h1,A,V,P].

%Coger
cogerA([R,A,V,P],In):-(R==A),(V\==v),(P==e),In=[R,A,V].
cogerV([R,A,V,P],In):-(R==V),(A\==v),(P==e),In=[R,A,V,v].

%Soltar
soltarA([R,A,V],In):-(R==A),In=[R,R,V].
soltarV([R,A,V],In):-(R==V),In=[R,A,R].

%Para definir los costos fue necesario realizar una búsqueda en internet
%donde explicara exactamente como funcionaban los operadores aritméticos en prolog
%por lo que nos guiamos de https://docplayer.es/13765867-1-el-vocabulario-de-un-programa-prolog.html
%Lo cual muestra que estos operadores de comparación están predefinidos por el lenguaje c
%Costos
%Para realizar los costos se utilizó como referencia https://www.swi-prolog.org/pldoc/man?predicate=%5C%3D%3D/2
%Tomando como guia la estructura para verificar si se ha llegado al final de una lista
%Pero, teniendo en cuenta https://www.uv.mx/personal/aguerra/files/2018/10/pia-slides-04.pdf
%Que explica la función costo cuando se mueve entre estados 

costoR([X,_,_,_],[Y,_,_,_],S):-(X\==Y),S is 1.
costoR([X,_,_,_],[Y,_,_,_],S):-(X==Y),S is 0.
costoA([_,X,_,_],[_,Y,_,_],S):-(X\==Y),S is 1.
costoA([_,X,_,_],[_,Y,_,_],S):-(X==Y),S is 0.

costoV([_,_,X,_],[_,_,Y,_],S):-(X\==Y),S is 1.
costoV([_,_,X,_],[_,_,Y,_],S):-(X==Y),S is 0.
costoPinzas([_,_,_,X],[_,_,_,Y],S):- (X\==Y), S is 1.
costoPinzas([_,_,_,X],[_,_,_,Y],S):- (X==Y), S is 0.


%Heuristica: La función puede ser una estimación de lo proximo 
%que se encuentra el estado de un estado objetivo 
%Asigna a cada estado un valor que es la distancia

heuristica(In, Fin, Costo, R,A,V,P):-costoR(In,Fin, R),costoA(In,Fin, A),costoV(In,Fin, V),costoPinzas(In,Fin, P),
    Costo is R+A+V+P.
 
%El algoritmo Best First Search se encontró y
% se usó como referencia 
% de la página: https://www.cs.unm.edu/~luger/ai-final/code/PROLOG.best.html
%Para resolver este proyecto tuvimos en cuenta el Capitulo 4: Production Systems and Search 
%Del libro Programming in Prolog material obtenido en la clase 
