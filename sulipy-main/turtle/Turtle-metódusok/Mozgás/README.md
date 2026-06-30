# Turtle - mozgás

## Mozgás előre

Mozgás előre (a Turtle állásának megfelelően) megadott értékkel.

```python
turtle.forward(distance)
turtle.fd(distance)
```

**Paraméterek:**
- `distance` (távolság): szám (int vagy float típus)

---

## Mozgás hátra

Mozgás hátra (a Turtle állásához képest) meghatározott értékkel.

```python
turtle.back(distance)
turtle.bk(distance)
turtle.backward(distance)
```

**Paraméterek:**
- `distance` (távolság): szám (int vagy float típus)

---

## Fordulás jobbra

Fordulás jobbra (a Turtle állásához képest) megadott értékkel.

```python
turtle.right(angle)
turtle.rt(angle)
```

**Paraméterek:**
- `angle` (szög): szám (int vagy float típus). Az érték megadható szögben vagy radiánban.

---

## Fordulás balra

Fordulás balra (a Turtle állásához képest) meghatározott értékkel.

```python
turtle.left(angle)
turtle.lt(angle)
```

**Paraméterek:**
- `angle` (szög): szám (int vagy float típus). Az érték megadható szögben vagy radiánban.

---

## Haladás megadott pozícióig

Haladás a megadott pozícióig az aktuális helyről.

```python
turtle.goto(x, y=None)
turtle.setpos(x, y=None)
turtle.setposition(x, y=None)
```

**Paraméterek:**
- `x`: szám / számpár / vektor
- `y`: szám / None

Ha a toll leengedett állapotban van, rajzol. Nem változtatja meg a Turtle orientációját.

**Példák:**
```python
turtle.setpos(60, 30)
turtle.setpos((20, 80))
```

---

## Koordináta felülírása

Adott koordináta felülírása a másik változatlanul hagyása mellett.

```python
turtle.setx(szam)
turtle.sety(szam)
```

**Paraméterek:**
- `szam`: szám (int vagy float típus)

---

## Orientáció megadása

Turtle orientációjának megadása.

```python
turtle.setheading(to_angle)
turtle.seth(to_angle)
```

**Paraméterek:**
- `to_angle` (szöghöz): szám (int vagy float típus)

Pl: 0 - kelet, 90 - észak, 180 - nyugat, 270 - dél

---

## Kezdőpozícióba állítás

Turtle kezdőpozícióba (0;0) koordinátájú pontba, kezdő orientációba állítása.

```python
turtle.home()
```

---

## Akció visszavonása

Megadott számú utolsó Turtle akció visszavonása.

```python
turtle.undo()
```

A visszavonható akciók száma a tároló méretétől függ.

---

## Sebesség megadása

Turtle sebességének megadása.

```python
turtle.speed(speed=None)
```

**Paraméterek:**
- `speed` (sebesség): 0 és 10 közötti szám
