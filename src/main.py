# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Enrique_Escalante-Notario
# Instituto de Fisica, UNAM
# email: <enriquescalante@gmail.com>
# Distributed under terms of the GPLv3 license.
# main.py
# --------------------------------------------------------

from makedataset import *

# Setup these files for each geometry

# Name files with models
name_models_from_orbifolder = "z8_MSSM.txt"
# Name of geometry, see List_of_geometries.txt
name_geometry = "Z8-I_1_1.txt"
# Name output file
name_dataset = "Z8_MSSM.csv"
# Sectors considered, untwisted sector = 0
list_sectors = [1,3]  

#--------------------------------------------------------

# Optional parameters

## Num of model where the script break
## start = 0  

## Check file from the orbifolder for the separator
## separator = " "
## separator = ",  "

# ------------------------------------------------------

# Execution

#gauge_group(name_models_from_orbifolder)
make_dataset(name_models_from_orbifolder,list_sectors,name_geometry,name_dataset)
	