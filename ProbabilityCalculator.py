# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 00:13:40 2022

@author: loren
"""

import copy
import random
# Consider using the modules imported above.

class Hat:     
    def __init__(self, **balls):
        self.contents = []        
        for (color, number) in balls.items():
            index = 0
            while index < number:
                self.contents.append(color)
                index += 1
    
    def draw(self, numberfordraw):
        index=0
        if numberfordraw >= len(self.contents):
            deleted = self.contents
            self.contents = []
        else:
            deleted = list() 
            while index < numberfordraw:                           
                random_item = random.randrange(len(self.contents))            
                deleted.append(self.contents[random_item])
                self.contents.pop(random_item)         
                index += 1     
        return deleted    
        
#hat2 = Hat(red=5, orange=4)     
#deleted = hat2.draw(3)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    index = 0
    positive_cases = 0
    while index < num_experiments:
        counts = dict()
        copyhat = copy.deepcopy(hat)
        drawn = copyhat.draw(num_balls_drawn)
        index +=1
        for name in drawn :
            if name not in counts:
                counts[name] = 1
            else:
                counts[name] = counts[name] + 1              
        rate = all((counts.get(k,0) >= v for k, v in expected_balls.items()))              
        if rate is True:
            positive_cases +=1
    probability = positive_cases/num_experiments        
    return probability    


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)


#expected_balls = {"blue":2, "red":1}    


#hat1 = Hat(yellow=3, blue=2, green=6)
#hat2 = Hat(red=5, orange=4)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)