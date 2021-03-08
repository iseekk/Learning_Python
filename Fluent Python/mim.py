import json


def plus(a, b):
    return a + b


def display(string, a, b):
    return "{}: {}".format(string, plus(a, b))


class Application:
    def get_next_person(self, user):
        person = self.get_random_person()
        while person in user['people seen']:
            person = self.get_random_person()
        return person

    def get_random_person(self):
        pass

    def evaluate(self, person1, person2):
        if person1 in person2["likes"]:
            self.send_email(person1)
            self.send_email(person2)
        elif person1 in person2["dislikes"]:
            self.let_down_gently(person1)
        elif person1 not in person2["dislikes"] \
                and person1 not in person2["likes"]:
            self.give_it_time(person1)

    def send_email(self, person):
        pass

    def let_down_gently(self, person):
        pass

    def give_it_time(self, person):
        pass


def get_json(filename):
    try:
        return json.loads(open(filename).read())
    except (IOError, ValueError):
        return ""
