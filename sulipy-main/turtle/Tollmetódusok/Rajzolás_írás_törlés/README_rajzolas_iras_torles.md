# Rajzolás, írás, törlés

## Tollat le

Tollat le: rajzol.

```python
turtle.pendown()
turtle.pd()
turtle.down()
```

---

## Tollat fel

Tollat fel: nem rajzol.

```python
turtle.penup()
turtle.pu()
turtle.up()
```

---

## Toll lent

Megadja, hogy a toll lent van-e. `True` vagy `False` értékkel tér vissza.

```python
turtle.isdown()
```

---

## Vonalvastagság

Toll vastagságának lekérdezése vagy beállítása.

```python
turtle.pensize(width=None)
turtle.width(width=None)
```

**Paraméterek:**
- `width` (szélesség): szám, ha nincs megadva, az aktuális értékkel tér vissza

---

## Toll beállítása

```python
turtle.pen(pen=None, **pendict)
```

**Paraméterek:**
- `pen` (toll): szótár az alábbi kulcsokkal
- `pendict`: kulcsszó-argumentum

**Lehetséges kulcsok:**
- `"shown"`: `True` / `False`
- `"pendown"`: `True` / `False`
- `"pencolor"`: szín-sztring vagy szín-tuple
- `"fillcolor"`: szín-sztring vagy szín-tuple
- `"pensize"`: pozitív szám
- `"speed"`: szám 0 és 10 között
- `"resizemode"`: `"auto"` / `"user"` / `"noresize"`
- `"stretchfactor"`: (pozitív szám, pozitív szám)
- `"outline"`: pozitív szám
- `"tilt"`: szám

> Ez a szótár használható argumentumként egy későbbi `pen()` metódushíváshoz, vagy a korábbi tollállapot visszaállításához. Ezenfelül ezen attribútumok közül egy vagy több megadható kulcsszó-argumentumként, így több tollattribútum állítható be egy utasításban.

**Példák:**
```python
turtle.pen(fillcolor="black", pencolor="red", pensize=10)
sorted(turtle.pen().items())
penstate = turtle.pen()
```

---

## Szöveg kiírása

```python
turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
```

**Paraméterek:**
- `arg`: megjelenítendő szöveg
- `move`: `True` / `False`
- `align`: `"left"` / `"center"` / `"right"`
- `font`: tuple (betűtípus, betűméret, betűvastagság)

**Példák:**
```python
turtle.write("Home = ", True, align="center")
turtle.write((0, 0), True)
```

---

## Törlés

### Teljes visszaállítás

Törli a rajzot, a Turtle visszakerül a kiindulási pozícióba, és az alapértelmezett értékek kerülnek beállításra.

```python
turtle.reset()
```

### Csak rajz törlése

Csak a rajzot törli, egyéb beállításokat nem módosít.

```python
turtle.clear()
```
