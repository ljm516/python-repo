class Person(object):
    def __init__(self, name, age, address, subject, score):
        self.name = name
        self.age = age
        self.address = address
        self.subject = subject
        self.score = score


if __name__ == '__main__':
    p_1 = Person('ljm', 25, 'beijing', 'python', 60)
    p_2 = Person('ljm', 25, 'beijing', 'java', 70)
    p_3 = Person('cy', 18, 'wuhan', 'python', 60)

    p_list = [p_1, p_2, p_3]
    p_dict = {}

for p in p_list:

    if p.name in p_dict.keys():
        p_dict[p.name]['subject'].append({"name": p.subject, "score": p.score})
    else:
        p_dict[p.name] = {"address": p.address, "age": p.age, "subject": []}
        score_dict = {"name": p.subject, "score": p.score}
        p_dict[p.name]['subject'].append(score_dict)

print(p_dict)
