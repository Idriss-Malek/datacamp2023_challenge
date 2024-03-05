import numpy as np


def prepare(df):
    df = df.replace("Not Answer", np.nan)
    df = df.replace("Not_Answer", np.nan)
    df["Question_InstallmentMonthly"] = df["Question_InstallmentMonthly"].replace(
        "Cash", np.nan
    )
