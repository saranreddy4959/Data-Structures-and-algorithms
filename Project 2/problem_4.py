class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    for users in group.users:
        if (users == user):
            return True
    for g in group.groups:
        if (is_user_in_group(user, g)):
            return True
    return False
#Test case-1
print(is_user_in_group("sub_child_user", parent))

#Test case-2
movies = Group("English")
movies.add_user("John Wick")
movies.add_user("Dark Phoneix")
marvel = Group ("Marvel")
marvel.add_user("Avengers")
marvel.add_user("Spider Man")
marvel.add_user("Thor")
movies.add_group(marvel)
dc_ = Group("DC Comics")
dc_.add_user("SuperMan")
dc_.add_user("Wonder Women")
dc_.add_user("Batman")
movies.add_group(dc_)
songs = Group("Songs")
songs.add_user("Counting Stars")
img_dragons = Group("Imagine Dragons")
evolve = Group("Evolve")
evolve.add_user("Whatever It takes")
evolve.add_user("Thunder")
evolve.add_user("Believer")
origins = Group ("Origins")
origins.add_user("Natural")
origins.add_user("Bad Liar")
origins.add_user("Digital")
origins2 = Group("Origins_part2")
origins2.add_user("Boomerang")
origins2.add_user("Real Life")
origins.add_group(origins2)
img_dragons.add_group(evolve)
img_dragons.add_group(origins)
songs.add_group(img_dragons)

main_directory = Group("Entertainment")
main_directory.add_user("picture.jpeg")
main_directory.add_user("picture2.png")
main_directory.add_group(movies)
main_directory.add_group(songs)

print(is_user_in_group("Avengers", main_directory))  #True

#Test-Case-3
print(is_user_in_group("Counting Stars", main_directory)) #True
print(is_user_in_group("C", main_directory)) #False
print(is_user_in_group("picture2.png", main_directory))#True
print(is_user_in_group(" ", main_directory)) #False
