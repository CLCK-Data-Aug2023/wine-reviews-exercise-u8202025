# add your code here

import pandas as pd
reviews = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)

counts = reviews['country'].value_counts()
avg = reviews.groupby('country')['points'].mean().round(1)
combine = pd.DataFrame({'count': counts, 'points': avg})
table = combine.sort_values(by='count', ascending=False)
table.index.name = 'country'
table.reset_index().to_csv("reviews-per-country.csv", index=False)
