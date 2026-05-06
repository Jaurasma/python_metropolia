def create_story():
    story = ""
    while True:
        word = input("Anna sana lisättäväksi tarinaan: ")
        if word == "loppu":
            break
        if story and word == story.split()[-1]:
            print("Sama sana peräkkäin, lopetetaan.")
            break
        story += word + " "
    print(story.strip())

if __name__ == "__main__":
    create_story()