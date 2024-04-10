import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import random

from .ListOfRecom import first_rec, zero_rec, sec_rec


# Create train set

X = []
y = []

for i in range(1000):
    time = random.randint(0, 32400)  # max - 9 hours

    emotional_state = random.choice(["весело", "нейтрально", "грустно"])

    # "отдыхать" -> 0
    # "перерыв" -> 1
    # "работать" -> 2

    if time < 18000 and emotional_state in ["нейтрально", "весело"]:
        recommendation = 2
    elif time < 18000 and emotional_state == "грустно":
        recommendation = 1
    elif time >= 18000 and emotional_state == "грустно":
        recommendation = 1
    elif time >= 18000 and emotional_state == "весело":
        recommendation = 0
    else:
        recommendation = random.choice([0, 1])

    X.append([time, emotional_state])
    y.append(recommendation)

# convert into dataframe
X_df = pd.DataFrame(X, columns=['time', 'emotional state'])
y_df = pd.DataFrame(y, columns=['recommendation'])

# Encoding
X_encoded = pd.get_dummies(X_df)

# Splt data
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_df, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Create recommendations for each class
recommendations = {
    0: zero_rec,
    1: first_rec,
    2: sec_rec
}


def get_recommendation(data):
    y_pred = model.predict([data['time'], data['emotion']])

    for pred_class in y_pred:
        if pred_class in recommendations:
            recommendations_for_class = recommendations[pred_class]
            random_recommendation = random.choice(recommendations_for_class)
            print("Рекомендация для сотрудника:", random_recommendation)
        else:
            print("Класс рекомендации не найден в словаре")
    return random_recommendation
