from pyplasm import *
from lar import *
from utilities import *

#===================================== !!!!!!!!!!!!!!!!!!!! =================================================================================================
# Per questo esercizio ho posizionato il volante all'interno del modello 3d dello scheletro dell'automobile, in modo da essere più chiara la sua collocazione
#============================================================================================================================================================

def circl (sel) :
	def circl0 (r) :
		def circl1 (altezza) :
			def circl2 (p) :
	        		return [ r * COS(sel(p)), r * SIN(sel(p)), altezza ]
			return circl2
		return circl1
	return circl0

def circl_dx (sel) :
	def circl0 (r) :
		def circl1 (altezza) :
			def circl2 (dx):
				def circl3 (p) :
					return [ r * COS(sel(p))+ dx, r * SIN(sel(p))+dx, altezza ]
				return circl3
			return circl2
		return circl1
	return circl0

def annulus_sector (alpha, r, R) :
	domain = DOMAIN([[0,2*PI],[r,R]])([36,36])
	def mapping (v) :
		a = v[0]
		r = v[1]
		return [r*COS(a), r*SIN(a)]
	model = MAP(mapping)(domain)
	return model

domain1D = INTERVALS(1)(20)
distanza_tra_frontal_behind = 20

#vano anteriore, profilo basso
vano_anteriore_piano_x_frontal_points_1 = [[0,0,0.9],[6.6,0,0.45]]
vano_anteriore_piano_x_frontal_1 = BEZIER(S1)(vano_anteriore_piano_x_frontal_points_1)
vano_anteriore_piano_x_behind_points_1 = trasla(vano_anteriore_piano_x_frontal_points_1, 0,distanza_tra_frontal_behind,0)
vano_anteriore_piano_x_behind_1 = BEZIER(S1)(vano_anteriore_piano_x_behind_points_1)

#vano anteriore, profilo medio
vano_anteriore_piano_x_frontal_points_2 = [[0,0,0.9],[6.6,0,0.9 + 0.45]]
vano_anteriore_piano_x_frontal_2 = BEZIER(S1)(vano_anteriore_piano_x_frontal_points_2)
vano_anteriore_piano_x_behind_points_2 = trasla(vano_anteriore_piano_x_frontal_points_2, 0,distanza_tra_frontal_behind,0)
vano_anteriore_piano_x_behind_2 = BEZIER(S1)(vano_anteriore_piano_x_behind_points_2)

#vano anteriore, pezzo sotto, chiusura
vano_anteriore_piano_x_frontal_vertical_points = [[6.6,0,0.45],[6.6,0,0.9 + 0.45]]
vano_anteriore_piano_x_frontal_vertical = BEZIER(S1)(vano_anteriore_piano_x_frontal_vertical_points)
vano_anteriore_piano_x_behind_vertical_points = trasla(vano_anteriore_piano_x_frontal_vertical_points,0,distanza_tra_frontal_behind,0)
vano_anteriore_piano_x_behind_vertical = BEZIER(S1)(vano_anteriore_piano_x_behind_vertical_points)

#vano anteriore, profilo faretto
vano_anteriore_piano_x_frontal_spoiler_points_1 = [[2.3,0,1.00],[1.9,0,3.00]]
vano_anteriore_piano_x_frontal_spoiler_1 = BEZIER(S1)(vano_anteriore_piano_x_frontal_spoiler_points_1)
vano_anteriore_piano_x_behind_spoiler_points_1 = trasla(vano_anteriore_piano_x_frontal_spoiler_points_1 ,0,distanza_tra_frontal_behind,0)
vano_anteriore_piano_x_behind_spoiler_1 = BEZIER(S1)(vano_anteriore_piano_x_behind_spoiler_points_1)

vano_anteriore_piano_x_frontal_spoiler_points_2 = [[1.9,0,3.00],[0,0,3.00]]
vano_anteriore_piano_x_frontal_spoiler_2 = BEZIER(S1)(vano_anteriore_piano_x_frontal_spoiler_points_2)
vano_anteriore_piano_x_behind_spoiler_points_2 = trasla(vano_anteriore_piano_x_frontal_spoiler_points_2 ,0,distanza_tra_frontal_behind,0)
vano_anteriore_piano_x_behind_spoiler_2 = BEZIER(S1)(vano_anteriore_piano_x_behind_spoiler_points_2)

