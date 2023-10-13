#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")


# In[4]:


match=pd.read_csv(r"C:\Users\jeevi\Downloads\Indian Premier League\matches.csv")
score=pd.read_csv(r"C:\Users\jeevi\Downloads\Indian Premier League\deliveries.csv")


# In[5]:


match.head()


# In[6]:


score.head()


# ## Basic Information about the dataset

# In[8]:


print(match.info())


# In[9]:


score.info()


# In[11]:


match.isnull().sum()


# In[12]:


score.isnull().sum()


# In[13]:


match.describe()


# In[14]:


score.describe()


# In[17]:


#Matches we have got in the dataset
match.shape


# In[18]:


# seasons we have got in the dataset
match['season'].unique()


# ### Team won by Maximum Runs

# In[20]:


match.iloc[match['win_by_runs'].idxmax()]


# In[22]:


match.iloc[match['win_by_runs'].idxmax()]['winner']


# ### Team won by minimum runs

# In[23]:


match.iloc[match[match['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# ### Team won by minimum wickets

# In[24]:


match.iloc[match[match['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]['winner']


# ### Season which had most number of matches

# In[32]:


sns.countplot(x='season',data=match)


# #### we can see the year 2013 has the highest matches

# In[35]:


data=match.winner.value_counts()
sns.barplot(x=data,y=data.index)


# #### we can see that Mumbai Indians won the higher matches
# 

# In[48]:


top_players = match.player_of_match.value_counts()[:10]
top_players.plot.bar()
sns.barplot(x = top_players.index, y = top_players, palette="Greens");
plt.ylabel("Count")
plt.title("Top player of the match Winners")


# CH Gayle is the most Successful player in all match winners

# ### Champions each season

# In[50]:


df = match.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']].reset_index(drop=True)
df


# ### Number of matches in each venue

# In[55]:


sns.countplot(x='venue', data=match)
plt.xticks(rotation='vertical')
plt.show()


# #### There are quite a few venues present in the data with "Eden Gardens" being the one with most number of matches.

# ### Number of matches played by each team

# In[56]:


df = pd.melt(match, id_vars=['id','season'], value_vars=['team1', 'team2'])
sns.countplot(x='value', data=df)
plt.xticks(rotation='vertical')
plt.show()


# ### Toss decision

# In[68]:


temp_series = match.toss_decision.value_counts()
labels = (np.array(temp_series.index))
sizes = (np.array((temp_series / temp_series.sum())*100))
plt.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=100)
plt.title("Toss decision percentage")


# #### Almost 61% of the toss decisions are made to field first. Now let us see how this decision varied over time.

# In[61]:


sns.countplot(x='season', hue='toss_decision', data=match)
plt.xticks(rotation='vertical')
plt.show()


# #### It seems during the initial years, teams wanted to bat first. Look at the 2011 season, most of the toss decisions are to field first.

# In[67]:


wins = (match.win_by_wickets>0).sum()
loss = (match.win_by_wickets==0).sum()
labels = ["Wins", "Loss"]
total = float(wins + loss)
sizes = [(wins/total)*100, (loss/total)*100]
plt.pie(sizes, labels=labels,autopct='%1.1f%%',  startangle=100)
plt.title("Win percentage batting second")
plt.show()


# #### So percentage of times teams batting second has won is 53.7. Now let us split this by year and see the distribution.

# ### Batsman analysis

# In[71]:


df = score.groupby('batsman')['batsman_runs'].agg('sum').reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
df = df.iloc[:10,:]

labels = np.array(df['batsman'])
ind = np.arange(len(labels))
width = 0.9
fig, ax = plt.subplots(figsize=(15,8))
rects = ax.bar(ind, np.array(df['batsman_runs']), width=width, color='blue')
ax.set_xticks(ind+((width)/2.))
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel("Count")
ax.set_title("Top run scorers in IPL")
ax.set_xlabel('Batsmane Name')
plt.show()


# In[75]:


pip install pivottablejs


# In[76]:


from pivottablejs import pivot_ui


# In[78]:


pivot_ui(score)


# In[80]:


# Now let us see most common dismissal types in IPL.
sns.countplot(x='dismissal_kind', data=score)
plt.xticks(rotation='vertical')
plt.show()


# In[86]:


teams_per_season = match.groupby('season')['winner'].value_counts()
year = 2008
win_per_season_df = pd.DataFrame(columns=['year', 'team', 'wins'])
for items in teams_per_season.iteritems():    
    if items[0][0]==year:
        win_series = pd.DataFrame({
            'year': [items[0][0]],
            'team': [items[0][1]],
            'wins': [items[1]]
        })
        win_per_season_df = win_per_season_df.append(win_series)
        year += 1   
        
win_per_season_df


# In[ ]:




