def exportLARmodelToObject (V, FV):
	out =""
	#set of vertexes
	for i in range(0,V.length):
		out += "v"
		for c in range(0,V[i].length):
			out += " "+ V[i][c]
		out += "\n"
	#set of facets
	for j in range(0,FV.length):
		out += "v"
		for d in range(0,FV[j].length):
			out += " "+ V[j][d]
		out += "\n"
	return out