vano_anteriore_piano_y_frontal_points_1 = [[0,0,0.9],[0,distanza_tra_frontal_behind,0.9]]
vano_anteriore_piano_y_frontal_1 = BEZIER(S1)(vano_anteriore_piano_y_frontal_points_1)
vano_anteriore_piano_y_frontal_points_12 = [[1,0 +3,2],[3,distanza_tra_frontal_behind/2,2],[1,distanza_tra_frontal_behind -3 ,2]]
vano_anteriore_piano_y_frontal_12 = BEZIER(S1)(vano_anteriore_piano_y_frontal_points_12)
vano_anteriore_piano_y_frontal_points_2 = [[0,0,3],[0,distanza_tra_frontal_behind,3]]
vano_anteriore_piano_y_frontal_2 = BEZIER(S1)(vano_anteriore_piano_y_frontal_points_2)

#vano anteriore,cofano, 
vano_anteriore_piano_x_frontal_cofano_points_1 = [[0,0,3],[1.5,0,5.4],[13,0,8],[12.5,0,7.5]]
vano_anteriore_piano_x_frontal_cofano_1 = BEZIER(S1)(vano_anteriore_piano_x_frontal_cofano_points_1)
vano_anteriore_piano_x_behind_cofano_points_1 = trasla(vano_anteriore_piano_x_frontal_cofano_points_1 ,0,distanza_tra_frontal_behind,0)
vano_anteriore_piano_x_behind_cofano_1 = BEZIER(S1)(vano_anteriore_piano_x_behind_cofano_points_1)

#vano anteriore, cofano profilo y
vano_anteriore_piano_y_frontal_cofano_points_1 = [[12.5,0,7.5],[10,7,7.5],[10,16,7.5],[12.5,distanza_tra_frontal_behind,7.5]]
vano_anteriore_piano_y_frontal_cofano_1 = BEZIER(S1)(vano_anteriore_piano_y_frontal_cofano_points_1)

#portiera
portiera_frontal_piano_x_points_1 = [[12.5,0,7.5],[12,0,5],[13.8,0,7.25],[15,0 ,2.25]]
portiera_frontal_piano_x_1 = BEZIER(S1)(portiera_frontal_piano_x_points_1)
portiera_behind_piano_x_points_1 = trasla(portiera_frontal_piano_x_points_1, 0,distanza_tra_frontal_behind,0)
portiera_behind_piano_x_1 = BEZIER(S1)(portiera_behind_piano_x_points_1)

#profili della parte centrale
partecentrale_frontal_piano_x_points1 = [[14.5,0 ,2.25],[38,0,3.5]]
partecentrale_frontal_piano_x_1 = BEZIER(S1)(partecentrale_frontal_piano_x_points1)
partecentrale_behind_piano_x_points1 = trasla(partecentrale_frontal_piano_x_points1 ,0,distanza_tra_frontal_behind,0)
partecentrale_behind_piano_x_1 = BEZIER(S1)(partecentrale_behind_piano_x_points1)

partecentrale_frontal_piano_x_points2 = [[14.5,0 ,0.4],[37,0,0.4]]
partecentrale_frontal_piano_x_2 = BEZIER(S1)(partecentrale_frontal_piano_x_points2)
partecentrale_behind_piano_x_points2 = trasla(partecentrale_frontal_piano_x_points2, 0,distanza_tra_frontal_behind,0)
partecentrale_behind_piano_x_2 = BEZIER(S1)(partecentrale_behind_piano_x_points2)

partecentrale_frontal_piano_x_raccordo_circ_points = [[14.5,0 ,0.4], [14.55,0,1.35]]
partecentrale_frontal_piano_x_raccordo_circ = BEZIER(S1)(partecentrale_frontal_piano_x_raccordo_circ_points)
partecentrale_behind_piano_x_raccordo_circ_points = trasla(partecentrale_frontal_piano_x_raccordo_circ_points, 0,distanza_tra_frontal_behind,0)
partecentrale_behind_piano_x_raccordo_circ = BEZIER(S1)(partecentrale_behind_piano_x_raccordo_circ_points)

parte_centrale_raccordo_circ_post_frontal_piano_x_points = [[37,0,0.4],[37,0,1]]
parte_centrale_raccordo_circ_post_frontal_piano_x = BEZIER(S1)(parte_centrale_raccordo_circ_post_frontal_piano_x_points)
parte_centrale_raccordo_circ_post_behind_piano_x_points = trasla(parte_centrale_raccordo_circ_post_frontal_piano_x_points, 0,distanza_tra_frontal_behind,0)
parte_centrale_raccordo_circ_post_behind_piano_x = BEZIER(S1)(parte_centrale_raccordo_circ_post_behind_piano_x_points)

