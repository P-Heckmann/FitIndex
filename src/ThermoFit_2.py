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


MELTS_models = [model_1000, model_2000, model_3000, model_4000]


# plagioclase oxide concentrations of measurement
oxide_plag_meas = ["SiO2", "Al2O3", "CaO", "Na2O"]

# plagioclase oxide concentrations of model
oxide_plag_model = ["SiO2_Plag", "Al2O3_Plag", "CaO_Plag", "Na2O_Plag"]


def Fitindex_plagioclase(models, plagio_meas):
    F_plagioclase_data = []

    for mod in models:  # iterating for different models (pressures)
        num_rows = mod.shape[0]
        numbers_list = list(range(num_rows))
        for i in numbers_list:  # iterating for different rows (temperature)
            temperature = mod["T_C"][i]  # Get the temperature
            for oxide_model, oxide_meas in zip(
                oxide_plag_model, oxide_plag_meas
            ):
                F_plagioclase = (
                    abs((mod[oxide_model][i] - plagio_meas[oxide_meas][0]))
                    / plagio_meas[oxide_meas][0]
                )
            F_plagioclase_data.append([F_plagioclase, temperature])

            df = pd.DataFrame(
                F_plagioclase_data, columns=["fitindex", "temperature"]
            )

    return df


df_fit_plag = Fitindex_plagioclase(MELTS_models, plagio_meas)

df_fit_plag.to_excel(r"Data\FitIndex\FitIndex_plagioclase_pressure_range.xlsx")


def Fitindex_plagioclase(models, plagio_meas):
    F_plagioclase_data = {}  # Use a dictionary to store data for each model

    for mod_idx, mod in enumerate(
        models
    ):  # Enumerate to keep track of model index
        F_plagioclase_data[mod_idx] = []  # Create a new list for each model

        num_rows = mod.shape[0]
        numbers_list = list(range(num_rows))

        for i in numbers_list:  # iterating for different rows (temperature)
            temperature = mod["T_C"][i]  # Get the temperature
            F_plagioclase = []
            for oxide_model, oxide_meas in zip(
                oxide_plag_model, oxide_plag_meas
            ):
                F = (
                    abs((mod[oxide_model][i] - plagio_meas[oxide_meas][0]))
                    / plagio_meas[oxide_meas][0]
                )
                F_plagioclase.append(F)

            F_plagioclase_data[mod_idx].append([F_plagioclase, temperature])

    dfs = []  # List to store individual DataFrames for each model
    for mod_idx, data in F_plagioclase_data.items():
        df = pd.DataFrame(data, columns=["fitindex", "temperature"])
        dfs.append(df)

    return dfs  # Return a list of DataFrames, one for each model


df_fit_plag = Fitindex_plagioclase(MELTS_models, plagio_meas)
