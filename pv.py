import pandas as pd
df=pd.read_csv("employee.csv")
print("\nEmployees sorted by salary:")
df_sorted = df.sort_values("salary")
df_sorted1 = df.sort_values("salary",ascending=False)
# print(df_sorted)
print(df_sorted1)