#SOTTO finestrino
parte_centrale_sotto_finestrino_frontal_piano_x_points_1 = [[12.5,0,7.5],[13,0 , 6],[27,0,8]]
parte_centrale_sotto_finestrino_frontal_piano_x_1 = BEZIER(S1)(parte_centrale_sotto_finestrino_frontal_piano_x_points_1)
parte_centrale_sotto_finestrino_behind_piano_x_points_1 = trasla(parte_centrale_sotto_finestrino_frontal_piano_x_points_1, 0,distanza_tra_frontal_behind,0)
parte_centrale_sotto_finestrino_behind_piano_x_1 = BEZIER(S1)(parte_centrale_sotto_finestrino_behind_piano_x_points_1)

parte_centrale_portiera_frontal_piano_x_points = [[27,0,8],[28,0,7],[26,0, 2.9]]
parte_centrale_portiera_frontal_piano_x = BEZIER(S1)(parte_centrale_portiera_frontal_piano_x_points)
parte_centrale_portiera_behind_piano_x_points = trasla(parte_centrale_portiera_frontal_piano_x_points, 0,distanza_tra_frontal_behind,0)
parte_centrale_portiera_behind_piano_x = BEZIER(S1)(parte_centrale_portiera_behind_piano_x_points)

#continuo
parte_centrale_sotto_finestrino_frontal_piano_x_points_2 = [[27,0,8], [38,0,9], [43,0, 8], [43, 0, 9.5]]
parte_centrale_sotto_finestrino_frontal_piano_x_2 = BEZIER(S1)(parte_centrale_sotto_finestrino_frontal_piano_x_points_2)
parte_centrale_sotto_finestrino_behind_piano_x_points_2 = trasla(parte_centrale_sotto_finestrino_frontal_piano_x_points_2, 0,distanza_tra_frontal_behind,0)
parte_centrale_sotto_finestrino_behind_piano_x_2 = BEZIER(S1)(parte_centrale_sotto_finestrino_behind_piano_x_points_2)

#sopra il finestrino
parte_centrale_sopra_finestrino_frontal_piano_x_points_1 =  [[12.5,0,7.5], [ 20,0,14] , [40,0,10]  ,[43, 0, 9.5]]
parte_centrale_sopra_finestrino_frontal_piano_x = BEZIER(S1)(parte_centrale_sopra_finestrino_frontal_piano_x_points_1)
parte_centrale_sopra_finestrino_behind_piano_x_points_1 =  trasla(parte_centrale_sopra_finestrino_frontal_piano_x_points_1, 0,distanza_tra_frontal_behind,0)
parte_centrale_sopra_finestrino_behind_piano_x = BEZIER(S1)(parte_centrale_sopra_finestrino_behind_piano_x_points_1)

#divisore tra finestrini anteriori e posteriori
parte_centrale_tra_finestrini_frontal_piano_x_points_1 = [[26.8,0,8],[26.3,0, 11.25]]
parte_centrale_tra_finestrini_frontal_piano_x_1 = BEZIER(S1)(parte_centrale_tra_finestrini_frontal_piano_x_points_1)
parte_centrale_tra_finestrini_behind_piano_x_points_1 = trasla(parte_centrale_tra_finestrini_frontal_piano_x_points_1, 0,distanza_tra_frontal_behind,0)
parte_centrale_tra_finestrini_behind_piano_x_1 = BEZIER(S1)(parte_centrale_tra_finestrini_behind_piano_x_points_1)

parte_centrale_tra_finestrini_frontal_piano_x_points_2 = [[25.8,0,7.8],[25.3,0, 11.25]]
parte_centrale_tra_finestrini_frontal_piano_x_2 = BEZIER(S1)(parte_centrale_tra_finestrini_frontal_piano_x_points_2)
parte_centrale_tra_finestrini_behind_piano_x_points_2 = trasla(parte_centrale_tra_finestrini_frontal_piano_x_points_2, 0,distanza_tra_frontal_behind,0)
parte_centrale_tra_finestrini_behind_piano_x_2 = BEZIER(S1)(parte_centrale_tra_finestrini_behind_piano_x_points_2)
#
#coda della macchina
coda_sopra_finestrino_frontal_piano_x_points_1 = [[43, 0, 9.5], [49,0,8.5]]
coda_sopra_finestrino_frontal_piano_x_1 = BEZIER(S1)(coda_sopra_finestrino_frontal_piano_x_points_1)
coda_sopra_finestrino_behind_piano_x_points_1 = trasla(coda_sopra_finestrino_frontal_piano_x_points_1,0,distanza_tra_frontal_behind,0)
coda_sopra_finestrino_behind_piano_x_1 = BEZIER(S1)(coda_sopra_finestrino_behind_piano_x_points_1)

