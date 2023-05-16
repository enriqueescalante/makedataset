# -*- coding: utf-8 -*-

# --------------------------------------------------------
# Enrique_Escalante-Notario
# Instituto de Fisica, UNAM
# email: <enriquescalante@gmail.com>
# Distributed under terms of the GPLv3 license.
# MakeDataSet.py
# --------------------------------------------------------


import itertools
import numpy as np
import shlex, subprocess
from os import remove
import os
import re


name_models_writted = "purged_models.txt"


# ------------------------------------------


# Return one file with the parameters rewritten
def write_parameters(name_models_from_orbifolder):
    Mod = open(name_models_from_orbifolder, "r")  # File from Orbifolder
    Para = open(name_models_writted, "w")         # File brigde

    # Important: check file from the orbifolder for the sep
    #separa = " "
    separa = ",  "

    conta = 1
    model = []
    
    
    for linea in Mod:
        if conta == 6:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 7:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 8:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 9:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 10:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 11:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 12:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 13:
            model.append("["+linea[:-1].replace(
                separa, ",").replace("   ","").replace(" ","")+"]")
        if conta == 14:
            conta = 0
            Para.write(str(model).replace("'","")+"\n")
            model = []
        conta += 1
    Para.close()
    Mod.close()

    
# ------------------------------------------



# Create the nomassive states
def roots():
    conjunto1 = [1, 1, 0, 0, 0, 0, 0, 0]
    conjunto2 = [-1, -1, 0, 0, 0, 0, 0, 0]
    conjunto3 = [-1, 1, 0, 0, 0, 0, 0, 0]
    conjunto4 = [-1/2., -1/2., -1/2., -1/2., -1/2., -1/2., -1/2., -1/2.]
    conjunto5 = [-1/2., -1/2., -1/2., -1/2., -1/2., -1/2., 1/2., 1/2.]
    conjunto6 = [-1/2., -1/2., -1/2., -1/2., 1/2., 1/2., 1/2., 1/2.]
    conjunto7 = [-1/2., -1/2., 1/2., 1/2., 1/2., 1/2., 1/2., 1/2.]
    conjunto8 = [1/2., 1/2., 1/2., 1/2., 1/2., 1/2., 1/2., 1/2.]
    states1 = list(set(itertools.permutations(conjunto1, 8)))
    states2 = list(set(itertools.permutations(conjunto2, 8)))
    states3 = list(set(itertools.permutations(conjunto3, 8)))
    states4 = list(set(itertools.permutations(conjunto4, 8)))
    states5 = list(set(itertools.permutations(conjunto5, 8)))
    states6 = list(set(itertools.permutations(conjunto6, 8)))
    states7 = list(set(itertools.permutations(conjunto7, 8)))
    states8 = list(set(itertools.permutations(conjunto8, 8)))
    total = states1 + states2 + states3 + states4 + states5 + states6 + \
        states7 + states8
    final = []
    for element in total:
        final.append(list(element))
    return final


#-------------------------------------------
#Write program for gg in the orbifolder 
def program(label_model):
    prog = open("program.txt", "w")
    prog.write("load orbifolds(model.txt)\n"+"cd "+label_model+"\n"+
        "gg\n"+"print to file(gauge_groups.txt) gauge group")
    prog.close()

# -----------------------------------------
# Execution the orbifolder

def executeorbifolder():
    with open(os.devnull, "w") as f:
        args = shlex.split("./orbifolder auto")
        subprocess.call(args, stdout=f)

# -----------------------------------------

# Write gauge groups of models
def gauge_group(name_models_from_orbifolder):
    models = open(name_models_from_orbifolder, "r")
    lines = models.readlines()
    while len(lines) != 0:
        mod = open("model.txt","w")
        ini = lines.index("begin model\n")
        fin = lines.index("end model\n")
        model = lines[ini:fin+1]
        mod.write(''.join(map(str,model)))      
        mod.close()
        label_model = model[1][6:-1]

        program(label_model)
        executeorbifolder()
        del lines[ini:fin+1]
    remove("model.txt")
    remove("program.txt")
# -----------------------------------------

# Write num of U1 in each model

def numU1(name_models_from_orbifolder):
    gauge_groups = open("gauge_groups.txt", "r")
    U1 = open("U1s.txt", "w")

    for line in gauge_groups:
        if line != "\n":
            final = line[-9:-1]
            if re.search(' U',final):
                if final[0] == " ":
                    U1.write(str(final[6:])+"\n") 
                if final[0] == "x":
                    U1.write(str(final[7:])+"\n")
                if final[0] == "d":
                    U1.write(str(final[7:])+"\n")
            else:
                U1.write(str(0)+"\n")
    U1.close()



