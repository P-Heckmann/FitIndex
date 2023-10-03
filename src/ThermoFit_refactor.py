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


def get_fitindex_sum(
    model: pd.DataFrame,
    measurements: pd.DataFrame,
    oxide_names: list[str],
    suffix: str,
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
    model: pd.DataFrame,
    measurements: pd.DataFrame,
    oxide_names: list[str],
    suffix: str,
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
