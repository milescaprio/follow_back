
#Enter username and password here for authentication.
#Use at your own risk.
#Will not work with 2fa.
U = ""
P = ""


from instagrapi import Client
cl = Client()
cl.login(U,P)
print(cl)
ID = cl.user_id_from_username(U)
print(ID)
