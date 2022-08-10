# need file brand.xlsx and url.xlsx

import pandas as pd

df = pd.read_excel('brand.xlsx')
brands = list(df.Brandname) # brands is a list & Brandname is header
categories = ['skincare', 'makeup', 'perfume', 'mens-skincare', 'cologne', 'haircare', 'health-foods']
subCs = ['groupid=', 'groupId=']
subsubC = 'typeId='
sort = 'sort='

# read and export url excel
df = pd.read_excel('url.xlsx')

def myfunc(x):
	if any(brand in x for brand in brands) and any(category in x for category in categories) and not any(subC in x for subC in subCs) and not subsubC in x and not sort in x:
		return "brand under category"
	elif any(brand in x for brand in brands) and any(category in x for category in categories) and any(subC in x for subC in subCs) and not subsubC in x and not sort in x:
		return "brand under category w/ sub category"
	elif any(brand in x for brand in brands) and any(category in x for category in categories) and any(subC in x for subC in subCs) and subsubC in x and not sort in x:
		return "brand under category w/ sub sub category"
	elif sort in x:
		return "with sort"
	else:
		return "other type"

df['KindOfType'] = df['URL'].apply(myfunc) # URL is header
print(df)

df.to_excel('urltest.xlsx')