#coda posteriore
coda_posteriore_frontal_piano_x_points_1 = [[49,0,8.5], [51,0,4]]
coda_posteriore_frontal_piano_x_1 = BEZIER(S1)(coda_posteriore_frontal_piano_x_points_1)
coda_posteriore_behind_piano_x_points_1 = trasla(coda_posteriore_frontal_piano_x_points_1, 0,distanza_tra_frontal_behind,0)
coda_posteriore_behind_piano_x_1 = BEZIER(S1)(coda_posteriore_behind_piano_x_points_1)

coda_posteriore_inferiore_frontal_piano_x_points_1 = [[52,0,4],[53,0,2],[48,0,1.5],[45,0,1]]
coda_posteriore_inferiore_frontal_piano_x_1 = BEZIER(S1)(coda_posteriore_inferiore_frontal_piano_x_points_1)
coda_posteriore_inferiore_behind_piano_x_points_1 = trasla (coda_posteriore_inferiore_frontal_piano_x_points_1, 0,distanza_tra_frontal_behind,0)
coda_posteriore_inferiore_behind_piano_x_1 = BEZIER(S1)(coda_posteriore_inferiore_behind_piano_x_points_1)

coda_posteriore_raccordo_frontal_piano_x_points = [[51,0,4],[52,0,4]]
coda_posteriore_raccordo_frontal_piano_x = BEZIER(S1)(coda_posteriore_raccordo_frontal_piano_x_points)
coda_posteriore_raccordo_behind_piano_x_points = trasla(coda_posteriore_raccordo_frontal_piano_x_points, 0,distanza_tra_frontal_behind,0)
coda_posteriore_raccordo_behind_piano_x = BEZIER(S1)(coda_posteriore_raccordo_behind_piano_x_points)


coda_posteriore_piano_y_points_1 = [[51,0,4],[51,distanza_tra_frontal_behind,4]]
coda_posteriore_piano_y_1 = BEZIER(S1)(coda_posteriore_piano_y_points_1)
coda_posteriore_piano_y_points_2 = [[49,0,8.5],[49,distanza_tra_frontal_behind,8.5]]
coda_posteriore_piano_y_2 = BEZIER(S1)(coda_posteriore_piano_y_points_2)

coda_posteriore_piano_y_points_3 = [[45,0,1],[45,distanza_tra_frontal_behind,1]]
coda_posteriore_piano_y_3 = BEZIER(S1)(coda_posteriore_piano_y_points_3)

parabrezza_piano_y = T([1,3])([7,3])(MAP(vano_anteriore_piano_y_frontal_cofano_1)(domain1D))

motore_piano_y_points_1 = [[26.3,0 +3, 11.25],[26.3,distanza_tra_frontal_behind -3, 11.25]]
motore_piano_y_1 = BEZIER(S1)(motore_piano_y_points_1)
motore_piano_y_points_2 = [[43, 0 +3, 9.5], [43, distanza_tra_frontal_behind -3, 9.5]]
motore_piano_y_2 = BEZIER(S1)(motore_piano_y_points_2)

motore_piano_z_points_1 = [[26.3,0 +3, 11.25],[43, 0 +3, 9.5]]
motore_piano_z_1 = BEZIER(S1)(motore_piano_z_points_1)

motore_piano_z_points_2 = [[26.3,distanza_tra_frontal_behind -3, 11.25],[43, distanza_tra_frontal_behind -3, 9.5]]
motore_piano_z_2 = BEZIER(S1)(motore_piano_z_points_2)


#figure della ruota
profilo_ruota_anteriore_frontal_piano_x = MAP(circl(S1)(4)(0))(INTERVALS(PI)(24))
profilo_ruota_anteriore_frontal_piano_x = R([2,3])(PI/2)(profilo_ruota_anteriore_frontal_piano_x)
profilo_ruota_anteriore_frontal_piano_x = T([1,3])([10.6, 1.35])(profilo_ruota_anteriore_frontal_piano_x)
profilo_ruota_anteriore_behind_piano_x = T(2)(distanza_tra_frontal_behind)(profilo_ruota_anteriore_frontal_piano_x)

profilo_ruota_posteriore_frontal_piano_x = MAP(circl(S1)(4)(0))(INTERVALS(PI)(24))
profilo_ruota_posteriore_frontal_piano_x = R([2,3])(PI/2)(profilo_ruota_posteriore_frontal_piano_x)
profilo_ruota_posteriore_frontal_piano_x = T([1,3])([41, 1])(profilo_ruota_posteriore_frontal_piano_x)
profilo_ruota_posteriore_behind_piano_x = T(2)(distanza_tra_frontal_behind)(profilo_ruota_posteriore_frontal_piano_x)


