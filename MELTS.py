import PySulfSat as ss
import pyMELTScalc as M
import os

df = ss.import_data(
    r"C:\Users\paulh\Desktop\FitIndex\Data\Glass_composition.xlsx", suffix="_Liq"
)

sample = df.iloc[0]

Pressure_range = [1000, 2000, 3000, 4000]

H2O_range = [0, 1, 2, 3, 4]

Oxygen_fugacity_range = []

# List of names for results files
Results = [
    "Results_1000.xlsx",
    "Results_2000.xlsx",
    "Results_3000.xlsx",
    "Results_4000.xlsx",
]


def MELTS_crystallization():
    for P, Res in zip(Pressure_range, Results):
        MELTS_FC = M.multi_path(
            Model="MELTSv1.0.2",
            Fe3Fet_Liq=0.1,
            H2O_Liq=0.1,
            comp=sample.to_dict(),
            Frac_solid=True,
            Frac_fluid=True,
            find_liquidus=True,
            T_end_C=750,
            dt_C=5,
            P_bar=P,
        )

        MELTS = MELTS_FC["All"]

        MELTS.to_excel(Res)

        # Specify the folder path where the files are located
        folder_path = ""

        # List of files to delete
        files_to_delete = [
            "Bulk_comp_tbl.txt",
            "Liquid_comp_tbl.txt",
            "Phase_main_tbl.txt",
            "Solid_comp_tbl.txt",
            "System_main_tbl.txt",
            "liquid-model-batch.inp",
        ]

        # Iterate through the list of files and delete them
        for file_name in files_to_delete:
            # Construct the full path to the file
            file_path = os.path.join(folder_path, file_name)

            # Check if the file exists before attempting to delete it
            if os.path.exists(file_path):
                # Delete the file
                os.remove(file_path)
                print(f"Deleted {file_name}")
            else:
                print(f"{file_name} not found")
