// Write a constructor function Point2D 
//that create a 2D point given its x and y coordinates.

function Point2D (x, y){
	this.x = x;
	this.y = y;
}

//Write a contructor function Edge
//that create an edge given its two vertices (i.e. two points).

//2a
function Edge(v1, v2){
	this.v1 = v1;
	this.v2 = v2;
}

//Write a method length for Edge that compute the length of the edge.
//2b
Edge.prototype.length = function () {
		return Math.sqrt(Math.pow((this.v1.x-this.v2.x),2) + Math.pow((this.v1.y-this.v2.y),2));
	};

//Write a constructor function Trinagle that create a triangle given its three edges.
//3a
function Triangle(e1, e2, e3){
	this.e1 = e1;
	this.e2 = e2;
	this.e3 = e3;
}

//Write a method perimeter for Triangle that compute the perimeter of the triangle.
//3b
Triangle.prototype.perimeter = function () {
	return this.e1.length() + this.e2.length() +this.e3.length();
}

//Write a method area for Triangle that compute the area of the triangle.
//3c
Triangle.prototype.area = function () {
	l1 = this.e1.length();
	l2 = this.e2.length();
	l3 = this.e3.length();
	var p = (l1 + l2 + l3)/2;
	return Math.sqrt(p*(p-l1)*(p-l2)*(p-l3));
}