# LA STRUCT DI TUTTE LE CURVE VISIBILI DAL PIANO X
piano_x = STRUCT([MAP(vano_anteriore_piano_x_frontal_1)(domain1D), MAP(vano_anteriore_piano_x_behind_1)(domain1D), 
	MAP(vano_anteriore_piano_x_frontal_2)(domain1D), MAP(vano_anteriore_piano_x_behind_2)(domain1D),
	MAP(vano_anteriore_piano_x_frontal_vertical)(domain1D), MAP(vano_anteriore_piano_x_behind_vertical)(domain1D),
	MAP(vano_anteriore_piano_x_frontal_spoiler_1)(domain1D), MAP(vano_anteriore_piano_x_behind_spoiler_1)(domain1D),
	MAP(vano_anteriore_piano_x_frontal_spoiler_2)(domain1D), MAP(vano_anteriore_piano_x_behind_spoiler_2)(domain1D),
	MAP(vano_anteriore_piano_x_frontal_cofano_1)(domain1D), MAP(vano_anteriore_piano_x_behind_cofano_1)(domain1D),
	MAP(portiera_frontal_piano_x_1)(domain1D), MAP(portiera_behind_piano_x_1)(domain1D),
	MAP(partecentrale_frontal_piano_x_1)(domain1D),MAP(partecentrale_behind_piano_x_1)(domain1D),
	MAP(partecentrale_frontal_piano_x_2)(domain1D),MAP(partecentrale_behind_piano_x_2)(domain1D),
	MAP(parte_centrale_sotto_finestrino_frontal_piano_x_1)(domain1D), MAP(parte_centrale_sotto_finestrino_behind_piano_x_1)(domain1D),
	MAP(parte_centrale_portiera_frontal_piano_x)(domain1D),MAP(parte_centrale_portiera_behind_piano_x)(domain1D),
	MAP(parte_centrale_sotto_finestrino_frontal_piano_x_2)(domain1D),MAP(parte_centrale_sotto_finestrino_behind_piano_x_2)(domain1D),
	MAP(parte_centrale_sopra_finestrino_frontal_piano_x)(domain1D),MAP(parte_centrale_sopra_finestrino_behind_piano_x)(domain1D),
	MAP(parte_centrale_tra_finestrini_frontal_piano_x_1)(domain1D),MAP(parte_centrale_tra_finestrini_behind_piano_x_1)(domain1D),
	MAP(parte_centrale_tra_finestrini_frontal_piano_x_2)(domain1D),MAP(parte_centrale_tra_finestrini_behind_piano_x_2)(domain1D),
	MAP(coda_sopra_finestrino_frontal_piano_x_1)(domain1D),MAP(coda_sopra_finestrino_behind_piano_x_1)(domain1D),
	MAP(coda_posteriore_frontal_piano_x_1)(domain1D),MAP(coda_posteriore_behind_piano_x_1)(domain1D),
	MAP(coda_posteriore_inferiore_frontal_piano_x_1)(domain1D),MAP(coda_posteriore_inferiore_behind_piano_x_1)(domain1D),
	MAP(coda_posteriore_raccordo_frontal_piano_x)(domain1D),MAP(coda_posteriore_raccordo_behind_piano_x)(domain1D),
	profilo_ruota_anteriore_frontal_piano_x,profilo_ruota_anteriore_behind_piano_x,
	profilo_ruota_posteriore_frontal_piano_x,profilo_ruota_posteriore_behind_piano_x,
	MAP(partecentrale_frontal_piano_x_raccordo_circ)(domain1D), MAP(partecentrale_behind_piano_x_raccordo_circ)(domain1D),
	MAP(parte_centrale_raccordo_circ_post_frontal_piano_x)(domain1D),MAP(parte_centrale_raccordo_circ_post_behind_piano_x)(domain1D)])

# LA STRUCT DI TUTTE LE CURVE VISIBILI DAL PIANO Y
piano_y = STRUCT([MAP(vano_anteriore_piano_y_frontal_1)(domain1D), MAP(vano_anteriore_piano_y_frontal_2)(domain1D),MAP(vano_anteriore_piano_y_frontal_12)(domain1D),
	MAP(vano_anteriore_piano_y_frontal_cofano_1)(domain1D),
	MAP(coda_posteriore_piano_y_1)(domain1D),MAP(coda_posteriore_piano_y_2)(domain1D),MAP(coda_posteriore_piano_y_3)(domain1D),
	MAP(motore_piano_y_1)(domain1D),MAP(motore_piano_y_2)(domain1D),
	parabrezza_piano_y,])

# LA STRUCT DI TUTTE LE CURVE RIMANENTI VISIBILI DAL PIANO Z
piano_z = STRUCT ([MAP(motore_piano_z_1)(domain1D),MAP(motore_piano_z_2)(domain1D)])

