mondat = input("Írj be egy mondatot (ENTER a véghez): ")

while mondat != "":
    utolso = mondat[-1]

    if utolso == ".":
        print("Kijelentő mondat!")
    elif utolso == "?":
        print("Kérdő mondat!")
    elif utolso == "!":
        print("Felkiáltó / felszólító / óhajtó mondat!")
    else:
        print("Ismeretlen mondatvégi jel!")

    mondat = input("Írj be egy mondatot (ENTER a véghez): ")

print("Viszlát!")
