def winner(names, scores):
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]

def average(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum = sum + scores[i]
    return (sum / len(scores))

def ranking(names, scores):
    indices = list(range(len(names)))
    indices.sort(key=lambda i: -scores[i])
    return [names[i] for i in indices]

def above_average(names, scores):
    avg = average(scores)
    return [names[i] for i in range(len(scores)) if scores[i] > avg]

names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
print(winner(names, scores))
print(round(average(scores),2))
print(ranking(names, scores))
print(above_average(names, scores))