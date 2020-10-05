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
        team = request.GET['Teams']
        team_df = Cleaned_df[Cleaned_df['Team'] == team] 
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

                    k = 5 if team == 'Kolkata Knight Riders' else 4
                    if t['Uncapped']< k:
                        My_team_11_index = samples
            except KeyError:
                continue
        Final_prediction = [j for j in team_df.loc[My_team_11_index]['Player_Name']]
        Roles = [j for j in team_df.loc[My_team_11_index]['Playing_Role']]
        
        context={}
        context =  {
         'Team': team,   
         'Final_prediction': Final_prediction,
         'Roles': Roles  
        }
        response = render(request,"result.html",context)
        return  response    

