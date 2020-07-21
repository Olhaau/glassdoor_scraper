import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

os.chdir(r'C:\Users\Asus\Documents\01_code\03_projects\glassdoor_scraper')

jd_df = pd.read_excel(r'data\job_data_final.xlsx', index_col=0)

# cleaning the company name
jd_df['Company Name'] = jd_df['Company Name'].apply(lambda x: str(x).split('\n')[0])

jd_df.to_excel('data\job_data_cleaned.xlsx')

print(jd_df.head())

# some overview which locations and industries offer the most data scientist jobs
#plt.barh(jd_df['Location'].value_counts().head(20).index,
#jd_df['Location'].value_counts().head(20),
# align = 'center')
plt.figure(figsize = (7,4))
plt.tight_layout()
sns.barplot(
jd_df['Location'].value_counts().drop('Deutschland').apply(lambda x: x / 1000.0)[0:10],
jd_df['Location'].value_counts().drop('Deutschland')[0:10].index,
)
plt.ylabel('Percentage')
plt.xlabel('Location')
plt.yticks( fontsize = 8)
plt.xticks(fontsize = 8)
plt.show()

#plt.figure(figsize = (4,5))
plt.figure(figsize = (7,4))
plt.tight_layout()
sns.barplot(
jd_df['Industry'].value_counts().apply(lambda x: x / 1000.0)[1:11],
jd_df['Industry'].value_counts()[1:11].index,
)
plt.ylabel('Percentage')
plt.xlabel('Location')
plt.yticks( fontsize = 8)
plt.xticks(fontsize = 8)
plt.show()

print(jd_df.Location.value_counts().index)
#print(jd_df['Location'].value_counts().head(20))
#print(jd_df['Industry'].value_counts()[1:20])

# jobs in places I am interested in
relevant_df = jd_df[jd_df['Location'].isin(['Mainz', 'Frankfurt', 'Wiesbaden'])]
print('number of jobs in interesting locations: ',len(relevant_df))
relevant_df.to_excel(r'data\relevant_jobs.xlsx')
