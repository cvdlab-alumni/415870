var i;
var j;
var a;
for (j=1; j<=10;j++){
	a = "";
	for (i = 1; i <= 10; i +=1) {
		if (i === j)
			a+= "1";
		else
			a+= "0";
		if (i === 10)
			a += "\t";	 
		else
			a += ",\t";
	}
	console.log(a+"\n")
}