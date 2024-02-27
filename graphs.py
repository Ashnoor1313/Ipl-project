import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')
balls=pd.read_csv('IPL Ball-by-Ball 2008-2020.csv')
matches=pd.read_csv('IPL.csv')

def runs_dist():
 runs_by_match = balls.groupby(by='id').sum()
 runs_by_match = pd.DataFrame(runs_by_match['total_runs'])
 runs_by_match.reset_index(inplace=True)
 runs_by_match
 plt.figure(figsize=(15,9))
 sns.histplot(runs_by_match['total_runs'])
 plt.title('Runs distribution match wise')
 plt.show()

def runs():
 data = pd.merge(left=matches, right=balls, on='id', how='right')
 data['date'] = pd.to_datetime(data['date'])
 data['year'] = pd.DatetimeIndex(data['date']).year
 runs_by_years = data.groupby(by='year').sum()['total_runs']
 runs_by_years = pd.DataFrame(runs_by_years)
 runs_by_years.reset_index(inplace=True)

 plt.figure(figsize=(15,9))
 sns.lineplot(data=runs_by_years, x='year', y='total_runs')
 plt.title('Runs scored over the years')
 plt.show()

def toss():
 plt.figure(figsize=(15,9))
 sns.countplot(data=matches, x='toss_decision')
 plt.title('Preferred toss decision')
 plt.show()

def wickets():
 runs_and_wickets_by_over = balls.groupby(by='over').sum()
 runs_and_wickets_by_over = pd.DataFrame(runs_and_wickets_by_over[['total_runs', 'is_wicket']])
 runs_and_wickets_by_over.reset_index(inplace=True)

 plt.figure(figsize=(15,9))
 sns.scatterplot(data=runs_and_wickets_by_over, x='over', y='total_runs', size='is_wicket')
 plt.title('Totals runs and wickets by over')
 plt.show()

def runs_box():
 runs_overs = balls[['total_runs', 'over']]
 plt.figure(figsize=(15,9))
 sns.boxplot(data=balls, x='over', y='total_runs')
 plt.title('Runs distribution over wise')
 plt.show()

def cities():
 plt.figure(figsize=(12,12))
 c1 = sns.countplot(y= 'city',order=matches['city'].value_counts().iloc[:10].index,data = matches,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('Cities',fontsize=12)
 plt.xlabel('No: of matches',fontsize=12)
 plt.title('Top 10 Cities in which matches where held ',fontsize=15)
 plt.show()

def players():
 pom = matches['player_of_match'].value_counts().iloc[:10]
 plt.figure(figsize=(12,12))
 c1 = sns.countplot(y= 'player_of_match',order=pom.index,data = matches ,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('Player',fontsize=12)
 plt.xlabel('No: of matches',fontsize=12)
 plt.title('Top 10 Players who received POM',fontsize=15)
 plt.show()

def venues():
 venues = matches['venue'].value_counts().head(10)
 plt.figure(figsize=(12,12))
 c1 = sns.countplot(y='venue',order=venues.index,data = matches,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('Venues',fontsize=12)
 plt.xlabel('No: of matches',fontsize=12)
 plt.title('Top 10 Venues where matches were held',fontsize=15)
 plt.show()

def ranking_toss():
 toss_wins = matches['toss_winner'].value_counts()
 plt.figure(figsize=(12,12))
 c1 = sns.countplot(y='toss_winner',order=toss_wins.index,data = matches,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('Venues',fontsize=12)
 plt.xlabel('No: of tosses won',fontsize=12)
 plt.title('Teams ranked on basis of winning toss',fontsize=15)
 plt.show()

def ranking():
 wins = matches['winner'].value_counts()
 plt.figure(figsize=(12,12))
 c1 = sns.countplot(y='winner',order=wins.index,data = matches,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('Venues',fontsize=12)
 plt.xlabel('No: of matches won',fontsize=12)
 plt.title('Teams ranked on basis of winning matches',fontsize=15)
 plt.show()

def results():
 res = matches['result'].value_counts()
 plt.figure(figsize=(10,10))
 c1 = sns.countplot(x='result',order=res.index,data = matches,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('No of matches won',fontsize=12)
 plt.xlabel('Results',fontsize=12)
 plt.title('Results of the matches played',fontsize=15)
 plt.show()

def result_margin():
 res_mar = matches['result_margin'].value_counts().head(10)
 plt.figure(figsize=(10,10))
 c1 = sns.countplot(y='result_margin',order=res_mar.index,data = matches,palette = 'mako')
 c1.bar_label(c1.containers[0],size = 15)
 plt.ylabel('Margin',fontsize=12)
 plt.xlabel('No of matches won',fontsize=12)
 plt.title('Result margin by which the teams have won',fontsize=15)
 plt.show()



