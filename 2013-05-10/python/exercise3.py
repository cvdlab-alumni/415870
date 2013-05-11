from pyplasm import *
from lar import *
from utilities import *

#===================================== !!!!!!!!!!!!!!!!!!!! =================================================================================================
# Per questo esercizio ho posizionato le ruote all'interno del modello 3D dello scheletro dell'automobile, in modo da rendere evidente la loro collocazione
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


#==========================================
# COSTRUZIONE DELLE RUOTE
#==========================================

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
VIEW(modello3D_x_y_Z)