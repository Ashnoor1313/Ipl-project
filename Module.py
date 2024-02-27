import pandas as pd
import graphs as gs

Df=pd.read_csv('IPL.csv')

def Dataframes():
    while True:
        print('Menu for manipulation of the dataframe')
        print('-----------------------------------------------------')

        print('Choose the option from the following options:')
        print()

        print('1- To display the name of various cities in which matches are conducted')
        print('2- To display the No of stadiums in which matches are conducted')
        print('3- To display the name of the teams which played the tournament at least once')
        print('4- To display the no of umpires who have umpired in the tournament so far')
        print('5- To display the name of the Stadiums ')
        print('6- To display the name of the player of the match')
        print('-----------------------------------------------------')


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
def Text():

    print('Menu for Text based Analysis')
    print()

    while True:
        print('1-Comparison of no of matches played in any two cities :')
        print('2-To find the number of matches won by either wickets or by Runs: ')
        print('3-Comparison between number of matches played by any two teams :')
        print('4-Comparison of more no of matches played at two venues.')
        print('5-Most  decisions taken by teams after winning toss.')
        print('6-Comparison between the playeer of match award won by a plyaer.')
        print('7-To display the details of a match on a given date.')
        print('8-Analysis of the no of matches won by any two teams.')
        print('9-Comparison between no of matches umpired by any 2 umpires.')
        print('10-Comparison between Number of tosses won by a team.')
        print()
        
        code = eval(input('Enter the option number : '))
        print()

        if code == 1:
            print('List of cities:')
            print('Mumbai')
            print('Bangalore')
            print('Chandigarh')
            print('Delhi')
            print('Kolkata')
            print('Chennai')
            print('Jaipur')
            print('Hyderabad')
            print('Cape Town')
            print('Durban')
            print('Port Elizabeth')
            print('Centurion')
            print('Johannesburg')
            print('East London')
            print('Kimberly')
            print('Cuttack')
            print('Ahemdabad')
            print('Dubai')
            print('Sharjah')
            print('Abu Dhabi')
            print()
                
            a=input('Enter the code for the  first city: ')
            b=input('Enter the code for the second city: ')
            c=Df[Df.city==a]
            d=Df[Df.city==b]
            print('Number of matches played in',a,'is',c.size,'and number of matches played in',b,'is',d.size)
            input()

        elif code == 2:
            print('runs-The result is by runs')
            print('wickets-The result is by wickets')
            print()
            x=input('Enter the type of result: ')
            a=Df[Df.result==x]
            print('Number of matches won by the result type',x,' are: ')
            print(a.size)
            input()    
            
        elif code == 3:
            print('Names of Teams are: ')
            print('Mumbai Indians')
            print('Chennai Super Kings')
            print('Kolkata Knight Riders')
            print('Royal Challengers Bangalore')
            print('Kings XI Punjab')
            print('Delhi Capitals')
            print('Rajasthans Royals')
            print('Sunrisers Hyderabad')
            print('Deccan Chargers')
            print('Delhi Daredevils')
            print('Gujrat Lions')
            print('Rising Pune Supergiant')
            print('Pune Warriors')
                
            T1=input('Enter the name of first team: ')
            T2=input('Enter the name of second team: ')
            x=Df[Df.team1==T1]
            y=Df[Df.team1==T2]
            print('Number of matches played by',T1,'is',x.size)
            print('Number of matches played by',T2,'is',y.size)
            input()

        elif code == 4:
            print('List of Venues: ')
            print('M Chinnaswamy Stadium')
            print('Punjab Cricket Association Stadium, Mohali')
            print('Feroz Shah Kotla')
            print('Wankhede Stadium')
            print('Eden Gardens')
            print('Sawai Mansingh Stadium')
            print('Rajiv Gandhi International Stadium,Uppal')
            print('MA Chidambaram Stadium,Chepauk')
            print('Dr DY Patil Sports Academy')
            print('Newlands')
            print('Kingsmead')
            print('SuperSport Park')
            print('Buffalo Park')
            print('New Wanderes Sradium')
            print('St Georges Park')
            print('De Beers Diamond Oval')
            print('Sheikh Zayed Stadium')
            print('Dubai International Cricket Stadium')
            print('Sharjah Cricket Stadium')
                  
            x=input('Enter the name of first stadium: ')
            y=input('Enter the name of the second stadium: ')
            a=Df[Df.venue==x]
            b=Df[Df.venue==y]
            print()
            print('Number of matches played at',x,'is',a.size)
            print('Number of matches played at',y,'is',b.size)
            input()

        elif code == 5:
            print('Decisions taken by a team after winning toss are bat or field')
            print()
            x=input('Enter the decision taken during toss: ')
            a=Df[Df.toss_decision==x]
            b=a.size
            print('Number of times the decision of',x,'taken by a team is',b)
            input()

        elif code == 6:
            p1=input('Enter the name of player 1: ')
            p2=input('Enter the name of player 2: ')
            a=Df[Df.player_of_match==p1]
            b=Df[Df.player_of_match==p2]
            print('Number of times player of match award won by',p1,'is',a.size)
            print('Number of times player of match award won by',p2,'is',b.size)
            input()

        elif code == 7:
            y=input('Enter the date in the following format MM/DD/YY: ')
            a=Df[Df.date==y]
            print('Details of the match played on any given date are: ')
            print(a)
            input()

        elif code == 8:
            print('Names of Teams are: ')
            print('Mumbai Indians')
            print('Chennai Super Kings')
            print('Kolkata Knight Riders')
            print('Royal Challengers Bangalore')
            print('Kings XI Punjab')
            print('Delhi Capitals')
            print('Rajasthans Royals')
            print('Sunrisers Hyderabad')
            print('Deccan Chargers')
            print('Delhi Daredevils')
            print('Gujrat Lions')
            print('Rising Pune Supergiant')
            print('Pune Warriors')
            print()    
            a=input('Enter the name of team1: ')
            b=input('Enter the name of team2: ')
            print()
            c=Df[Df.winner==a]
            d=Df[Df.winner==b]
            print('Number of matches won by',a,'are',c.size)
            print('Number of matches won by',b,'are',d.size)
            input()

        elif code == 9:
            print('Name of the umpires are: ')
            print('Asad Rauf')
            print('MR Benson')
            print('Aleem Dar')
            print('SJ Davis')
            print('BF Bowden')
            print('IL Howell')
            print('DJ Harper')
            print('RE Koertzen')
            print('BR Doctrove')
            print('VK Sharma')
            print('CB Gaffaney')
            print('AY Dandekar')
            print('YC Barde')
            print('C Shamshuddin')
            print('RK Illingworth')
            print('UV Gandhe')
            print('AK Chaudhary')
            print('Nitin Menon')
            print()

            a=input('Enter the name of umpire1: ')
            b=input('Enter the name of umpire2: ')
            print()
            c=Df[Df.umpire1==a]
            d=Df[Df.umpire2==b]
            print('Number of matches umpired by',a,'are',c.size)
            print('Number of matches umpired by',b,'are',d.size)
            input()
            
        elif code == 10:
            print('Names of Teams are: ')
            print('Mumbai Indians')
            print('Chennai Super Kings')
            print('Kolkata Knight Riders')
            print('Royal Challengers Bangalore')
            print('Kings XI Punjab')
            print('Delhi Capitals')
            print('Rajasthans Royals')
            print('Sunrisers Hyderabad')
            print('Deccan Chargers')
            print('Delhi Daredevils')
            print('Gujrat Lions')
            print('Rising Pune Supergiant')
            print('Pune Warriors')
            print()    
            
            a=input('Enter the name of team1: ')
            b=input('Enter the name of team2: ')
            print()
            x=Df[Df.toss_winner==a]
            y=Df[Df.toss_winner==b]
            print('Number of tosses won by',a,'are',x.size)
            print('Number of tosses won by',b,'are',y.size)
            input()

        else:
            print('Your program is over')
            
            break                                                                                                                                                                                                                                                        




    
