# Three is a Crowd
def crowd_test(names):
    if(len(names) > 3):
        print("The room is crowded!\n")
    else:
        print("The room isn't that crowded.\n")

names = ["Michael", "Taimur", "Sebnem", "Alice", "Xander", "Hunter", "Eiko", "Chase", "Vanessa"]
print(names)
crowd_test(names)

# Pop names from list
print("Currently removing people from the room...")
while(len(names) > 3):
    names.pop()
print(names)
crowd_test(names)

