# Kitöltés

## Kitöltés állapota

Megadja, hogy éppen kitöltés van-e folyamatban.

```python
turtle.filling()
```

`True` értékkel tér vissza kitöltés esetén, egyébként `False`.

---

## Kitöltés kezdése és befejezése

```python
turtle.begin_fill()
turtle.end_fill()
```

> A `begin_fill()` és `end_fill()` közé rajzolt alakzat kitöltődik a beállított kitöltőszínnel.

**Példa:**
```python
turtle.color("black", "red")  # vonalszín fekete, kitöltőszín piros
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
```
