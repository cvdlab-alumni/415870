var points = [[0,0],[4,0],[4,4],[2,6],[0,4],[0,0]];

var pl = POLYLINE(points);

var cells = [[0,1,2,3,4,5]];

var parete = SIMPLICIAL_COMPLEX(points)(cells);

var home = EXTRUDE([5])(pl)

var home = COLOR([1,1,0])(home)

var points_porta = [[0,0],[1,0],[1,1],[2,1],[2,0],[4,0],[4,4],[2,6],[0,4],[0,0]];

var pl2 = POLYLINE(points_porta);

var ext = EXTRUDE([1])(pl2)

var cells_porta = [[0,1,2],[0,6,8],[3,5,6],[2,3,6],[3,4,5],[6,7,8]];

var parete_porta = T([2])([5])(SIMPLICIAL_COMPLEX(points_porta)(cells_porta))

var figura = STRUCT([home,parete, parete_porta]);

DRAW(figura);
