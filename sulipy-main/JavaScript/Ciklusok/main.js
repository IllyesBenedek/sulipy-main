// --- 2.13 Loops: while and for (Ciklusok) ---

// 1. Példa: Visszaszámlálás (While ciklus)
let visszaszamlalo = 5;
while (visszaszamlalo > 0) {
    console.log(`Kilövésig hátravan: ${visszaszamlalo} másodperc`);
    visszaszamlalo--; // Csökkentjük az értéket, hogy egyszer véget érjen
}
console.log("KILÖVÉS! ");

// 2. Példa: Jelszó ellenőrzés (While ciklus adatbekérésre)
let titkosJelszo = prompt("Kérlek, add meg a titkos jelszót!");
while (titkosJelszo !== "sulipy123") {
    titkosJelszo = prompt("Hibás jelszó! Próbáld újra:");
}
console.log("Sikeres belépés! ");

// 3. Példa: Életkor ellenőrzés (Do-while ciklus)
let eletkor;
do {
    eletkor = Number(prompt("Hány éves vagy? (Minimum 18 év kell a belépéshez)"));
} while (isNaN(eletkor) || eletkor < 18); 
console.log("Üdvözlünk a felnőtt tartalomnál!");

// 4. Példa: Páros számok kiírása (For ciklus)
for (let i = 0; i <= 10; i += 2) {
    console.log(`Páros szám: ${i}`);
}

// --- 2.14 The "switch" statement (A switch szerkezet) ---
let honap = "június";

switch (honap) {
    case "december":
    case "január":
    case "február":
        console.log("Tél van, hideg van. ❄");
        break; // Megállítja a futást, ha megvan a találat
        
    case "június":
    case "július":
    case "augusztus":
        console.log("Nyár van, irány a strand! ☀️");
        break;
        
    default:
        console.log("Ez egy átmeneti évszak (Tavasz vagy Ősz).");
}