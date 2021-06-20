import numpy as np
import math
import itertools
import operator
import pandas as pd 
data = pd.read_csv("real_survey.csv") 
df = pd.DataFrame(data) 

# getiing inputs from user
math_score = int(input("Enter your Math Score : ")) 
ch_score = int(input("Enter your Chemistry Score : ")) 
ph_score = int(input("Enter your Physic Score : ")) 
# calculating avarage value based on user inputs
avag_user = (math_score + ch_score + ph_score) / 3
# rounding avarage value of user inputs
round_avg_user = round(avag_user)
# getting avarage value from dataset
df['avg'] = (df['math_score'] + df['ch_score'] + df['ph_score']) / 3
# rounding the data set values
round_avg = round(df['avg'])
# finding the nearest value in data set based on what the user avarage is 
nearest_value = min(round_avg, key=lambda x:abs(x-round_avg_user))
# comparing and getting result of the avarage value in dataset 
rslt_scores = df['study_under'][round_avg == nearest_value].to_string(index=False)
 
# asking user about thier hobby
choose_h = input("What is your hobby? \n 1- sport \n 2- games \n 3- reading \n 4- writing \n 5- traveling \n 6- other \n anwer: ") 
# comparing the user answer witj the dataset and outputing the most frequent program for given ansswer
rslt_hobby = df['study_under'][df['hobby'] == choose_h].value_counts().idxmax()

# asking user about thier type of game
choose_g = input("What games do you most prefer to play? \n 1- puzzle \n 2- thinking \n 3- sport \n 4- action \n 5- adventure \n 6- other \n anwer: ") 
# comparing the user answer witj the dataset and outputing the most frequent program for given ansswer
rslt_game = df['study_under'][df['game'] == choose_g].value_counts().idxmax()

array=[rslt_scores, rslt_hobby, rslt_game]

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

print ('We recomend',most_common(array), 'For you.')