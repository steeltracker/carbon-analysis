## Scope 1 and 2 Values Per EAF Plant in the United States

# %%
### Loading Libraries
import pandas as pd
import numpy as np
import janitor

# %%
### Importing eGrid Data

## Importing grid region electricity values
egrid2021_data = pd.read_excel('../data/eGRID2021_data.xlsx', sheet_name = "SRL21").clean_names()

# %%
