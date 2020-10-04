from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db import models
import pandas as pd
import numpy as np
import random


Cleaned_df = pd.read_excel('Final_excel.xlsx')



def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def models(request):
    if 'Chennai Super Kings' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Chennai Super Kings'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context={}
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        response = render(request,"result.html",context)
        return  response



    if 'Delhi Capitals' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Delhi Capitals'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context={}
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        return  render(request,"result.html",context)




    if 'Kings XI Punjab' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Kings XI Punjab'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        return  render(request,"result.html",context)




    if 'Kolkata Knight Riders' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Kolkata Knight Riders'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<5:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        return  render(request,"result.html",context)




    if 'Mumbai Indians' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Mumbai Indians'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        return  render(request,"result.html",context)




    if 'Rajasthan Royals' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Rajasthan Royals'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
            }
        return  render(request,"result.html",context)




    if 'Royal Challengers Bangalore' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Royal Challengers Bangalore'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        return  render(request,"result.html",context)



    if 'Sunrisers Hyderabad' in request.POST:
        team_df = Cleaned_df[Cleaned_df['Team'] == 'Sunrisers Hyderabad'] 
        A = list(i for i, j in team_df[team_df['IsCaptain']=='Captain'].iterrows())
        B = list(i for i, j in team_df[(team_df['Playing_Role']=='Opening batsman')|(team_df['Playing_Role']=='Top-order batsman')|(team_df['Playing_Role']=='Batsman')|(team_df['Playing_Role']=='Middle-order batsman')].iterrows())
        C = list(i for i, j in team_df[(team_df['Playing_Role']=='Batting allrounder')|(team_df['Playing_Role']=='Bowling allrounder')].iterrows())
        D = list(i for i, j in team_df[team_df['Playing_Role']=='Bowler'].iterrows())
        E = list(i for i, j in team_df[team_df['Playing_Role']=='Wicketkeeper batsman'].iterrows())

        My_team_11_index = []

        while len(My_team_11_index)==0:
            samples = []
            samples.append((sorted(random.sample(A, 1))))

            if A[0] in B:
                B.remove(A[0])
                samples.append((sorted(random.sample(B, 3))))
            else:
                samples.append((sorted(random.sample(B, 3))))

            if team_df.loc[A]['Playing_Role'].item()!='Wicketkeeper batsman':
                samples.append((sorted(random.sample(E, 1))))
                samples.append((sorted(random.sample(C, 2))))
            else:  
                samples.append((sorted(random.sample(C, 3))))

            samples.append((sorted(random.sample(D, 4))))

            samples = [j for i in samples for j in i]

            s = team_df.loc[samples].groupby('IsOverseasPlayer')['IsOverseasPlayer'].count()
            t = team_df.loc[samples].groupby('IsUncapped')['IsUncapped'].count()
            try:
                if s['Overseas Player']==4:
                    if t['Uncapped']<4:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context =  {
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        return  render(request,"result.html",context)
 
    
