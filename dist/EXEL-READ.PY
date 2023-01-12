import pandas as pd
# Read Excel file
df = pd.read_excel(r'WEEK.xlsx', engine='openpyxl')
print(df)