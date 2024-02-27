import pandas as pd, numpy as np

Df=pd.read_csv('IPL.csv')

print('Menu for manipulation of the dataframe')
print()

print('Choose the option from the following options:')
print()

print('1- To display the name of various cities in which matches are conducted')
print('2- To display the No of stadiums in which matches are conducted')
print('3- To display the name of the teams which played the tournament at least once')
print('4- To display the no of umpires who have umpired in the tournament so far')
print('5- To display the name of the Stadiums ')
print('6- To display the name of the player of the match')
print()


a=eval(input('Enter the option Number:'))
print()

while True:
    if a==1:
        print('Name of the cities in which Matches are conducted are: ')
        print(Df['city'].unique())
        input()

    elif a==2:
        print('Number of the stadiums in which matches are conducted are: ')
        print(Df['venue'].nunique())
        input()
        
    elif a==3:
        print(Df['team1'].unique())
        input()
            
    elif a==4:
        print('Number of First umpires who have umpired in the tournament are:')
        print(Df['umpire1'].nunique())
        input()

    elif a==5:
        print('Name of the stadiums: ' )
        print(Df['venue'].unique())
        input()
        
    elif a==6:
        print('Name of player of  the match are')
        print(Df['player_of_match'].unique())
        input()

    else:
        print('Exit')

    break    
      
