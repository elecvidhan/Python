name = input("What's your name? ")

match name:
    case "harry" | "hermione" | "ron":
        print("grifyndoor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")
