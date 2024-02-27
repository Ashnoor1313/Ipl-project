import pandas as pd
import matplotlib.pyplot as plt
import Module as m
Df=pd.read_csv('IPL.csv')

print('This project gives the analysis of all matches of the IPL from 2008 to 2020')
print('This file IPl.csv has been taken from www.kaggle.com')
print('This file gives the basic analysis of the following: ')
print('1.)Number of matches played in any two cities.')
print('2.)Number of matches won by either wickets or by Runs.')
print('3.)Number of matches played by any two teams.')
print('4.)More number of matches won either by runs or by wickets.')
print('5.)Most  decisions taken by teams after winning toss.')
print('6.)Comparison between the player of match award won by a plyaer.')
print('7.)Details of a match on a given date.')
print('8.)Number of matches won by any two teams.')
print('9.)Matches won by how much result margin.')
print('10.)Number of tosses won by a team.')

print('---------------------------------------------')

while True:
    print('MAIN MENU')
    print('1-For performing operation on DATAFRAMES.')
    print('2-For TEXTUAL ANALYSIS.')
    print('3-For GRAPHICAL ANALYSIS.')
    print('-----------------------------------------')
    code = eval(input('Enter the option number which you want to operate: '))
    print()
    if code == 1:
        m.Dataframes()
       

    elif code == 2:
        m.Text()
        
    elif code == 3:
        m.graph()
        
    else:
        print('END')
        
 
