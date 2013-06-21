/*
DA WIKIPEDIA:
file obj
-elenco di vertici
-elenco di facets
*/

function exportLARmodelToObject(V, FV){
	var out ="";
	//set of vertexes
	for (var i = 0; i<V.length; i++){
		out += "v";
		for(var c = 0; c<V[i].length; c++){
			out += " "+ V[i][c];
		}
		out += "\n";
	}
	//set of facets
	for (var i = 0; i<FV.length; i++){
		out += "fv";
		for(var c = 0; c<FV[i].length; c++){
			out += " "+ FV[i][c];
		}
		out += "\n";
	}
	return out;
}

//=====================  TEST  ====================================================
//esempio di istanza
fv = [[5,6,7,8],
[0,5,8],
[0,4,5],
[1,2,4,5],
[2,3,5,6],
[0,8,7], [3,6,7], [1,2,3], [0,1,4]
];
v = [[0,6],
[0,0],
[3,0],
[6,0,4],
[0,3,4],
[3,3],
[6,3],
[6,6],
[3,6]];

exportLARmodelToObject(v,fv);