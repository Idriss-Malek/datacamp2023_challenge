import pandas as pd
import numpy as np
from scipy.stats import boxcox

def prepare(df):
    df.drop(
        columns=[
            "VisitorID",
            "Question_InstallmentMonthly",
            "Question_Nationality",
            "Question_P_Income",
            "Question_TimeToMoveIn",
        ],
        inplace=True,
    )
    df = df.replace("Not Answer", np.nan)
    df = df.replace("Not_Answer", np.nan)
    df["Question_InstallmentMonthly"] = df["Question_InstallmentMonthly"].replace(
        "Cash", np.nan
    )
    col1_boxcox, _ = boxcox(df["Question_Budget"])
    col2_boxcox, _ = boxcox(df["Question_HHIncome"])
    df["Question_Budget"] = col1_boxcox
    df["Question_HHIncome"] = col2_boxcox
    df["Traget"] = df["Target"].astype(int)
    categorical_columns = [
        c for c in df.columns if df[c].dtype.kind not in ["i", "f"]
    ]
    df = pd.get_dummies(df, columns=categorical_columns)
    return df