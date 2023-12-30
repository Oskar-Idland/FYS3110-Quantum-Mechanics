import matplotlib.pyplot as plt
import numpy as np

# Reads data from textfile and plots bar chart

# Open and read data file
import matplotlib.pyplot as plt
import numpy as np


def extract_score(filename):
    results = {}
    with open(filename, 'r') as file:
        for line in file:
            score = int(line.split()[1])
            
            if score not in results.keys():
                results[score] = 1
            else:
                results[score] += 1
    
    score = list(results.keys())
    people = list(results.values())
    return score, people

score, people = extract_score('midterm_score.txt')
arr = []
for i in range(len(score)):
    arr.append(score[i]*people[i])



fontsize = 14
unique_score = list(set(score))
median = np.median(score)
print(median)
plt.bar(score,people, width=0.75)
plt.xticks(unique_score, fontsize=fontsize-4)
plt.xlabel('Score', fontsize=fontsize)
plt.ylabel('People', fontsize=fontsize, labelpad=1)
plt.title(f'Midterm Results from {sum(people)} Students\nWith an average: {sum(arr)/sum(people): .2f}', fontsize=fontsize+3)
plt.show()