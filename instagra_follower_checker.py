def load_usernames_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def find_unfollowers(followers, following):
    return [user for user in following if user not in followers]

if __name__ == "__main__":

    name1 = "/followers.txt"
    name2 = "/following.txt"

    file_path = "C:\Folder1\Folder2\..." # paste hete te txt-s path (right click on the txt, properties and location)

    followers = load_usernames_from_file(file_path + name1)
    following = load_usernames_from_file(file_path + name2)


    unfollowers = find_unfollowers(followers, following)


    print("Users in 'following' but not in 'followers':")




for user in unfollowers:
        print(user)
    

'''
line = False
for user in unfollowers:
    if line == False:
        print(user, end=": ")
        line = True
    else:
        print(user)
        line = False
'''
