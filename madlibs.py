## string concatenation (aka how to put string together)
# # suppose we want to create a string that says "subscribe to ____"
# youtuber = "kylie ying" # some string variable 

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_persion = input("famous persion: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to{verb1}. Stay hydrated and {verb2} like you are {famous_persion}!" 
print(madlib)