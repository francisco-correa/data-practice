import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

diabetes = pd.read_csv("./Provisional_Diabetes_2020.csv", index_col=0)
print(diabetes.info())
print(diabetes.head())

sex = diabetes[(diabetes["Sex"] != "Male (M)") & (diabetes["COVID19"] == 1) ]
print(sex)
print(diabetes["Diabetes.uc"].max())

diabetes_age = diabetes.groupby("AgeGroup")["Diabetes.mc"].mean()
diabetes_age.plot(kind="line", color="blue", marker="*", linestyle=':')
plt.title("Group Age by mc")
plt.ylabel("mc_sum")
plt.legend()
plt.show()

diabetes_sex = diabetes.groupby("Sex")["Diabetes.uc"].mean()
diabetes_sex.plot(kind="bar", color="red")
plt.title("Group Sex by uc")
plt.ylabel("uc_sum")
plt.legend()
plt.show()

for x, y in diabetes.iterrows():
    print(x + " My sex is " + y["Sex"])

diabetes["total_mc_uc"] = diabetes["Diabetes.uc"] + diabetes["Diabetes.mc"]
diabetes["fraction_uc"] = (diabetes["Diabetes.uc"] / diabetes["total_mc_uc"])
print(diabetes.info())

diabetes_stats = diabetes.groupby("Sex")["total_mc_uc"].agg([min, max, np.mean, np.median])
print(diabetes_stats)