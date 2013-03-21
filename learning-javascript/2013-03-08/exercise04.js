function select(data, key, values){
	var result = []
	for (i = 0; i < values.length; i++){
		s = data.filter(function(item, index, array){
 			return (item[key] === values[i]);	//risultati per l'i-esimo valore di values
		});
		result = result.concat(s);
	}
	return result;
}

var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var values = ['goofy', 'scrooge'];

function best_select (data, key, values) {
	return data.filter(function (item_data) {
		return values.some(function (item_values) {
			return item_data[key] === item_values;
		})
	})
}