def graph():
    while True:
        print('Graphical Analysis Menu')
        print('------------------------------------------------')
        print('1-To display runs distribution match wise.')
        print('2-To display runs scored over the years.')
        print('3-To display preferred toss decision.')
        print('4-To display Total runs and wickets by over.')
        print('5-To display runs distribution over wise.')
        print('6-To diplay top 10 cities in which matches were held.')
        print('7-to display top 10 players who won player of the match.')
        print('8-To display top 10 venues where matches were held.')
        print('9-To display Teams ranked on basis of winning toss.')
        print('10-To display Teams ranked on basis of winning matches.')
        print('11-To display results of matches played.')
        print('12-To display result margin by which teams have won.')
        print('------------------------------------------------')
        
        
        code=eval(input('Enter the option number on which you want to perform operation: '))
        print()
        if code == 1:
            gs.runs_dist()

        elif code == 2:
            gs.runs()

        elif code == 3:
            gs.toss()

        elif code == 4:
            gs.wickets()

        elif code == 5:
            gs.runs_box()

        elif code == 6:
            gs.cities()

        elif code == 7:
            gs.players()

        elif code == 8:
            gs.venues()

        elif code == 9:
            gs.ranking_toss()

        elif code == 10:
            gs.ranking()
        
        elif code == 11:
            gs.results()

        elif code == 12:
            gs.result_margin()

        else:
            print('END')
           
            break     

           



