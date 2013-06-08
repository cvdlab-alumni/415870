wood = [166.0/255, 128.0/255, 100.0/255];
green = [0, 100.0/255, 0];
ground = [92.0/255, 51.0/255 ,23.0/255];
dark_grey = [0.2, 0.2, 0.2]

var square_map_side = 30;	//min 40

var subsquare_side = 1;

var lake_depth = square_map_side*4/100 + 0.1;

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


function circl (sel) {
  return function (r) {
    return function (altezza) {
      return function (p) {
        return [ r * COS(sel(p)), r * SIN(sel(p)), altezza ];
      };
    };
  };
};


//modello di conifera
function getModelTree(r, h, slices){
	var domainPI = DOMAIN([[0,2*PI],[0,1]])([80,1]);
	var trunk = CYL_SURFACE([r/6, h/4])(slices);
	var base_cone = circl(S0)(r)(h/4);
	var cone = BEZIER(S1)([base_cone, [0,0,h]]);
	cone = MAP(cone)(domainPI);
	trunk = COLOR(wood)(trunk);
	cone = COLOR(green)(cone);
	var tree = STRUCT([trunk, cone]);
	return tree;
}

// FORESTA DI CONIFERE
//gli alberi stanno tutti su una prima porzione di mappa, in modo da separare la foresta dagli insediamenti
function getForest(points, treeNumber) {
	var forest;
	for (var c = 0; c<treeNumber; c++) {
		//controllo che non ci siano alberi con tronco sull'acqua
		do{
			var i = getRandomIndex(points);
			var j = getRandomIndex(points);
			var p = points[i][j];
			//console.log("z: "+ p[2])
		} while(p[2]<=lake_depth+getLowestZ(points));
		var tree = getModelTree(0.25,1,[16,2]);
		tree = T([0,1,2])([p[0],p[1],p[2]])(tree);
		DRAW(tree)
		console.log(typeof forest);
		if (typeof forest === 'undefined')
   			forest = STRUCT([tree]);
		else
			forest = STRUCT([forest, tree]);
	}
	return forest;
}

function getRandomIndex(points) {
	var num = Math.floor((Math.random()*points.length/2) + points.length/2);
	return num;
}

//=================================================================================================================
//ESECUZIONI
//essendo tutto generato randomicamente, se il lago non è perfetto è consigliato rieseguire lo script.
var points = getPoints3D();

getMountains(points);
var lake = createLake(points);
var forest = getForest(points, 150);	//per avere l'effetto foresta deve essere un numero alto, ma è molto oneroso
var model = STRUCT([lake, forest]);
DRAW(model);