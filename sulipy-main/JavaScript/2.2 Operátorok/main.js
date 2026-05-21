// 2.8 Alapvető operátorok, matematika!
let x = 10;
let y = 4;
console.log(x + y); // Összeadás: 14
console.log(x - y); // Kivonás: 6
console.log(x * y); // Szorzás: 40
console.log(x / y); // Osztás: 2.5

// 2.9 Összehasonlítások
console.log(10 > 5);   // Igaz (true)
console.log(10 === 5); // Hamis (false)
console.log(10 !== 5); // Igaz (true)

// 2.10 Feltételes elágazások: if, '?'
let pontszam = 60;
if (pontszam >= 50) {
    console.log("Sikeres vizsga!");
} else {
    console.log("Sikertelen vizsga.");
}

// Háromágú operátor (rövidített if)
let eredmeny = (pontszam >= 50) ? "Átment" : "Meghasalt";

// 2.11 Logikai operátorok
let regisztralt = true;
let belepett = false;
console.log(regisztralt && belepett); 
console.log(regisztralt || belepett);

// 2.12 Null-összefogó operátor '??'
let nev;
let aktualisFelhasznalo = nev ?? "Vendég";
console.log(aktualisFelhasznalo); // "Vendég"