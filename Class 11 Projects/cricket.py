teams = {"India":["Rohit","Dhawan","Kohli","Rayudu","Dhoni","Jadhav","Shankar","Bhuvneshwar","Kuldeep","Shami","Chahal"],
         "New Zealand":["Guptill","Munro","Williamson","Taylor","Latham","Nicholls","Grandhomme","Bracewell","Sodhi","Ferguson","Boult"],
         "England":["Burns","Jennings","Bairstow","Root","Stokes","Buttler","Ali","Foakes","Curran","Rashid","Anderson"],
         "West Indies":["Brathwaite","Campbell","Hope","Bravo","Chase","Hetmyer","Dowrich","Holder","Roach","Joseph","Gabriel"],
         "Australia":["Harris","Burns","Khawaja","Labuschagne","Head","Patterson","Paine","Cummins","Starc","Lyon","Richardson"],
         "Sri Lanka":["Karunaratne","Thirimanne","Chandimal","Mendis","Silva","DeSilva","Dickwella","Perera","Lakmal","Chameera","Kumara"],
         "South Africa":["deCock","Amla","Hendricks","duPlessis","Dussen","Miller","Phehlukwayo","Rabada","Beuran","Shamsi","Steyn"],
         "Pakistan":["Haq","Zaman","Azam","Hafeez","Malik","Wasim","Hasan","Sarfraz","Shadab","Amir","Afridi"]
         }

def cricket():
    x=int(input("How many overs? "))
    print ("PLAYER 1:")
    player1=input("Enter name: ")
    p1=inning(x,9999)
    print ("PLAYER 2:")
    player2=input("Enter name: ")
    p2=inning(x,p1)
    if p1>p2:
        print (player1,"won!")
    elif p2>p1:
        print (player2,"won!")
    else:
        print ("Its a tie!")

def inning(overs_max,prev_score):
    import random
    out_list=("Run Out","Caught","Bowled","Stumped","Hit Wicket")
    runs_total=0
    out_total=0
    team=[]
    teamscore=[0,0,0,0,0,0,0,0,0,0,0]
    teamout=["","","","","","","","","","",""]
    teamballs=[0,0,0,0,0,0,0,0,0,0,0]
    print ("Which team do you want from")
    for a in teams:
        print (a)
    del a
    team_name=input()
    if team_name in teams:
        team=teams[team_name]
    else:
        print ("You have chosen a custom team")
        for a in range (0,11,1):
            player=input("Enter cricketer name: ")
            team.append(player)
        del a
    print ("BEGIN!")
    p1=team[0]
    p2=team[1]
    p=p1
    for overs in range(0,overs_max):
        runs_over=0
        out_over=0
        balls=1
        while balls<7:
            o=0
            r=0
            a=random.randint(0,2000)
            for pch in range(0,11):
                if p==team[pch]:
                    pbh=pch
                    break
            print (p,"on strike")
            x=input("Attack-8/Defend-9/Loft-0: ")
            ballno=str(overs)+"."+str(balls)+":"
            print (ballno,end=" ")
            if a==666:
                o=1
                out=out_list[4]
            elif x=="8":
                if a<(50+(pbh*5)):
                    o=1
                    out=out_list[2]
                elif a%150==0:
                    o=1
                    out=out_list[0]
                elif a<500+(pbh*10):
                    r=0
                elif a<1000+(pbh*10):
                    r=1
                elif a<1600+(pbh*10):
                    r=2
                elif a<1650+(pbh*10):
                    r=3
                else:
                    r=4
                    four=1
            elif x=="9":
                if a<20:
                    o=1
                    out=out_list[2]
                elif a<1500:
                    r=0
                else:
                    r=1
            elif x=="0":
                if a<200+(pbh*20):
                    o=1
                    out=out_list[1]
                elif a<250+(pbh*20):
                    o=1
                    out=out_list[2]
                elif a%50==0:
                    o=1
                    out=out_list[0]
                elif a<500+(pbh*30):
                    r=0                   
                elif a<800+(pbh*30):
                    r=1
                elif a<1300+(pbh*30):
                    r=2
                elif a<1400+(pbh*20):
                    r=3
                elif a<1600+(pbh*20):
                    r=4
                    four=1
                else:
                    r=6
                    six=1
            else:
                continue
            if o==1:
                out_over+=1
                out_total+=1
                print ("Player out due to",out)
                teamout[pch]=out
                for pah in range(0,11):
                    if teamout[pah]=="" and team[pah]!=p1 and team[pah]!=p2:
                        if p==p1:
                            p1=team[pah]
                            p=p1
                        elif p==p2:
                            p2=team[pah]
                            p=p2
                        break
                del pah
            elif r==6:
                print ("IT IS A SIX!!!")
            elif r==4:
                print ("IT IS A FOUR!!!")
            elif r in (1,2,3,5):
                print (r,"runs!")
            elif r==0:
                print ("Dot ball")
            runs_over+=r
            runs_total+=r
            if out_total==10:
                print ("ALL OUT")
                break
            print ("Score:",runs_total,"/",out_total)
            print ("")
            teamscore[pch]+=r
            teamballs[pch]+=1
            if r in (1,3):
                if p==p1:
                    p=p2
                else:
                    p=p1
            balls+=1
            if runs_total>prev_score:
                break
        if out_total==10:
            break
        if runs_total>prev_score:
            break
        print ("Over",(overs+1),"completed.",runs_over,"runs and",out_over,"wickets")
        if runs_over==0 and out_over==0:
            print ("Maiden Over")
        print ("")
        if p==p1:
            p=p2
        else:
            p=p1
    print ("The final score is",runs_total,"/",out_total)
    for pah in range (0,11):
        print (team[pah],end=" ")
        if teamout[pah]!="":
            print (":",teamscore[pah],"runs,",teamballs[pah],"balls played, strike rate:",(((teamscore[pah]/teamballs[pah])*100)//1),",out by",teamout[pah])
        else:
            print ("*", end=" ")
            if teamballs[pah]!=0:
                print (":",teamscore[pah],"runs,",teamballs[pah],"balls played")
            else:
                print ("")
    return (runs_total)
        
                    
                
                    
                    


        
