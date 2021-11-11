# Three is a Crowd
def crowd_test(names):
    if(len(names) > 5):
        print("There's a mob in the room!\n")
    elif(len(names) <= 5 and len(names) >= 3):
        print("The room is crowded.\n")
    elif(len(names) == 1 or len(names) == 2):
        print("The room is not that crowded!\n")
    else:
        print("The room is empty.\n")

names = ["Michael", "Taimur", "Sebnem", "Alice", "Xander", "Hunter", "Eiko", "Chase", "Vanessa"]

while(len(names) > 0):
    print(names)
    crowd_test(names)
    names.pop()
crowd_test(names)

