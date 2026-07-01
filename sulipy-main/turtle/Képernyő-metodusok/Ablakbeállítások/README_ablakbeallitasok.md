# Ablakbeállítások

## Ablak mérete, pozíciója

```python
turtle.setup(width=_CFG["width"], height=_CFG["height"],
             startx=_CFG["leftright"], starty=_CFG["topbottom"])
```

> Az alapértelmezett értékek a konfigurációs könyvtárban vannak tárolva, és a `turtle.cfg` fájlban módosíthatóak.

**Paraméterek:**
- `width`: ha egész szám, akkor pixelben; ha tizedes tört, akkor a képernyőméret százalékában határozza meg az ablak szélességét — alapértelmezett: képernyő 50%-a
- `height`: ha egész szám, akkor pixelben; ha tizedes tört, akkor a képernyőméret százalékában határozza meg az ablak magasságát — alapértelmezett: képernyő 75%-a
- `startx`: ha pozitív szám, akkor a képernyő bal szélétől; ha negatív szám, akkor a képernyő jobb szélétől pixelben határozza meg az ablak pozícióját; ha `None`, akkor vízszintesen középen helyezkedik el
- `starty`: ha pozitív szám, akkor a képernyő tetejétől; ha negatív szám, akkor a képernyő aljától pixelben határozza meg az ablak pozícióját; ha `None`, akkor függőlegesen középen helyezkedik el

**Példák:**
```python
# 200 x 200 pixel méretű ablak, pozíciója a képernyő bal felső sarka
# screen objektum létrehozásával:
screen = turtle.Screen()
screen.setup(width=200, height=200, startx=0, starty=0)

# de így is működik:
turtle.setup(width=200, height=200, startx=0, starty=0)

# szélessége a képernyőméret 75%-a, magassága 50%-a, középre igazított
turtle.setup(width=.75, height=0.5, startx=None, starty=None)
```

---

## Bejárható terület beállítása

```python
turtle.screensize(canvwidth=None, canvheight=None, bg=None)
```

**Paraméterek:**
- `canvwidth` (szélesség): pozitív egész, szélesség pixelben
- `canvheight` (magasság): pozitív egész, magasság pixelben
- `bg` (háttérszín): szín-sztring vagy RGB tuple
- nincs argumentum: az aktuális értékkel tér vissza

> A teknős által bejárható terület nagyságát határozza meg, **DE** az ablakméret változatlan marad — az ablakméreten túli területek csak görgetéssel válnak láthatóvá!

---

## Ablakcím

```python
turtle.title(titlestring)
```

**Paraméterek:**
- `titlestring`: az ablak címsorában megjelenítésre kerülő szöveg

---

## Háttérszín

```python
turtle.bgcolor(*args)
```

**Paraméterek:**
- `args`: szín-sztring vagy 3 RGB szám vagy RGB-tuple
- nincs argumentum: az aktuális értékkel tér vissza

---

## Háttérkép

```python
turtle.bgpic(picname=None)
```

**Paraméterek:**
- `picname`: a gif fájl neve, vagy `"nopic"` — törli a háttérképet, vagy `None` — a fájl nevével tér vissza
- nincs argumentum: az aktuális értékkel tér vissza

---

## Ablak alaphelyzetbe állítása

```python
turtle.clear()
turtle.clearscreen()
```

Töröl minden rajzot és Turtle-t a képernyőről. Visszaállítja az ablak kiindulási értékeit: fehér háttér, nincs háttérkép, nincs esemény regisztrálva.

---

## Turtle alaphelyzetbe állítása

```python
turtle.reset()
turtle.resetscreen()
```

Minden Turtle-t alaphelyzetbe állít.

---

## Ablak bezárása

```python
turtle.bye()
```

Bezárja az ablakot.
