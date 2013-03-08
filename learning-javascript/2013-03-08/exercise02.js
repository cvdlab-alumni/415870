function pushToArrayRandomly(n) {
    var a = [];
    for (var i = 0; i < n; i++)
        a.push(Math.floor(Math.random()*101));	//interi tra 0 e 101
    return a;
}

function filterEven(item, index, array) {
    return (item % 2 !== 0);
}

function compare(n1, n2){
	return n1-n2;	//>0 se n1>n2, <0 se n1<n2
}

function exercise02(n){
	return pushToArrayRandomly(n).
		filter(filterEven).
		sort(compare);
}