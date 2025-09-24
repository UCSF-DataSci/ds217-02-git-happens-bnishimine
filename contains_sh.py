
again = "yes"
while again == "yes":
    maybe_sh = input("Enter a word or sentence (all lowercase): ")

    if "sh" in maybe_sh:
        print("Found 'sh'")
    else:
        print("No 'sh' found")

    again = input("Do you want to try again? (yes/no): ")
