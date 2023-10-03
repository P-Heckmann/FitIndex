import pandas as pd

plagio_meas = pd.read_excel(
    r"Data\Measured_compositions\Plagioclase_composition.xlsx"
)
clino_meas = pd.read_excel(
    r"Data\Measured_compositions\Clinopyroxene_composition.xlsx"
)
model_1000 = pd.read_excel(r"Data\MELTS_models\Results_1000.xlsx")
model_2000 = pd.read_excel(r"Data\MELTS_models\Results_2000.xlsx")
model_3000 = pd.read_excel(r"Data\MELTS_models\Results_3000.xlsx")
model_4000 = pd.read_excel(r"Data\MELTS_models\Results_4000.xlsx")


# plagioclase oxide concentrations of measurement
oxide_plag_meas = ["SiO2", "Al2O3", "CaO", "Na2O"]

# plagioclase oxide concentrations of model
oxide_plag_model = ["SiO2_Plag", "Al2O3_Plag", "CaO_Plag", "Na2O_Plag"]

# clinopyroxene oxide concentrations of measurement
oxide_cpx_meas = ["SiO2", "TiO2", "Al2O3", "FeO", "MgO", "CaO", "Na2O"]

# clinopyroxene oxide concentrations of model
oxide_cpx_model = [
    "SiO2_Cpx",
    "TiO2_Cpx",
    "Al2O3_Cpx",
    "FeOt_Cpx",
    "MgO_Cpx",
    "CaO_Cpx",
    "Na2O_Cpx",
]


def Fitindex_plagioclase(model, plagio_meas):
    num_rows = model.shape[0]
    numbers_list = list(range(num_rows))

    F_plagioclase_data = []
    for i in numbers_list:
        temperature = model_1000["T_C"][i]  # Get the temperature
        for oxide_model, oxide_meas in zip(oxide_plag_model, oxide_plag_meas):
            F_plagioclase = (
                abs((model_1000[oxide_model][i] - plagio_meas[oxide_meas][0]))
                / plagio_meas[oxide_meas][0]
            )
        F_plagioclase_data.append([F_plagioclase, temperature])

    df = pd.DataFrame(F_plagioclase_data, columns=["fitindex", "temperature"])

    return df


df_fit_plag = Fitindex_plagioclase(model_1000, plagio_meas)

df_fit_plag.to_excel(r"Data\FitIndex\FitIndex_plagioclase.xlsx")


def Fitindex_clinopyroxene(model, clino_meas):
    num_rows = model.shape[0]
    numbers_list = list(range(num_rows))

    F_clinopyroxene_data = []
    for i in numbers_list:
        temperature = model_1000["T_C"][i]  # Get the temperature
        for oxide_model, oxide_meas in zip(oxide_cpx_model, oxide_cpx_meas):
            F_clinopyroxene = (
                abs((model_1000[oxide_model][i] - clino_meas[oxide_meas][0]))
                / clino_meas[oxide_meas][0]
            )
        F_clinopyroxene_data.append([F_clinopyroxene, temperature])

    df = pd.DataFrame(
        F_clinopyroxene_data, columns=["fitindex", "temperature"]
    )

    return df


df_fit_cpx = Fitindex_clinopyroxene(model_1000, clino_meas)

df_fit_cpx.to_excel(r"Data\FitIndex\FitIndex_clinopyroxene.xlsx")


def Fitindex_combined_1(model, clino_meas, plagio_meas):
    num_rows = model.shape[0]
    numbers_list = list(range(num_rows))

    F_combined_data = []

    for i in numbers_list:
        temperature = model_1000["T_C"][i]  # Get the temperature
        for oxi_cpx_mod, oxi_cpx_me, oxi_plag_mod, oxi_plag_me in zip(
            oxide_cpx_model, oxide_cpx_meas, oxide_plag_model, oxide_plag_meas
        ):
            F_clinopyroxene = abs(
                (model_1000[oxi_cpx_mod][i] - clino_meas[oxi_cpx_me][0])
                + (model_1000[oxi_plag_mod][i] - plagio_meas[oxi_plag_me][0])
            ) / (clino_meas[oxi_cpx_me][0] + plagio_meas[oxi_plag_me][0])
        F_combined_data.append([F_clinopyroxene, temperature])

    df = pd.DataFrame(F_combined_data, columns=["fitindex", "temperature"])

    return df


df_fit_combined_test = Fitindex_combined_1(model_1000, clino_meas, plagio_meas)
df_fit_combined_test

df_fit_combined_test.to_excel(r"Data\FitIndex\FitIndex_combined_test.xlsx")


def Fitindex_combined_2(model, clino_meas, plagio_meas):
    num_rows = model.shape[0]
    numbers_list = list(range(num_rows))

    F_combined_data = []

    for i in numbers_list:
        temperature = model_1000["T_C"][i]  # Get the temperature
        for oxi_cpx_mod, oxi_cpx_me, oxi_plag_mod, oxi_plag_me in zip(
            oxide_cpx_model, oxide_cpx_meas, oxide_plag_model, oxide_plag_meas
        ):
            F_clinopyroxene = (
                abs((model_1000[oxi_cpx_mod][i] - clino_meas[oxi_cpx_me][0]))
                / clino_meas[oxi_cpx_me][0]
            )
            F_plagioclase = (
                abs(
                    (model_1000[oxi_plag_mod][i] - plagio_meas[oxi_plag_me][0])
                )
                / plagio_meas[oxi_plag_me][0]
            )

            F_combined = F_clinopyroxene + F_plagioclase
        F_combined_data.append([F_combined, temperature])

    df = pd.DataFrame(F_combined_data, columns=["fitindex", "temperature"])

    return df


df_fit_combined = Fitindex_combined_2(model_1000, clino_meas, plagio_meas)
df_fit_combined

df_fit_combined.to_excel(r"Data\FitIndex\FitIndex_combined_2_5.xlsx")
