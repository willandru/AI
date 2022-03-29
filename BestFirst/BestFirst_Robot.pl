
en(r,h2).
en(a,h2).
en(v,h2).

en(r,h2):- r is 1.
en(a,h2):- a is 1.
en(v,h2):- v is 1.

estado_inicial=[r,a,v].
estado_final=[0,0,1].

pasar(h1):- en(robt,h2), r is 0.
pasar(h2):- r is 1.
coger(a):- a is 2.
coger(b):- b is 2.
soltar(a,h1):- a is 0.
soltar(b,h1):- b is 0.
soltar(a,h2):- a is 1.
soltar(b,h2):- b is 1.





% %Inicial:Hay un robot en la habitación 2, junto con una caja verde y una caja amarilla.
% %Final: Hay un robot en la habitación 1 junto con la caja amarilla, la caja verde esta en la habitación 2.

inicial(1,1,1).
final(0,0,1).

coger(Caja):- 
