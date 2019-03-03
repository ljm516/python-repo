from collections import deque


def person_is_find(person):
    return person.endswith('m')


# 广度优先搜索
def search(name):
    ljm_dict = {
        "you": ["alice", "claire", "bob"],
        "bob": ["anuj", "peggy"], "alice": ["peggy"],
        "claire": ["jonny", "thom"], "peggy": [],
        "anuj": [], "jonny": [], "thom": []
    }
    searched_list = []
    search_queue = deque()
    search_queue += ljm_dict[name]

    while search_queue:
        person = search_queue.popleft()
        print("person: {p}".format(p=person))
        if person not in searched_list:
            if person_is_find(person):
                print("{person} has finded...".format(person=person))
                return True
            else:
                search_queue += ljm_dict[person]
                searched_list.append(person)

    return False


search("you")
