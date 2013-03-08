function capitalizeFirstLetter (word){
	return word.charAt(0).toUpperCase().concat(word.slice(1,word.length).toLowerCase())
}

function capitalizeString (string){
	return string.split(" ").
		map(function(item, index, array){
   			return capitalizeFirstLetter (item)
		}).
		join(" ");
}
