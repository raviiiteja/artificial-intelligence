import math

data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
]

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

def entropy(data):
    total = len(data)

    yes = sum(row[-1] == 'Yes' for row in data)
    no = sum(row[-1] == 'No' for row in data)

    result = 0

    for count in [yes, no]:
        if count > 0:
            p = count / total
            result -= p * math.log2(p)

    return result

def information_gain(data, feature_index):
    total_entropy = entropy(data)

    values = set(row[feature_index] for row in data)

    weighted_entropy = 0

    for value in values:
        subset = [
            row for row in data
            if row[feature_index] == value
        ]

        weight = len(subset) / len(data)

        weighted_entropy += weight * entropy(subset)

    return total_entropy - weighted_entropy


def best_feature(data, features):
    gains = []

    for i in range(len(features)):
        gain = information_gain(data, i)
        gains.append(gain)

    best_index = gains.index(max(gains))

    return best_index

def build_tree(data, features):

    labels = [row[-1] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    
    if len(features) == 0:
        return max(set(labels), key=labels.count)

    
    best_index = best_feature(data, features)
    best_feature_name = features[best_index]

    tree = {best_feature_name: {}}

    values = set(row[best_index] for row in data)

    for value in values:

        subset = [
            row for row in data
            if row[best_index] == value
        ]

        new_features = features[:best_index] + features[best_index + 1:]

        new_data = [
            row[:best_index] + row[best_index + 1:]
            for row in subset
        ]

        tree[best_feature_name][value] = build_tree(
            new_data,
            new_features
        )

    return tree



tree = build_tree(data, features)

print("Decision Tree:")
print(tree)