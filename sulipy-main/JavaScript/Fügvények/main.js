// --- 2.15 Functions (Sima függvények declaration) ---
function koszont(nev) {
    return `Szia ${nev}! Jó tanulást a Sulipy-vel! 👋`;
}

let uzenet = koszont("Peti");
console.log(uzenet);

// --- 2.16 Function expressions (Függvény kifejezések) ---
const osszead = function(a, b) {
    return a + b;
};

let matek = osszead(10, 20);
console.log(`Az összeg: ${matek}`);

// --- 2.17 Arrow functions, the basics (Nyíl függvények, az alapok) ---
const negyzet = (szam) => {
    return szam * szam;
};

const duplaz = szam => szam * 2;

console.log(negyzet(4)); // 16
console.log(duplaz(5));  // 10