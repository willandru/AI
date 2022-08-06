% Ro = Robot
% Ca = Caja Amarilla
% Cv = Caja Verde
% P = Pinza
% h1 = habitacion 1
% h2 = habitacion 2
% Nodo = (Ro,Ca,Cv,P)
%Pinza puede estar vacia 'e' llevar caja amarilla 'a' o llevar caja verde 'v'
%Integrantes : Felipe Ariza, William Rodriguez, William Gomez



%Acciones

cojerCa([Ro,Ca,Cv,P], Nodo_Actual):-(Ro==Ca), (P==e), Nodo_Actual = [Ro,Ca,Cv,a]. %Caja amarilla en pinza
cojerCv([Ro,Ca,Cv,P], Nodo_Actual):-(Ro==Cv), (P==e), Nodo_Actual = [Ro,Ca,Cv,v]. %Caja verde en pinza

soltarCa([Ro,Ca,Cv,P], Nodo_Actual):-(Ro==Ca), (P==a), Nodo_Actual = [Ro,Ro,Cv,e]. %Caja amarilla se encuentra en el robot
soltarCv([Ro,Ca,Cv,P], Nodo_Actual):-(Ro==Cv), (P==v), Nodo_Actual = [Ro,Ca,Ro,e]. %Caja verde se encuentra en el robot

pasar([Ro,Ca,Cv,P], Nodo_Actual):-(Ro==h1), (P==a),Nodo_Actual = [h2,h2,Cv,P];(Ro==h1), (P==v), Nodo_Actual = [h2,Ca,h2,P];(Ro==h1), (P==e), Nodo_Actual = [h2,Ca,Cv,P].
pasar([Ro,Ca,Cv,P], Nodo_Actual):-(Ro==h2), (P==a),Nodo_Actual = [h1,h1,Cv,P];(Ro==h2), (P==v), Nodo_Actual = [h1,Ca,h1,P];(Ro==h2), (P==e), Nodo_Actual = [h1,Ca,Cv,P].

%Costos

costoRobot([Ro_i,_,_,_],[Ro_f,_,_,_], Costo):- (Ro_i==Ro_f), Costo is 0.
costoRobot([Ro_i,_,_,_],[Ro_f,_,_,_], Costo):- (Ro_i\==Ro_f), Costo is 1.

costoCa([_,Ca_i,_,_],[_,Ca_f,_,_], Costo):- (Ca_i==Ca_f), Costo is 0.
costoCa([_,Ca_i,_,_],[_,Ca_f,_,_], Costo):- (Ca_i\==Ca_f), Costo is 1.

costoCv([_,_,Cv_i,_],[_,_,Cv_f,_], Costo):- (Cv_i==Cv_f), Costo is 0.
costoCv([_,_,Cv_i,_],[_,_,Cv_f,_], Costo):- (Cv_i\==Cv_f), Costo is 1.

costoPinza([_,_,_,P_i],[_,_,_,P_f],Dif):- (P_i==P_f), Dif is 0.
costoPinza([_,_,_,P_i],[_,_,_,P_f],Dif):- (P_i\==P_f), Dif is 1.

%Heuristica

heuristica(Nodo_Actual, Goal, Costo, Ro,Ca,Cv,P):-
    costoRobot(Nodo_Actual,Goal,Ro),
    costoCa(Nodo_Actual,Goal,Ca),
    costoCv(Nodo_Actual,Goal,Cv),
    costoPinza(Nodo_Actual,Goal,P),
    Costo is Ro+Ca+Cv.


%Estados presentes, se realiza la creacion del nodo y se le asigna un padre
state_record(State, Parent, Goal, Heuristica, Padre, [State, Parent, Goal, Heuristica, Padre]).
precedes([_,_,_,_,F1], [_,_,_,_,F2]) :- F1 =< F2.   


%Incializacion de las colas, donde se podran ver cada estado.
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



go(Start, Goal) :-
    empty_set(Closed),
    empty_sort_queue(Empty_open),
    heuristica(Start, Goal, H,_,_,_,_),
    state_record(Start, nil, 0, H, H, Root),
    insert_sort_queue(Root, Empty_open, Open),
    path(Open,Closed, Goal).

%Si Open esta vacio es porque no se encontro solucion
path(Open, _,_) :-
       empty_sort_queue(Open),
       write('No se encontro solucion.').

%Imprime la lista de estados visitados si hay en la cola
path(Open, Closed, Goal) :-
    remove_sort_queue(First_record, Open, _),
    state_record(State, _, _, _, _, First_record),
    State = Goal,
    write('Solucion: '), nl,
    imprimir(First_record, Closed).

%Se realiza backtracking en caso de que no se encuentra la solucion en un nodo hijo este se añade
path(Open, Closed, Goal) :-
    remove_sort_queue(First_record, Open, Rest_of_open),
    (bagof(Child, moves(First_record, Open, Closed, Child, Goal), Children);Children = []),
    insert_list(Children, Rest_of_open, New_open),
    add_to_set(First_record, Closed, New_closed),
    imprimir(First_record, Closed),
    path(New_open, New_closed, Goal),!.

%moves se encarga de generar hijos nuevos y calcula la heuristica
moves(State_record, Open, Closed, Child,Goal):-
    state_record(State,_,G,_,_,State_record),
    pasar(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).


moves(State_record, Open, Closed, Child,Goal):-
    state_record(State,_,G,_,_,State_record),
    cojerCa(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).

moves(State_record, Open, Closed, Child,Goal):-
    state_record(State,_,G,_,_,State_record),
    cojerCv(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).

moves(State_record, Open, Closed, Child,Goal):-
    state_record(State,_,G,_,_,State_record),
    soltarCa(State, Next),
    % not(unsafe(Next)),
    state_record(Next, _, _, _, _, Test),
    not(member_sort_queue(Test, Open)),
    not(member_set(Test, Closed)),
    G_new is G + 1,
    heuristica(Next, Goal, H,_,_,_,_),
    F is G_new + H,
    state_record(Next, State, G_new, H, F, Child).

moves(State_record, Open, Closed, Child,Goal):-
    state_record(State,_,G,_,_,State_record),
    soltarCv(State, Next),
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