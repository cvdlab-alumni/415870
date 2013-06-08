wood = [166.0/255, 128.0/255, 100.0/255];
green = [0, 100.0/255, 0];
ground = [92.0/255, 51.0/255 ,23.0/255];
dark_grey = [0.2, 0.2, 0.2]

var square_map_side = 30;	//min 40

var subsquare_side = 1;

var lake_depth = square_map_side*4/100 + 0.2;

function initialize(){
	getPoints3D();
}


function getRandomZ(z, offset){
	var num = offset*Math.random() -(offset/2);
	return z+num;
}

//genera una matrice di punti sul piano 2D uv
function generatePoints_uv(square_map_side, subsquare_side){
	var points = [];
	var i = 0;
	for (x = 0; x<=square_map_side; x=x+subsquare_side){
		points[i] = [];
		for (y = 0; y<=square_map_side; y=y+subsquare_side){
			points[i].push([x,y,0]);
		}
		i++;
	}
	return points;
}

function getPoints3D(){
	var mountains;
	var points = generatePoints_uv(square_map_side, subsquare_side);
	//ora tiro fuori il modello in 3D e modifico la z degli elementi della matrice.
	for (var i=0; i<points.length; i++){
		for (var j=0; j<points[i].length; j++){
			var point = points[i][j];
			if (i<square_map_side/2 && j<square_map_side/2)
				point[2]=2;	//scelta arbitraria per inizializzare la valle, dopodiche' parte la zona montuosa
			else{
				if (i===0) {
					point[2] = getRandomZ(points[i][j-1][2], 0.8);
				} 
				else{
					point[2] = getRandomZ(points[i-1][j][2], 0.8);
				}
			}
		}
	}
	return points;
}

function getMountains(points){
	for (var k=0; k<points.length; k++) {
		for (var l=0; l<points[k].length; l++) {
			//mountains = STRUCT([mountains, simplicial1(points, i,j), simplicial2(points, i,j)]);
			simplicial1(points, k, l);
			simplicial2(points, k, l);
		}
	}
}


function simplicial1(points, i, j){
	if (i<(points.length-1) && j<(points.length-1))
		DRAW(COLOR(ground)(SIMPLICIAL_COMPLEX([points[i][j], points[i+1][j], points[i+1][j+1]])([[0,1,2]])));
}

function simplicial2(points, i, j){
	if (i<(points.length-1) && j<(points.length-1))
		DRAW(COLOR(ground)(SIMPLICIAL_COMPLEX([points[i][j], points[i][j+1], points[i+1][j+1]])([[0,1,2]])));
}


function getLowestZ(points){
	var min = 2;
	for (var i=0; i<points.length; i++){
		for (var j=0; j<points[i].length; j++){
			if (points[i][j][2] < min)
				min = points[i][j][2];
		}
	}
	return min;
}

//LAGO
function createLake(points){
	var lake = CUBOID([square_map_side, square_map_side, lake_depth]);
	lake = T([2])([getLowestZ(points)])(lake);
	lake = COLOR([0,0,1])(lake)
	return lake;
}


//=================================================================================================================
//ESECUZIONI
//essendo tutto generato randomicamente, se il lago non è perfetto è consigliato rieseguire lo script.

var points = getPoints3D();

getMountains(points);
var lake = createLake(points);
var model = STRUCT([lake]);
DRAW(model);