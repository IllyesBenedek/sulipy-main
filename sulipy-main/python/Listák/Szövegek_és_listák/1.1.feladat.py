mondat = input("Írj be egy mondatot: ")

utolso = mondat[-1]

if utolso == ".":
    print("Kijelentő mondat!")
elif utolso == "?":
    print("Kérdő mondat!")
elif utolso == "!":
    print("Felkiáltó / felszólító / óhajtó mondat!")
else:
    print("Ismeretlen mondatvégi jel!")