# Load sectors
def load_sectors(list_sectors, name_geometry):

    SEC = open(name_geometry, "r")  # File with the fixed points
    sectors = []
    sector = []
    lines = SEC.readlines()
    points_fixed = lines[lines.index("begin constructing elements\n") + 1:
                         lines.index("end constructing elements\n")]

    for fixedpoint in points_fixed:
        if fixedpoint != "new sector\n":
            sector.append(
                list(map(int, fixedpoint[:-2].split(sep=" "))))
        else:
            sectors.append(sector)
            sector = []
    del(sectors[0])
    final = []
    for ind in list_sectors:
        final.append(sectors[ind])
    return final
# ------------------------------------------


# Load centralizer
def load_centralizer(name_geometry):

    CEN = open(name_geometry, "r")  # File with the centralizers
    lines = CEN.readlines()
    centralizer_all = []
    central = lines[lines.index("begin centralizer elements\n") + 1:
                    lines.index("end centralizer elements\n")]

    while len(central) != 0:
        if central[0][:14] == "// Const elem:":
            centralizer = []
            centralizer.append(central[0][15:])

            centralizer.extend(central[central.index("begin data\n")+1:
                                       central.index("end data\n")])
            del central[:
                        central.index("end data\n")+2]
            centralizer_all.append(centralizer)

    final = []
    for elements in centralizer_all:
        aux = []
        for element in elements:
            aux.append(
                list(map(int, element[:-2].split(sep=" "))))
        final.append(aux)
    return final
# ---------------------------------------


# Return a list with N's for global verification
def __global__(model, nomassive):

    Ns = []

    V1 = np.array(list(map(eval, model[2:-3].split(
        "], [")[0].split(","))))
    V2 = np.array(list(map(eval, model[2:-3].split(
        "], [")[1].split(","))))
    W1 = np.array(list(map(eval, model[2:-3].split(
        "], [")[2].split(","))))
    W2 = np.array(list(map(eval, model[2:-3].split(
        "], [")[3].split(","))))
    W3 = np.array(list(map(eval, model[2:-3].split(
        "], [")[4].split(","))))
    W4 = np.array(list(map(eval, model[2:-3].split(
        "], [")[5].split(","))))
    W5 = np.array(list(map(eval, model[2:-3].split(
        "], [")[6].split(","))))
    W6 = np.array(list(map(eval, model[2:-3].split(
        "], [")[7].split(","))))

    V11 = np.array(V1[:8])
    V12 = np.array(V1[8:])
    V21 = np.array(V2[:8])
    V22 = np.array(V2[8:])
    W11 = np.array(W1[:8])
    W12 = np.array(W1[8:])
    W21 = np.array(W2[:8])
    W22 = np.array(W2[8:])
    W31 = np.array(W3[:8])
    W32 = np.array(W3[8:])
    W41 = np.array(W4[:8])
    W42 = np.array(W4[8:])
    W51 = np.array(W5[:8])
    W52 = np.array(W5[8:])
    W61 = np.array(W6[:8])
    W62 = np.array(W6[8:])
    N1 = 0
    N2 = 0

    for element in nomassive:
        state = np.array(element)
        VP11 = np.modf(state@V11)
        VP12 = np.modf(state@V12)
        VP21 = np.modf(state@V21)
        VP22 = np.modf(state@V22)
        WP11 = np.modf(state@W11)
        WP12 = np.modf(state@W12)
        WP21 = np.modf(state@W21)
        WP22 = np.modf(state@W22)
        WP31 = np.modf(state@W31)
        WP32 = np.modf(state@W32)
        WP41 = np.modf(state@W41)
        WP42 = np.modf(state@W42)
        WP51 = np.modf(state@W51)
        WP52 = np.modf(state@W52)
        WP61 = np.modf(state@W61)
        WP62 = np.modf(state@W62)

        if VP11[0] == 0.0:
            if VP21[0] == 0.0:
                if WP11[0] == 0.0:
                    if WP21[0] == 0.0:
                        if WP31[0] == 0.0:
                            if WP41[0] == 0.0:
                                if WP51[0] == 0.0:
                                    if WP61[0] == 0.0:
                                        N1 = N1 + 1
                                   

        if VP12[0] == 0.0:
            if VP22[0] == 0.0:
                if WP12[0] == 0.0:
                    if WP22[0] == 0.0:
                        if WP32[0] == 0.0:
                            if WP42[0] == 0.0:
                                if WP52[0] == 0.0:
                                    if WP62[0] == 0.0:
                                        N2 = N2 + 1
                                       
    Ns.append(N1)
    Ns.append(N2)

    return Ns
