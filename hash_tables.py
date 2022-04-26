voted = dict()


def check_person(name):
    if voted.get(name):
        print("Go out!")
        return

    voted[name] = True
    print("Vote!")


check_person("Bruno")
check_person("Bruno")
check_person("Geovana")
