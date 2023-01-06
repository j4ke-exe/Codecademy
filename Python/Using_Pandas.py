import pandas

# df = DataFrame
commute_df = pandas.read_csv("commute_data.csv")

commute_df.columns = ['county_name', 'total_commuters', 'super_commuters', 'state_code', 'county_code']

print(commute_df.head())

# Output

# county_name  total_commuters  ...  state_code  county_code
# 0   Schoharie County, New York            13168  ...          36           95
# 1      Fulton County, New York            23576  ...          36           35
# 2  Rensselaer County, New York            76709  ...          36           83
# 3    Franklin County, New York            17811  ...          36           33
# 4      Queens County, New York          1071768  ...          36           81

# [5 rows x 5 columns]
