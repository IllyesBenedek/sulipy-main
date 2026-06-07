azonositok = ['id10', 'id100', 'id23', 'id2', 'id13', 'id1']

rendezett = sorted(azonositok, key=lambda i: int(i[2:]))

print(rendezett)
