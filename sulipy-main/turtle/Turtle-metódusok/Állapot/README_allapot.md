# Turtle állapotának lekérdezése és beállítása

## Pozíció

Turtle aktuális pozíciójának lekérdezése.

```python
turtle.position()
turtle.pos()
```

---

## Koordináta

Turtle aktuális X vagy Y koordinátájának lekérdezése.

```python
turtle.xcor()
turtle.ycor()
```

---

## Orientáció

Turtle aktuális iránya (szögben).

```python
turtle.heading()
```

---

## Távolság

Távolság adott ponttól vagy egy másik Turtle-től.

```python
turtle.distance(x, y=None)
```

---

## Turtle láthatósága

Megadja, hogy a Turtle látható-e.

```python
turtle.isvisible()
```

---

## Turtle elrejtése

Turtle elrejtése a képernyőn.

```python
turtle.hideturtle()
turtle.ht()
```

---

## Turtle megjelenítése

Turtle megjelenítése a képernyőn.

```python
turtle.showturtle()
turtle.st()
```

---

## Turtle-alak

Turtle alakjának beállítása.

```python
turtle.shape(name=None)
```

**Lehetséges értékek:**
- `"arrow"` - nyíl
- `"turtle"` - teknős
- `"circle"` - kör
- `"square"` - négyzet
- `"triangle"` - háromszög
- `"classic"` - klasszikus

---

## Turtle-méret

### Átméretezési mód

```python
turtle.resizemode(rmode=None)
```

**Lehetséges értékek:**
- `"auto"` - tollmérettől függő
- `"user"` - nyújtási faktortól és körvonal szélességtől függő
- `"noresize"` - nem alkalmazkodik

### Méret beállítása

```python
turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
turtle.turtlesize(stretch_wid=None, stretch_len=None, outline=None)
```

**Paraméterek:**
- `stretch_wid` - nyújtási szélesség
- `stretch_len` - nyújtási hosszúság
- `outline` - körvonal vastagsága

Ha egyik paraméter sincs megadva, a függvény visszaadja az aktuális értékeket. Ha meg vannak adva, beállítja azokat.
