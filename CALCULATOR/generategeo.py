# -*- coding: utf-8 -*-
"""
Mesh generatin subroutines
Juan Vergara
Juan Gomez
"""

from os import sys
import numpy as np
import os
sys.path.append('../CALCULATOR/')
#
def create_model(var = '', seemesh = True):
#    var = raw_input('jobname:--?')
    os.system ('/Applications/Gmsh.app/Contents/MacOS/gmsh' + ' ' + var + '.geo -2 -order 1')
    file_name=open('input.txt', 'w')
    file_name.write('%5s \n' % (var))
    file_name.write('%2s \n' % ('1'))
    file_name.close()
    os.system ('../CALCULATOR/./mallador')
    nodes        = np.loadtxt('nodes.txt')
    elements     = np.loadtxt('eles.txt')
    nn =len(nodes[:,0])
    if seemesh:
        os.remove('nodes.txt')
        os.remove('eles.txt')
        os.remove(var +'.geo')
        os.remove(var +'.msh')
        os.remove('input.txt')
    
    return nodes, elements , nn
#
def mygeom(l, h, c):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for Boussinesq'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l/2, 0, 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {-l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(5) = {-l/2, 0, 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 5};'))
    file_name.write('%17s \n' % ('Line(5) = {5, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4, 5};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var    
#
def wedge(l, fi, c):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%23s \n' % ('// Input .geo for wedge'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%1s \n' % (' '))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %40.36f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%4s %12.8f %1s \n' % ('fi= ', fi, ';'))

    file_name.write('%16s \n' % ('fi= fi*Pi/180.0;'))
	
    file_name.write('%0s \n' % (''))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%59s \n' % ('Point(2) = {-l*Sin(fi), l*Cos(fi), 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(3) = {0, 2.0*l*Cos(fi), 0, c};		    // {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(4) = {l*Sin(fi), l*Cos(fi), 0, c};		// {x,y,z, size}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%57s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
	
    return var
#
def ring(r1, r2, c):
     var = raw_input('jobname:--?')
     file_name=open(var +'.geo', 'w')
     file_name.write('%22s \n' % ('// Input .geo for Ring'))
     file_name.write('%21s \n' % ('// author: Juan Gomez'))
     file_name.write('%1s \n' % (' '))
     file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))    	
     file_name.write('%0s \n' % (''))    	
     file_name.write('%4s %8.4f %1s \n' % ('r1= ', r1, ';'))    	
     file_name.write('%4s %8.4f %1s \n' % ('r2= ', r2, ';'))   
     file_name.write('%0s \n' % (''))
     file_name.write('%0s \n' % (''))
     file_name.write('%16s \n' % ('// Define points'))
     file_name.write('%0s \n' % (''))
     file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
     file_name.write('%25s \n' % ('Point(2) = {r1, 0, 0, c};'))
     file_name.write('%25s \n' % ('Point(3) = {r2, 0, 0, c};'))
     file_name.write('%0s \n' % (''))
     file_name.write('%26s \n' % ('// Define boundary circles'))
     file_name.write('%61s \n' % ('Circle(1) = {2, 1, 2};		// {Initial_point, center, end_point}'))
     file_name.write('%22s \n' % ('Circle(2) = {3, 1, 3};'))
     file_name.write('%0s \n' % (''))
     file_name.write('%14s \n' % ('// Joint Lines'))
     file_name.write('%32s \n' % ('Line Loop(1) = {1};	// {Id_line}'))
     file_name.write('%19s \n' % ('Line Loop(2) = {2};'))
     file_name.write('%0s \n' % (''))
     file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
     file_name.write('%26s \n' % ('Plane Surface(1) = {1, 2};'))
    	
     file_name.write('%0s \n' % (''))
    	
     file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
     file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    	
     file_name.write('%0s \n' % (''))
    	
     file_name.write('%19s \n' % ('// "Structure" mesh'))
     file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
    	
     file_name.write('%0s \n' % (''))
    
     file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
    	
     file_name.close()
    	
     return var
#
def boussinesq(l, h, c):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for Boussinesq'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l/2, 0, 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {-l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(5) = {-l/2, 0, 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 5};'))
    file_name.write('%17s \n' % ('Line(5) = {5, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4, 5};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var
#
def beam(l, h, c):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for Boussinesq'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0,-h/2, 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l,-h/2, 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l, h/2, 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {0, h/2, 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var
#
def quad(l, h, c):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for quad domain'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0 , 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l, 0 , 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l, h , 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {0, h , 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var