import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PetThermoTools as M

import sys

sys.path.append(r"MELTS")

path = r"data\Example_data_Matt\Fernandina_glass.xlsx"
df = pd.read_excel(path)
df = df.fillna(0)

# split data based on the Group (Melt Inclusion or Matrix Glass)
MI = df.loc[df["Group"] == "MI", :].reset_index(drop=True)
MG = df.loc[df["Group"] == "MG", :].reset_index(drop=True)

MG.head()

MI = MI.sort_values("MgO", ascending=False, ignore_index=True)
MI.head()

starting_comp = MI.loc[0]
starting_comp


Isobaric_Xtal = M.isobaric_crystallisation(
    Model="MELTSv1.2.0",
    bulk=starting_comp,
    find_liquidus=True,
    P_bar=np.array([500]),
    T_end_C=1100,
    dt_C=2,
    fO2_buffer="FMQ",
    fO2_offset=-1.0,
    Frac_solid=True,
    Frac_fluid=True,
    label="pressure",
)
