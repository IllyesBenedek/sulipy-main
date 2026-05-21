"use strict"; // 2.3 The modern mode, "use strict"

// 2.1 Hello, Wilág!
console.log("Hello Word!");

// 2.2 Kódszerkezet
console.log("Hello");
console.log("Word!");

// 2.4 Változók
let uzenet = "Szia!";
console.log(uzenet);

uzenet = "Módosított üzenet";
console.log(uzenet);

const PI = 3.1415;
console.log(PI);

let elso = "Alma";
let masodik;
masodik = elso;
console.log(masodik);

// 2.5 Adattípusok
let szam = 42;
let szoveg = "JavaScript";
let logikai = true;
let ures = null;
let nincsMegadva = undefined;

console.log(typeof szam);
console.log(typeof szoveg);

// 2.6 Interakció: alert, prompt, confirm
alert("Üdvözöllek az oldalon!");
let nev = prompt("Hogy hívnak?", "Vendég");
console.log(nev);
let jovahagyas = confirm("Elfogadod a feltételeket?");
console.log(jovahagyas);

// 2.7 Típuskonverziók (Adattípusok átalakítása)
let szovegesSzam = "100";
let igaziSzam = Number(szovegesSzam);
console.log(typeof igaziSzam);

let logikaiErtek = Boolean(1);
console.log(logikaiErtek);

let szovegErtek = String(false);
console.log(typeof szovegErtek);
