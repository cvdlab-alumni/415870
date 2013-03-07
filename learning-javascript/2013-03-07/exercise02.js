function fibonacci (n){
	if (! (n in fibonacci)) { 	//uso la funzione come se fosse un oggetto
		fibonacci[n] = n + fibonacci(n-1);
	}
	return fibonacci[n];		//la proprietà 'n' conterrà il valore di fibonacci(n)
}

fibonacci[0] = 0; 	//condizione base della ricorsione