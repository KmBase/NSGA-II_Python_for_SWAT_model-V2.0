#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import os
import sys
# Use this if you do not want to install library
sys.path.append(os.path.join(os.getcwd(), "SWATnsga2Libs"))
from nsga2lib import nsga2, SWATutilities, nsga2utilities
time_start = time.time()

#---- Input ----(space on directory may cause problems during execution)
SWATtxtinoutDirectory = os.path.join(os.getcwd(), "TxtInOut")
#---------------

NSGAII = nsga2.nsga2(SWATtxtinoutDirectory)
NSGAII.CreateInitialPopulation()

#Loop through generations
TotalNumGenerations = NSGAII.ngener
i = 0
while i < TotalNumGenerations:
    # Thorough selection, crossover and mutation child population created from old population
    NSGAII.CreateChildPopulation()

    # Turn binary calibration parameters into normal numbers.
    nsga2utilities.decode(NSGAII.new_pop_ptr, NSGAII.vlen, NSGAII.lim_b)
    #new_pop_ptr=child population. vlen=the no.of bits assigned to the each calibration parameters. lim_b=range of calibration parameters.

    SWATutilities.CalculateObjectiveFunctions(
        NSGAII.new_pop_ptr, NSGAII.Outlet_Obsdata, NSGAII.FuncOpt, NSGAII.FuncOptAvr, NSGAII.parname, i+1, NSGAII.SWATdir)

    # Old and New populations goes throuth Elitism, crowding distances, nondominated sorting
    NSGAII.CreateParentPopulation(i+1)
    #and create the old population for next generation. Report is printed during this function process.
    i += 1

print "The NSGA-II execution finished. Look at the results in NSGA2.OUT folder."
time_end = time.time()
print 'totally cost', time_end-time_start, 's',