# -------------------------------------------------------------

# Return a list with N's for global verification
def __local__(model, sectors_considered, nomassive,name_geometry):

    Ns = []

    V1 = np.array(list(map(eval, model[2:-3].split(
        "], [")[0].split(","))))
    V2 = np.array(list(map(eval, model[2:-3].split(
        "], [")[1].split(","))))
    W1 = np.array(list(map(eval, model[2:-3].split(
        "], [")[2].split(","))))
    W2 = np.array(list(map(eval, model[2:-3].split(
        "], [")[3].split(","))))
    W3 = np.array(list(map(eval, model[2:-3].split(
        "], [")[4].split(","))))
    W4 = np.array(list(map(eval, model[2:-3].split(
        "], [")[5].split(","))))
    W5 = np.array(list(map(eval, model[2:-3].split(
        "], [")[6].split(","))))
    W6 = np.array(list(map(eval, model[2:-3].split(
        "], [")[7].split(","))))

    centralizer = load_centralizer(name_geometry)

    for sector in sectors_considered:
        for fijo in sector:
            N1 = 0
            N2 = 0
            for element in centralizer:  # locate centralizer
                if element[0] == fijo:
                    central = element
            for element in nomassive:
                state = np.array(element)
                aux1 = 0
                aux2 = 0
                for centra in central:
                    Vlocal = centra[0]*V1 + \
                        centra[1]*V2 + \
                        centra[2]*W1 + \
                        centra[3]*W2 + \
                        centra[4]*W3 + \
                        centra[5]*W4 + \
                        centra[6]*W5 + \
                        centra[7]*W6
                    Vlocal1 = np.array(Vlocal[:8])
                    Vlocal2 = np.array(Vlocal[8:])

                    VP1 = np.modf(state@Vlocal1)
                    VP2 = np.modf(state@Vlocal2)
                    if VP1[0] == 0.0:
                        aux1 = aux1 + 1
                    if (VP2[0] == 0.0):
                        aux2 = aux2 + 1
                if aux1 == len(central):
                    N1 = N1 + 1
                if aux2 == len(central):
                    N2 = N2 + 1
            Ns.append(N1)
            Ns.append(N2)

    return Ns
# -------------------------------------------------


# Return one file with the N's vectors written

def make_dataset(name_models_from_orbifolder, name_dataset, list_sectors, name_geometry, start, creategaugegroups=True):

    write_parameters(name_models_from_orbifolder)
    
    MOD = open(name_models_writted, "r")  # File bridge

    sectors_considered = load_sectors(list_sectors, name_geometry)
    nomassive = roots()

    if start == 0:
        DS = open(name_dataset, "w")  # File output with N's vectors
        if creategaugegroups == True:
            gauge_group(name_models_from_orbifolder)
        numU1(name_models_from_orbifolder)
        numU1s = open("U1s.txt", "r")
        U1s = numU1s.readlines()
        head = ["U1", "N1", "N2"]  # 
        sec = 1
        for sector in sectors_considered:
            fix = 1
            for fixed in sector:
                for i in range(1, 3):
                    head.append("N_"+str(sec)+"_"+str(fix)+"_"+str(i))
                fix = fix + 1
            fix = 1
            sec = sec + 1
        DS.write(",".join(head)+"\n")
    if start != 0:
        DS = open(name_dataset, "a")  # File output with N's vectors
        numU1s = open("U1s.txt", "r")
        U1s = numU1s.readlines()

    conta = 1
    for model in MOD:
        Ns = []
        if conta > start:
            print(conta, "models written", end="\r")
            Ns.extend([int(U1s[conta-1][:-1])])
            Ns.extend(__global__(model, nomassive))
            Ns.extend(__local__(model, sectors_considered, nomassive,name_geometry))
            DS.write(str(Ns)[1:-1]+"\n")
        else:
            pass
        conta = conta + 1


    numU1s.close()
    MOD.close()
    DS.close()
    
    remove("purged_models.txt")
    remove("U1s.txt")
    remove("gauge_groups.txt")
# ------------------------------------------



