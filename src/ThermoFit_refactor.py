import pandas as pd
import numpy as np

plagio_meas = pd.read_excel(
    r"./Data/Measured_compositions/Plagioclase_composition.xlsx"
)
clino_meas = pd.read_excel(
    r"./Data/Measured_compositions/Clinopyroxene_composition.xlsx"
)
model_1000 = pd.read_excel(r"./Data/MELTS_models/Results_1000.xlsx")
model_2000 = pd.read_excel(r"./Data/MELTS_models/Results_2000.xlsx")
model_3000 = pd.read_excel(r"./Data/MELTS_models/Results_3000.xlsx")
model_4000 = pd.read_excel(r"./Data/MELTS_models/Results_4000.xlsx")


# plagioclase oxide concentrations of measurement
plag_oxide_names = ["SiO2", "Al2O3", "CaO", "Na2O"]
plag_model_suffix = "Plag"

# clinopyroxene oxide concentrations of measurement
cpx_oxide_names = ["SiO2", "TiO2", "Al2O3", "FeO", "MgO", "CaO", "Na2O"]
cpx_model_suffix = "Cpx"


# possible columns
# 	T_C	P_bar	h	s	v	dvdp	logfO2	SiO2_Liq	TiO2_Liq	Al2O3_Liq	Cr2O3_Liq	Fe2O3_Liq	FeO_Liq	FeOt_Liq	MnO_Liq	MgO_Liq	CaO_Liq	Na2O_Liq	K2O_Liq	P2O5_Liq	H2O_Liq	CO2_Liq	Fe3Fet_Liq	h_Liq	mass_Liq	v_Liq	rho_Liq	SiO2_Plag	TiO2_Plag	Al2O3_Plag	Cr2O3_Plag	Fe2O3_Plag	FeO_Plag	FeOt_Plag	MnO_Plag	MgO_Plag	CaO_Plag	Na2O_Plag	K2O_Plag	P2O5_Plag	H2O_Plag	CO2_Plag	Fe3Fet_Plag	h_Plag	mass_Plag	v_Plag	rho_Plag	SiO2_Cpx	TiO2_Cpx	Al2O3_Cpx	Cr2O3_Cpx	Fe2O3_Cpx	FeO_Cpx	FeOt_Cpx	MnO_Cpx	MgO_Cpx	CaO_Cpx	Na2O_Cpx	K2O_Cpx	P2O5_Cpx	H2O_Cpx	CO2_Cpx	Fe3Fet_Cpx	h_Cpx	mass_Cpx	v_Cpx	rho_Cpx	SiO2_Cpx2	TiO2_Cpx2	Al2O3_Cpx2	Cr2O3_Cpx2	Fe2O3_Cpx2	FeO_Cpx2	FeOt_Cpx2	MnO_Cpx2	MgO_Cpx2	CaO_Cpx2	Na2O_Cpx2	K2O_Cpx2	P2O5_Cpx2	H2O_Cpx2	CO2_Cpx2	Fe3Fet_Cpx2	h_Cpx2	mass_Cpx2	v_Cpx2	rho_Cpx2	SiO2_Sp	TiO2_Sp	Al2O3_Sp	Cr2O3_Sp	Fe2O3_Sp	FeO_Sp	FeOt_Sp	MnO_Sp	MgO_Sp	CaO_Sp	Na2O_Sp	K2O_Sp	P2O5_Sp	H2O_Sp	CO2_Sp	Fe3Fet_Sp	h_Sp	mass_Sp	v_Sp	rho_Sp	SiO2_Ol	TiO2_Ol	Al2O3_Ol	Cr2O3_Ol	Fe2O3_Ol	FeO_Ol	FeOt_Ol	MnO_Ol	MgO_Ol	CaO_Ol	Na2O_Ol	K2O_Ol	P2O5_Ol	H2O_Ol	CO2_Ol	Fe3Fet_Ol	h_Ol	mass_Ol	v_Ol	rho_Ol
def get_fitindex_sum(
    model: pd.DataFrame, measurements: pd.DataFrame, oxide_names: list[str], suffix: str
) -> list[float]:
    summed_fit_indices = []
    for _, row in model.iterrows():
        oxide_fit_indices = []
        for oxide_name in oxide_names:
            column_name = f"{oxide_name}_{suffix}"
            measurement = measurements[oxide_name].iloc[0]
            # how is NaN handled in this computation ??????
            fit_index = abs(row[column_name] - measurement) / measurement
            oxide_fit_indices.append(fit_index)
        summed_fit_indices.append(sum(oxide_fit_indices))

    return summed_fit_indices


def get_fitindex_sum_vectorized(
    model: pd.DataFrame, measurements: pd.DataFrame, oxide_names: list[str], suffix: str
) -> pd.DataFrame:
    oxide_fit_indices = []
    for oxide_name in oxide_names:
        # this for loop can also be veectorized if it becomes too slow
        column_name = f"{oxide_name}_{suffix}"
        measurement = measurements[oxide_name].iloc[0]
        fit_indices = np.abs(model[column_name] - measurement) / measurement
        oxide_fit_indices.append(fit_indices)

    df = pd.concat(oxide_fit_indices, axis=1)
    df.columns = [col + "_fit" for col in df.columns]
    return df


get_fitindex_sum_vectorized(
    model_1000, plagio_meas, plag_oxide_names, plag_model_suffix
)

# plag_fitindex = get_fitindex_sum(
#     model_1000, plagio_meas, plag_oxide_names, plag_model_suffix
# )
# print("plag_fitindex", plag_fitindex)

# cpx_fitindex = get_fitindex_sum(
#     model_1000, clino_meas, cpx_oxide_names, cpx_model_suffix
# )
# print("cpx_fitindex", cpx_fitindex)

# combined_fitindex = plag_fitindex + cpx_fitindex

# print(combined_fitindex)
