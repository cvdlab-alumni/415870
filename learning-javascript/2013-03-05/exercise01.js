var i;
var j;
var a;
for (j=1; j<=10;j++){
	a = "";
	for (i = 1; i <= 10; i +=1) {
  		a += j*i+"\t";
	}
	console.log(a+"\n")
}