import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# load the data
os.chdir(r'C:\Users\Asus\Documents\01_code\03_projects\glassdoor_scraper')
jd_df = pd.read_excel(r'data\job_data_final.xlsx', index_col=0)
# jd_df = jd_df(drop_duplicates())

# drop these words from the discription to isolate the important keywords
bad_chars = ['!', ',', '.', '?',
            'in ', 'an ', 'und ', 'mit ', 'von ',
            'der ', 'im ', 'oder ', 'wir ', 'die ',
            'für ', 'zu ', 'auf ', 'den ', 'uns ', 'das ',
            'als ', 'eine ', 'sowie ', 'einem ', 'ein ', 'ist ',
            'bei ', 'über ', 'zur '
            ]


desc_all = []
for desc in jd_df['Job Description'][:100]:
    for char in bad_chars:
        desc = desc.replace(char, '')
    desc = desc.lower().split()
    desc = list(set(desc)) # unique words
    desc_all += desc

desc_all_df = pd.DataFrame({'words':desc_all})

word_count_df = desc_all_df['words'].value_counts()
word_count_df.head(50)
#word_count_df.to_excel('description_word_count.xlsx')


def count_keywords(num_jobs, debug = False):
    syn_dict = {'analytical': ['analytical', 'analytisch'],
                'english': ['english', 'Englisch'],
                'travel': ['reisebereitschaft'],
                'sklearn': ['scikit', 'Scikit'],
                'R ':['R,', 'R.'],
                'statistics': ['Statistik', 'statistisch'],
                'numeric': ['Numerik', 'numerisch'],
                'PhD': ['PHD', 'phd', 'Doktor'],
                'Pytorch': ['pytorch'],
                'classification': ['Klassifikation'],
                'german': ['deutsch'],
                'excel': ['Excel'],
                'RL': ['Reinforcement learning'],
                'ML': ['machine learning', 'Machine learning']}

    keyword_dict = {'ML': 0,
                    'Python': 0,
                    'R ': 0,
                    'Java': 0,
                    'SQL': 0,
                    'analytical': 0,
                    'travel': 0,
                    'english': 0,
                    'MATLAB': 0,
                    'Pytorch': 0,
                    'sklearn': 0,
                    'statistics': 0,
                    'numeric': 0,
                    'PhD': 0,
                    'TensorFlow': 0,
                    'classification': 0,
                    'RL': 0,
                    ' supervised': 0,
                    'unsupervised': 0,
                    'german': 0,
                    'Keras': 0,
                    'excel': 0}


    for desc in jd_df['Job Description'][:num_jobs]:
        for key in keyword_dict.keys():
            if key in desc:
                keyword_dict[key] += 1
                if debug: print(key)
            elif key in syn_dict.keys():
                inc = 0
                for syn in syn_dict[key]:
                    if syn in desc:
                        inc = 1
                        if debug: print(syn)
                keyword_dict[key] += inc
        if debug: print('--------------------------')

    return  keyword_dict

n_jobs = 1000
keyword_dict = count_keywords(n_jobs)
keyword_dict = {k: v / n_jobs for k,v in sorted(keyword_dict.items(), key = lambda item: item[1])}


sns.barplot(list(keyword_dict.values())[::-1][:-1],list(keyword_dict.keys())[::-1][:-1])
plt.title('Most requested skills in 1000 data science job descriptions on glassdoor.de')
plt.xlabel('percentage')
#sns.barplot(list(keyword_dict.keys()), keyword_dict.values()
#, align = 'center'
#)
#plt.yticks(range(len(keyword_dict)), list(keyword_dict.keys()))
#plt.title('Frequency of certain keywords in {} job descriptions'.format(n_jobs))
plt.show()
