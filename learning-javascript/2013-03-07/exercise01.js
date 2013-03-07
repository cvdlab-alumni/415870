function identity (n){
	var matrix = [];
	for (var i = 0; i<n; i++){
		matrix[i] = [];
	}
	for (var j=0; j<n; j++){
		for (i=0;i<n;i++){
			if (i === j)
				matrix[j][i]=1;
			else
				matrix[j][i]=0;
		}
	}
	return matrix;
}