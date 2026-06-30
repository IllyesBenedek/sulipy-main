# Turtle-események

## Egérgomb lenyomása

```python
turtle.onclick(fun, btn=1, add=None)
```

**Paraméterek:**
- `fun`: két paraméterrel rendelkező függvény, amely akkor kerül hívásra, ha a megadott koordinátájú pontra klikkelünk az egérrel
- `btn`: az egérgomb száma, alapértelmezett érték az 1 (bal egérgomb)
- `add`: `True` vagy `False` – ha `True`, új esemény kerül hozzárendelésre, különben felváltja a korábbi hozzárendelést

**Példa:**
```python
def turn(x, y):
    left(180)

onclick(turn)  # A pontra kattintva megfordul a teknőc
onclick(None)  # Az esemény hozzárendelése törlődik
```

---

## Egérgomb felengedése

```python
turtle.onrelease(fun, btn=1, add=None)
```

**Paraméterek:**
- `fun`: két paraméterrel rendelkező függvény, amely akkor kerül hívásra, ha a megadott koordinátájú pontra klikkelünk az egérrel
- `btn`: az egérgomb száma, alapértelmezett érték az 1 (bal egérgomb)
- `add`: `True` vagy `False` – ha `True`, új esemény kerül hozzárendelésre, különben felváltja a korábbi hozzárendelést

**Példa:**
```python
class MyTurtle(Turtle):
    def glow(self, x, y):
        self.fillcolor("red")
    def unglow(self, x, y):
        self.fillcolor("")

turtle = MyTurtle()
turtle.onclick(turtle.glow)     # az egérgomb lenyomásának hatására a kitöltőszín piros lesz
turtle.onrelease(turtle.unglow) # felengedéskor átlátszó
```

---

## Teknős "vonszolása"

```python
turtle.ondrag(fun, btn=1, add=None)
```

**Paraméterek:**
- `fun`: két paraméterrel rendelkező függvény, amely akkor kerül hívásra, ha a megadott koordinátájú pontra klikkelünk az egérrel
- `btn`: az egérgomb száma, alapértelmezett érték az 1 (bal egérgomb)
- `add`: `True` vagy `False` – ha `True`, új esemény kerül hozzárendelésre, különben felváltja a korábbi hozzárendelést

> **Megjegyzés:** A teknős minden egérmozgatási eseménysorozatát megelőzi egy egérkattintásos esemény az adott teknősön.

**Példa:**
```python
turtle.ondrag(turtle.goto)
```

A teknősre kattintva, majd annak húzásával áthelyezheti a képernyőn, ezáltal kézzel rajzolva (ha a toll le van nyomva).
