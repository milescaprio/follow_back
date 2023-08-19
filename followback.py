import importlib

x = input("1. Request from instagram\n2. Import json from file\n") 
if x == "1":
    import auth
    followers = auth.cl.user_followers(auth.ID)
    following = auth.cl.user_following(auth.ID)
    skeys = list(followers)
    gkeys = list(following)
    susers = [followers[i].username for i in skeys]
    gusers = [following[i].username for i in gkeys]

elif x == "2":
    folder = input("Insta data folder? (contains subfolder \"followers_and_following\"): ")
    import json
    followers = json.load(open(folder+"/followers_and_following/followers_1.json"))
    following = json.load(open(folder+"/followers_and_following/following.json"))
    followers = [i["string_list_data"][0]["value"] for i in followers]
    following = [i["string_list_data"][0]["value"] for i in following["relationships_following"]]
    susers = followers
    gusers = following



sgusers = set(susers) - set(gusers)
gsusers = set(gusers) - set(susers)
print("\n")
print("Followers:",susers,'\n')
print("Following:",gusers,'\n')
print("Not Following Back:",sgusers,'\n')
print("Not Followed Back:",gsusers,'\n')
y = input("Name of file to save to: ")
f = open("history/" + y, "w")
f.write("following = "+str(gusers)+"\nfollowers = "+str(susers) + "\nnot_following_back = "+str(list(set(susers)-set(gusers)))+"\nnot_followed_back = "+str(list(set(gusers)-set(susers))))


x = input("Would you like to compare with another log file? \n3. Compare old log of followers and following \n4. Compare old log of followers and following differences")

if x == "3":
    z = input("Old log file name: ")
    mod = importlib.import_module("history."+z)
    print("Used to follow: " + str(set(mod.following) - set(gusers)))
    print("Used to be followed by: " + str(set(mod.followers) - set(susers)))
    print("Newly followed: " + str(set(gusers) - set(mod.following)))
    print("Newly following: " + str(set(susers) - set(mod.followers)))

elif x == "4":
    z = input("Old log file name: ")

    mod = importlib.import_module("history."+z)
    print("Used to not be followed back: " + str(set(mod.not_followed_back) - gsusers),'\n')
    print("Used to not follow back: " + str(set(mod.not_following_back) - sgusers),'\n')
    print("Newly not followed back: " + str(gsusers - set(mod.not_followed_back)),'\n')
    print("Newly not following back: " + str(sgusers - set(mod.not_following_back)),'\n')