modello3D_x_y_Z = STRUCT([ COLOR([1,0,0])(piano_x) , COLOR([0,1,0])(piano_y), COLOR([0,0,1])(piano_z)])

#costruzione della ruota
def ruota (r,R, dy):
	anello = RING([r , R])([36,1])
	pneumatico = MYEXTRUDE(dy)(anello)
	return COLOR([0,0,0])(pneumatico)

def raggi (n ,dy, dz, r2):
	delta = 0.1
	phase = 2*PI/n
	rot = R([1,2])(phase)
	vertices = [[0+r2 -delta,0],[r2 +dz/2.0,1],[r2+dz +delta,0]]
	single_radius = PROD([BEZIERSTRIPE([vertices,dy,22]),QUOTE([dy])])
	single_radius = T(3)(-dy/2.0)(single_radius)
	models = NN(n)([single_radius, rot])
	return  (STRUCT(models))

def cerchione (r1, r2, R1, R2, n_raggi, dy ,dz):
	anello_esterno = RING([R1 , R2])([36,36])
	anello_esterno = MYEXTRUDE(dy)(anello_esterno)
	anello_interno = RING([r1, r2])([36,36])
	anello_interno = MYEXTRUDE(dy)(anello_interno)
	radiuses = raggi(n_raggi, dy, R1-r2, r2)
	radiuses = T(3)(dy/2)(radiuses)
	cerchione = STRUCT([anello_esterno,anello_interno, radiuses])
	cerchioni = STRUCT([cerchione, T(3)(dz-dy)(cerchione)])
	cerchioni = COLOR([205.0/256,173.0/256,0])(cerchioni)
	return cerchioni

#===========================================
# RUOTE
#===========================================
larghezza_wheel = 3;

wheel = STRUCT([ruota(2.3, 3.5,larghezza_wheel), cerchione(0.25,0.5, 2.0,2.3, 9, 0.2, larghezza_wheel)]);
wheel = R([2,3])(PI/2)(wheel)
wheel = T([2,3])([larghezza_wheel,1])(wheel)

ruota_ant_sx = T(1)(10.6)(wheel);
ruota_ant_dx = T(2)(distanza_tra_frontal_behind - larghezza_wheel)(ruota_ant_sx)
ruota_post_sx = T(1)(41 -10.6)(ruota_ant_sx);
ruota_post_dx = T(2)(distanza_tra_frontal_behind - larghezza_wheel)(ruota_post_sx)

ruote = STRUCT([ruota_ant_sx,ruota_post_sx, ruota_ant_dx, ruota_post_dx])

modello3D_x_y_Z = STRUCT([modello3D_x_y_Z, ruote])

#===================================
# VOLANTE
#===================================

def torus (R, r) :
  def torus0 (v) :
     a = v[0]
     b = v[1] 
     u = (r * COS(a)+2*R) * (COS(b))
     v = (r * COS(a)+2*R) * (SIN(b))
     w = (r * SIN(a))
     return [u,v,w]
  return torus0

def esterno_volante():
  interval = INTERVALS(2*PI)(30)
  interval2 = INTERVALS(2*PI)(30)
  domain = DOMAIN2D([interval,interval2])
  mapping = torus(3,1)
  esterno_volante = MAP(mapping)(domain)
  return esterno_volante

