import pandas as pd

df = pd.read_csv('../data/survey_results_public.csv')
schema_df = pd.read_csv('../data/survey_results_schema.csv')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.haed()
df.tail()

df.shape
df.info()

