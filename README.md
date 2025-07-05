# Kunskapskontroll 1: Test, loggning och schedulering

## 📌 Projektbeskrivning

Detta projekt är en del av kursen *Data Science* och syftar till att bygga ett automatiserat dataflöde med Python och schemaläggning. Programmet hämtar data, bearbetar den och uppdaterar en SQLite-databas automatiskt vid en förutbestämd tid.

---

## 🧱 Funktioner

- Läser in data från en CSV-fil.
- Bearbetar data (t.ex. datumformat eller datatyper)
- Uppdaterar en tabell i en SQLite-databas
- Loggar fel i en separat loggfil
- Har separata tester för huvudflödet
- Körs automatiskt via schemaläggning

---

## 📂 Filstruktur

📁 projektmapp/
├── hotel_bookings.csv Rådata som CSV
├── hotel_bookings.db# SQLite-databas
├── hotel_bookings.log # Loggfil för fel
├── uppgiften.py # Huvudflödet: läsning, bearbetning, uppdatering
└── README.md # Denna fil
