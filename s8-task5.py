instagram_followers = [120,1500,23000,800,45000]

for follower in instagram_followers:

    if follower < 1000:
        print("Micro!!")
    elif follower <= 10000:
        print("Influencer!!")
    else:
        print("Celebrity!!")