def volante ():
	volante = COLOR([0,0,0])(esterno_volante())
	punti_curva_superiore_volante_1 = [[-6,0,0], [-1,0,1], [-4,2,2], [0,2,2]]
	curva_superiore_volante_mapping_1 = BEZIER(S1)(punti_curva_superiore_volante_1)
	curva_superiore_volante_1 = OFFSET([0.5,0.5,1])(MAP(curva_superiore_volante_mapping_1)(domain1D))
	punti_curva_superiore_volante_2 = [[6,0,0], [1,0,1], [4,2,2], [0,2,2]]
	curva_superiore_volante_mapping_2 = BEZIER(S1)(punti_curva_superiore_volante_2)
	curva_superiore_volante_2 = OFFSET([0.5,0.5,1])(MAP(curva_superiore_volante_mapping_2)(domain1D))
	curva_superiore_volante = STRUCT([curva_superiore_volante_2,curva_superiore_volante_1])
	curva_superiore_volante = T([1,3])([-0.5,-0.5])(curva_superiore_volante)

	punti_curva_superiore_volante_12 = [[-6,0,0], [-1,0,1], [-4,-2,2], [0,-2,2]]
	curva_superiore_volante_mapping_12 = BEZIER(S1)(punti_curva_superiore_volante_12)
	curva_superiore_volante_12 = OFFSET([0.5,0.5,1])(MAP(curva_superiore_volante_mapping_12)(domain1D))
	punti_curva_superiore_volante_22 = [[6,0,0], [1,0,1], [4,-2,2], [0,-2,2]]
	curva_superiore_volante_mapping_22 = BEZIER(S1)(punti_curva_superiore_volante_22)
	curva_superiore_volante_22 = OFFSET([0.5,0.5,1])(MAP(curva_superiore_volante_mapping_22)(domain1D))
	curva_superiore_volante2 = STRUCT([curva_superiore_volante_22,curva_superiore_volante_12])
	curva_superiore_volante2 = T([1,3])([-0.5,-0.5])(curva_superiore_volante2)

	punti_curva_inferiore_volante_1 = [[-6,0,0], [-1,0,1], [-4,-2,2], [0,-2,1], [0,-6,0]]
	curva_inferiore_volante_mapping_1 = BEZIER(S1)(punti_curva_inferiore_volante_1)
	curva_inferiore_volante_1 = OFFSET([0.5,0.5,1])(MAP(curva_inferiore_volante_mapping_1)(domain1D))
	curva_inferiore_volante_1 = T([1,3])([-0.5,-0.5])(curva_inferiore_volante_1)
	punti_curva_inferiore_volante_2 = [[6,0,0], [1,0,1], [4,-2,2], [0,-2,1], [0,-6,0]]
	curva_inferiore_volante_mapping_2 = BEZIER(S1)(punti_curva_inferiore_volante_2)
	curva_inferiore_volante_2 = OFFSET([0.5,0.5,1])(MAP(curva_inferiore_volante_mapping_2)(domain1D))
	curva_inferiore_volante_2 = T([1,3])([-0.5,-0.5])(curva_inferiore_volante_2)
	curva_inferiore_volante = STRUCT([curva_inferiore_volante_1, curva_inferiore_volante_2])
	curva_inferiore_volante = T(1)(0.2)(curva_inferiore_volante)

	core = COLOR([221.0/256, 113.0/256, 0])(T([2,3])([0.6,-0.6])(MYEXTRUDE(2)(RING([0,2])([20,20]))))
	core_esterno = COLOR([0, 0, 0])(T([2,3])([0.6,-0.6])(MYEXTRUDE(2)(RING([2,2.6])([20,20]))))
	core= STRUCT([core, core_esterno])
	core = T(3)(1.4)(core)
	volante = (STRUCT([volante,curva_superiore_volante, core, curva_superiore_volante2,  curva_inferiore_volante]))
	return (volante)

steering = volante();
steering = R([1,3])(PI/2)(steering)
steering = R([2,3])(PI/2)(steering)
steering = S([1,2,3])([0.3,0.3,0.3])(steering)
steering = T([1,2,3])([15,5,6])(steering)

modello3D_x_y_Z = STRUCT([modello3D_x_y_Z, steering])

VIEW(modello3D_x_y_Z)

#========================================================
# i profili della lamborghini
#========================================================
curva_z_1 = MAP(BEZIER(S1)([[88.5,480,0],[-15,484,0],[-15, 800,0],[88.5, 805,0]]))(domain1D)
curva_z_2 = MAP(BEZIER(S1)([[88.5,805,0],[154,840,0],[268, 845,0],[310, 825,0]]))(domain1D)
curva_z_3 = MAP(BEZIER(S1)([[310,825,0],[390,815,0],[730, 870,0],[840, 850,0]]))(domain1D)
curva_z_4 = MAP(BEZIER(S1)([[840, 850,0],[935,830,0],[930, 800,0],[945, 655,0]]))(domain1D)
curva_z_5 = MAP(BEZIER(S1)([[945, 655,0],[930,485,0],[935, 460,0],[840, 440,0]]))(domain1D)
curva_z_6 = MAP(BEZIER(S1)([[840, 440,0],[560,430,0],[480, 460,0],[310, 460,0]]))(domain1D)
curva_z_7 = MAP(BEZIER(S1)([[310, 460,0],[160,445,0],[150,455,0],[88.5,480,0]]))(domain1D)
profilo_z = STRUCT([curva_z_1,curva_z_2,curva_z_3,curva_z_4,curva_z_5,curva_z_6,curva_z_7])

