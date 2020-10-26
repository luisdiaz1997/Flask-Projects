from nltk.corpus import wordnet as wn
import numpy as np
import nltk

people = wn.synset('people.n.01')
flower = wn.synset('flower.n.01')
animal = wn.synset('animal.n.01')

score_dict = {0:"people", 1:"flowers", 2:"animals"}

def set_category(labels_string):
    labels = labels_string.split()

    total_scores = list()
    for label in labels:
        if len(label)<4:
            continue
        if label[-1]=='s':
            label=label[:-1]

        try:
            current = wn.synset(label+".n.01")
        except(nltk.corpus.reader.wordnet.WordNetError):
            continue

        score_people = people.path_similarity(current)
        score_flower = flower.path_similarity(current)
        score_animal = animal.path_similarity(current)
        total_scores.append([score_people, score_flower, score_animal])

    total_scores = np.array(total_scores)
    total_mean = total_scores.mean(axis=0)
    total_max = total_scores.max(axis=0)

    absolute_score = total_mean*total_max*10
    print("total_max", total_max)
    print("absolute_score", absolute_score)
    i  = np.argmax(absolute_score)
    if absolute_score[i] > 0.25:
        print(score_dict[i])
        return score_dict[i]
    else:
        print("Other")
        return "other"
    