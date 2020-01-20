import pandas as pd
from collections import Counter, defaultdict

__filename = 'data/survey_results_public.csv'

data = pd.read_csv(__filename)

print()
# print(type(data))
def get_langs(column='LanguageWorkedWith'):
    langs = defaultdict(int)
    for line in data[column]:
        langs['total'] += 1
        if type(line) is float:
            continue
        for lang in line.split(';'):
            langs[lang] += 1
    return langs


sorted_work_langs = sorted(get_langs().items(), key=lambda lang: lang[1], reverse=True)
sorted_desired_langs = sorted(get_langs('LanguageDesireNextYear').items(), key=lambda lang: lang[1], reverse=True)

print(sorted_work_langs)
print()
print(sorted_desired_langs)
    #if line is float:
    #    print(f'Anomialy: {line}')
    #    continue
    #[working_langs.update(langs) for langs in line.split(';') if line is not float]
    #for lang in langs:
    #  working_langs.update(lang)

# Get top 20
#print(df.head(20))

# Get All Columns
#print(data.columns)

# # Get Specific Column
# print(df.LastInt) # df['LastInt']

# # Get Slice of column
# print(df['LastInt'][0:20])

# # # Get Multiple Columns
# print(df[['Employment', 'MgrIdiot']]) # a list of column names inside the index operator

# # Print each row
# print(df.iloc[1:4])

# #Get Specific Row and Column pair
# print(df.iloc[2,1])

# Read Each Row
# for row in df.iterrows():
#     print(row)