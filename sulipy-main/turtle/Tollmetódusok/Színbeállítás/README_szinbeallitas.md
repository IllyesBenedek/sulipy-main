# Színbeállítás

## Vonalszín

```python
turtle.pencolor(*args)
```

**Lehetséges argumentumok:**
- nincs megadva: az aktuális értékkel tér vissza
- szín-sztring: például `"red"`, `"yellow"`, `"#33cc8c"`
- szín-tuple: például `(125, 30, 170)` — RGB értékek: vörös, zöld és kék 0-255 közötti értékei

---

## Kitöltőszín

```python
turtle.fillcolor(*args)
```

**Lehetséges argumentumok:**
- nincs megadva: az aktuális értékkel tér vissza
- szín-sztring: például `"red"`, `"yellow"`, `"#33cc8c"`
- szín-tuple: például `(125, 30, 170)` — RGB értékek: vörös, zöld és kék 0-255 közötti értékei

---

## Vonal és kitöltőszín egyszerre

```python
turtle.color(*args)
```

**Lehetséges argumentumok:**
- nincs megadva: az aktuális értékkel tér vissza
- szín-sztring: például `"red"`, `"yellow"`, `"#33cc8c"`
- szín-tuple: például `(125, 30, 170)` — RGB értékek: vörös, zöld és kék 0-255 közötti értékei

**Példák:**
```python
turtle.color("red", "green")  # vonalszín piros, kitöltőszín zöld
turtle.color()                # aktuális értékek lekérdezése
```