curva_y_1 = MAP(BEZIER(S1)([[1270,615,0],[1215,600,0],[1205, 630,0],[1250, 630,0]]))(domain1D)
curva_y_2 = MAP(BEZIER(S1)([[1250, 630,0],[1235,730,0],[1275, 750,0],[1320, 745,0]]))(domain1D)
curva_y_3 = MAP(BEZIER(S1)([[1320, 745,0],[1335,720,0],[1450, 720,0],[1450, 720,0]]))(domain1D)
curva_y_4 = MAP(BEZIER(S1)([[1450, 720,0],[1450, 720,0],[1600, 720,0],[1585, 745,0]]))(domain1D)
curva_y_5 = MAP(BEZIER(S1)([[1585, 745,0],[1670, 745,0],[1660, 680,0],[1655, 615,0]]))(domain1D)
curva_y_6 = MAP(BEZIER(S1)([[1655, 615,0],[1715, 600,0],[1660, 630,0],[1655, 630,0]]))(domain1D)
curva_y_7 = MAP(BEZIER(S1)([[1655, 630,0],[1530, 530,0],[1370, 530,0],[1270, 615,0]]))(domain1D)
profilo_y = STRUCT([curva_y_1,curva_y_2,curva_y_3,curva_y_4,curva_y_5,curva_y_6,curva_y_7])
profilo_y = T(1)(-1000)(profilo_y)
profilo_y = R([1,2])(-PI/2)(profilo_y)
profilo_y = R([1,3])(PI/2)(profilo_y)
profilo_y = T([1,2,3])([1000,1125,-525])(profilo_y)

curva_y_front_1 = MAP(BEZIER(S1)([[1275,225,0],[1280,216,0],[1625, 217,0],[1625, 225,0]]))(domain1D)
curva_y_front_2 = MAP(BEZIER(S1)([[1625, 225,0],[1680,245,0],[1660, 191,0],[1650, 100,0]]))(domain1D)
curva_y_front_3 = MAP(BEZIER(S1)([[1650, 100,0],[1715,90,0],[1682, 62,0],[1624, 70,0]]))(domain1D)
curva_y_front_4 = MAP(BEZIER(S1)([[1624, 70,0],[1575, 15,0],[1500, 22,0],[1450, 20,0]]))(domain1D)
curva_y_front_5 = MAP(BEZIER(S1)([[1450, 20,0],[1380, 25,0],[1355, 35,0],[1280, 70,0]]))(domain1D)
curva_y_front_6 = MAP(BEZIER(S1)([[1280, 70,0],[1250, 66,0],[1180, 78,0],[1250, 94,0]]))(domain1D)
curva_y_front_7 = MAP(BEZIER(S1)([[1250, 94,0],[1238, 75,0],[1225, 255,0],[1275,225,0]]))(domain1D)
profilo_front_y = STRUCT([curva_y_front_1,curva_y_front_2,curva_y_front_3,curva_y_front_4,curva_y_front_5,curva_y_front_6,curva_y_front_7])
profilo_front_y = T(1)(-1000)(profilo_front_y)
profilo_front_y = R([1,2])(-PI/2)(profilo_front_y)
profilo_front_y = R([1,3])(PI/2)(profilo_front_y)
profilo_front_y = T([1,2])([-100,1125])(profilo_front_y)


curva_x_1 = MAP(BEZIER(S1)([[13.5,168,0],[160,85,0],[430, 12,0],[500, 20,0]]))(domain1D)
curva_x_2 = MAP(BEZIER(S1)([[500,20,0],[612,25,0],[884, 65,0],[905, 73,0]]))(domain1D)
curva_x_3 = MAP(BEZIER(S1)([[905, 73,0],[924,70,0],[1015, 205,0],[850, 210,0]]))(domain1D)
curva_x_4 = MAP(BEZIER(S1)([[850, 210,0],[830,40,0],[650, 125,0],[690, 225,0]]))(domain1D)
curva_x_5 = MAP(BEZIER(S1)([[690, 225,0],[295,230,0]]))(domain1D)
curva_x_6 = MAP(BEZIER(S1)([[295,230,0],[330,102,0],[140,50,0],[150,230,0]]))(domain1D)
curva_x_7 = MAP(BEZIER(S1)([[150,230,0],[13.5,220,0]]))(domain1D)
curva_x_8 = MAP(BEZIER(S1)([[13.5,220,0],[13.5,168,0]]))(domain1D)
profilo_x = STRUCT([curva_x_1,curva_x_2,curva_x_3,curva_x_4,curva_x_5,curva_x_6,curva_x_7, curva_x_8])
profilo_x =T(2)(500)(profilo_x)
profilo_x = R([2,3])(PI/2)(profilo_x)
profilo_x =T([2,3])([400,-500])(profilo_x)
profilo_x_behind =T(2)(500)(profilo_x)

profili = STRUCT([profilo_x,profilo_y,profilo_z,profilo_x_behind, profilo_front_y])
profili = T([1,2])([-500,-500])(profili)
#VIEW(profili)