from lar import *



# =====================================================
# DOMAIN by me
# =====================================================
#def DOMAIN(args):
#	i1, i2 = args
#	def DOMAIN0(nn):
#		n1, n2 = nn
#		return PROD([INTERVALS(S2(i1))(n1), INTERVALS(S2(i2))(n2)])
#	return DOMAIN0


def DOMAIN(args):
	i1, i2 = args
	def DOMAIN0(nn):
		n1,n2 = nn
		interval1 = DIFFERENCE([INTERVALS(S2(i1))(n1), INTERVALS(S1(i1))(n1)]);
		interval2 = DIFFERENCE([INTERVALS(S2(i2))(n2), INTERVALS(S1(i2))(n2)]);
		return PROD([interval1, interval2])
	return DOMAIN0
#======================================================
# MYEXTRUDE
#======================================================
def MYEXTRUDE (h):
	def MYEXTRUDE0(model):
		return PROD([model,Q(h)])
	return MYEXTRUDE0

# ALTRE
#=============================================================================
def DOMAIN2D(domains1D):
	def aux(q):
		a = q[0]
		b = q[1]
		c = q[2]
		d = q[3]
		return [ [ a, b, d ], [ d, b, c ] ]
	dd = PROD([ domains1D[0], domains1D[1] ])
	complex = UKPOL(dd)
	points = complex[0]
	cells = CAT(AA(aux)(complex[1]))
	return MKPOL([ points, cells, None ])


#============== utilities ====================================================
def trasla (points, dx,dy,dz):
	nuoviPunti = []
	for item in points:
		nuoviPunti.append([item[0]+dx,item[1]+dy,item[2]+dz])
  	return nuoviPunti

def scala (points, dx,dy,dz):
	nuoviPunti = []
	for item in points:
		nuoviPunti.append([item[0]*dx,item[1]*dy,item[2]*dz])
  	return nuoviPunti

def Rx (alpha) : return mat(
	[[1,		0,		0],
	[0,	COS(alpha), 	-SIN(alpha)],
	[0,	SIN(alpha), 	COS(alpha)]])

def Ry (alpha) : return mat(
	[[COS(alpha),	0,	SIN(alpha)],
	[0,		1, 		0],
	[-SIN(alpha),	0, 	COS(alpha)]])

def Rz (alpha) : return mat(
	[[COS(alpha),	-SIN(alpha),	0],
	[SIN(alpha),	COS(alpha), 	0],
	[0,		0,		1]])

def ruota (points, assi, alpha):
	r_points = []
	a1 = S1(assi)
	a2 = S2(assi)
	if (a1==1 and a2==2):
		for point in points:
			r_riga = []
			point_mat = mat([point])
			riga = (Rz(alpha)*point_mat.T).A1
			r_riga.append(riga[0])
			r_riga.append(riga[1])
			r_riga.append(riga[2])
			r_points.append(r_riga)
			r_points
		return r_points
	elif (a1==1 and a2==3):
		for point in points:
			r_riga = []
			point_mat = mat([point])
			riga = (Ry(alpha)*point_mat.T).A1
			r_riga.append(riga[0])
			r_riga.append(riga[1])
			r_riga.append(riga[2])
			r_points.append(r_riga)
		return r_points
	elif (a1==2 and a2==3):
		for point in points:
			r_riga = []
			point_mat = mat([point])
			riga = (Rx(alpha)*point_mat.T).A1
			r_riga.append(riga[0])
			r_riga.append(riga[1])
			r_riga.append(riga[2])
			r_points.append(r_riga)
		return r_points
	else:
		return points


#=========================== grid
def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V) / AA(float)(args))
	return MKPOL([verts, AA(AA(lambda h:h+1))(cells),None])
#========================================================================
