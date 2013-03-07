function fibonacci (n){
	if (! (n in fibonacci)) { 	//uso la funzione come se fosse un oggetto
		fibonacci[n] = fibonacci(n-1) + fibonacci(n-2);
	}
	return fibonacci[n];		//la proprietà 'n' conterrà il valore di fibonacci(n)
}

fibonacci[0] = 0; 	//condizione base della ricorsione
fibonacci[1] = 1;