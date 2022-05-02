# ALARM NETWORK (A bAYESIAN nETWORK)

# B(burglary), E(earthquake), A(alarm)
variable('B', [0,1])
variable('E',  [0,1])
variable('A', [0,1])

#samll probability of somethin happening
factor('fB', 'B', {0:0.95, 1:0.05})
factor('fE', 'E', {0: 0.95, 1: 0.05})


#If something happens
factor('fB', 'B E A', function(b,e,a){
	return (b||e) == (a==1);
	})

#Alarm went off: B,E no longer independent
# condition('A', 1)

# NO earthquake: explaining away phenomenon
# condition('E', 1)

query('B')  # Was there a Bulgary?

sumVariableElimination({order: 'A E'})