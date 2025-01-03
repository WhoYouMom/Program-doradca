print("Witaj w doradcy gier ! Pomozemy ci dobrac gre do twoich preferencji\n")

# Baza gier
gry = {
    "FIFA 24 (EA Sports FC 24)": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "łatwa",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "NBA 2K24": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "łatwa",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Madden NFL 24": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "PGA Tour 2K23": {
        "kategoria": "sportowa",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "MLB The Show 23": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "NHL 24": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Tony Hawk’s Pro Skater 1+2": {
        "kategoria": "sportowa",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Riders Republic": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "WWE 2K23": {
        "kategoria": "sportowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "The Witcher 3: Wild Hunt": {
        "kategoria": "fabularna",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Red Dead Redemption 2": {
        "kategoria": "fabularna",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Baldur’s Gate 3": {
        "kategoria": "rpg",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Cyberpunk 2077": {
        "kategoria": "fabularna",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Mass Effect Legendary Edition": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Horizon Forbidden West": {
        "kategoria": "fabularna",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Dragon Age: Inquisition": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Starfield": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Elder Scrolls V: Skyrim": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Divinity: Original Sin 2": {
        "kategoria": "rpg",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Forest": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "DayZ": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Rust": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "7 Days to Die": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Ark: Survival Evolved": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Subnautica": {
        "kategoria": "survivalowa",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Valheim": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "nie",
    },
    "Don't Starve Together": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "nie",
    },
    "Green Hell": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Minecraft": {
        "kategoria": "survivalowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "łatwa",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "nie",
    },
    "Resident Evil 4 Remake": {
        "kategoria": "horror",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Silent Hill 2": {
        "kategoria": "horror",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Outlast Trials": {
        "kategoria": "horror",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Dead Space": {
        "kategoria": "horror",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Amnesia: The Bunker": {
        "kategoria": "horror",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Layers of Fear": {
        "kategoria": "horror",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Phasmophobia": {
        "kategoria": "horror",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "SOMA": {
        "kategoria": "horror",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Dark Pictures Anthology": {
        "kategoria": "horror",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Devour": {
        "kategoria": "horror",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Microsoft Flight Simulator": {
        "kategoria": "symulator",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Farming Simulator 22": {
        "kategoria": "symulator",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Euro Truck Simulator 2": {
        "kategoria": "symulator",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Train Sim World 4": {
        "kategoria": "symulator",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Sims 4": {
        "kategoria": "symulator",
        "ile_osob": "jednoosobowe",
        "trudnosc": "łatwa",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "BeamNG.drive": {
        "kategoria": "symulator",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Car Mechanic Simulator 2021": {
        "kategoria": "symulator",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Bus Simulator 21": {
        "kategoria": "symulator",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Cities: Skylines II": {
        "kategoria": "strategiczne",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Construction Simulator": {
        "kategoria": "symulator",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Forza Horizon 5": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "łatwa",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Gran Turismo 7": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Assetto Corsa Competizione": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Project CARS 2": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Need for Speed Unbound": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "F1 23": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Dirt Rally 2.0": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "The Crew Motorfest": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Wreckfest": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "TrackMania": {
        "kategoria": "wyścigowa",
        "ile_osob": "wieloosobowe",
        "trudnosc": "łatwa",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Call of Duty: Modern Warfare III": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Counter-Strike 2": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Battlefield 2042": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Rainbow Six Siege": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Escape from Tarkov": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Apex Legends": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Overwatch 2": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "DOOM Eternal": {
        "kategoria": "strzelanka",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Destiny 2": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Halo Infinite": {
        "kategoria": "strzelanka",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Red Dead Redemption 2": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Assassin’s Creed Mirage": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Last of Us Part II": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Cyberpunk 2077: Phantom Liberty": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Horizon Forbidden West": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Ghost of Tsushima": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Marvel’s Spider-Man 2": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Uncharted 4: A Thief’s End": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Sekiro: Shadows Die Twice": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "God of War Ragnarök": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Witcher 3: Wild Hunt": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Baldur’s Gate 3": {
        "kategoria": "rpg",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Elden Ring": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Cyberpunk 2077": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Starfield": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Divinity: Original Sin 2": {
        "kategoria": "rpg",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Dragon Age: Inquisition": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Mass Effect Legendary Edition": {
        "kategoria": "rpg",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Diablo IV": {
        "kategoria": "rpg",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Path of Exile": {
        "kategoria": "rpg",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "The Legend of Zelda: Tears of the Kingdom": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Life is Strange: True Colors": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "łatwa",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Uncharted: The Lost Legacy": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Firewatch": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "łatwa",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Journey": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "łatwa",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Tomb Raider (2013)": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Detroit: Become Human": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "What Remains of Edith Finch": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "łatwa",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Gris": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "łatwa",
        "fabula": "tak",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "A Plague Tale: Requiem": {
        "kategoria": "przygodowe",
        "ile_osob": "jednoosobowe",
        "trudnosc": "średnia",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Civilization VI": {
        "kategoria": "strategiczne",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Total War: Warhammer III": {
        "kategoria": "strategiczne",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "tak",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Age of Empires IV": {
        "kategoria": "strategiczne",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Stellaris": {
        "kategoria": "strategiczne",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Crusader Kings III": {
        "kategoria": "strategiczne",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Company of Heroes 3": {
        "kategoria": "strategiczne",
        "ile_osob": "wieloosobowe",
        "trudnosc": "średnia",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "XCOM 2": {
        "kategoria": "strategiczne",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "szybka akcja",
        "grafika": "tak",
    },
    "Frostpunk": {
        "kategoria": "strategiczne",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Anno 1800": {
        "kategoria": "strategiczne",
        "ile_osob": "wieloosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    },
    "Hearts of Iron IV": {
        "kategoria": "strategiczne",
        "ile_osob": "jednoosobowe",
        "trudnosc": "trudna",
        "fabula": "nie",
        "eksploracja": "eksplorować świat",
        "grafika": "tak",
    }
}

# Kategorie
kategorie = [
    "sportowa", "fabularna", "survivalowa", "horror", "symulator",
    "wyscigowa", "strzelanka", "akcja", "rpg", "przygodowe", "strategiczne"
]

# Pytanka
def wybierz_gre():
    kategoria = input(f"Jaka kategoria gry Cię interesuje z podanych: {', '.join(kategorie)}?\n")
    if kategoria not in kategorie:
        print("Nie ma takiej kategorii. Spróbuj jeszcze raz.")
        return

    ile_osob = input("Wolisz gry jednoosobowe, czy wieloosobowe?\n").strip().lower()
    if ile_osob not in ["jednoosobowe", "wieloosobowe"]:
        print("Źle wpisałeś odpowiedź. Spróbuj jeszcze raz.")
        return

    trudnosc = input("Wolisz gry trudne, średnie czy łatwe?(trudna/średnia/łatwa)\n").strip().lower()
    if trudnosc not in ["trudna", "średnia", "łatwa"]:
        print("Źle wpisałeś odpowiedź. Spróbuj jeszcze raz.")
        return

    fabula = input("Czy gra ma mieć głęboką fabułę? (tak/nie)\n").strip().lower()
    if fabula not in ["tak", "nie"]:
        print("Źle wpisałeś odpowiedź. Spróbuj jeszcze raz.")
        return

    eksploracja = input("Wolisz eksplorować świat, czy szybką akcję? (eksplorować świat/szybka akcja)\n").strip().lower()
    if eksploracja not in ["eksplorować świat", "szybka akcja"]:
        print("Źle wpisałeś odpowiedź. Spróbuj jeszcze raz.")
        return

    grafika = input("Czy zależy Ci na dopracowanej grafice? (tak/nie)\n").strip().lower()
    if grafika not in ["tak", "nie"]:
        print("Źle wpisałeś odpowiedź. Spróbuj jeszcze raz.")
        return
    # Szukanie gier
    print("\nTwoje wyniki:")
    znaleziono = False
    for gra, dane in gry.items():
        if (
            dane["kategoria"] == kategoria and
            dane["ile_osob"] == ile_osob and
            dane["trudnosc"] == trudnosc and
            dane["fabula"] == fabula and
            dane["eksploracja"] == eksploracja and
            dane["grafika"] == grafika
        ):
            print(f"- {gra}")
            znaleziono = True
    if not znaleziono:
        print("Niestety, nie znaleziono gry spełniającej Twoje kryteria.")
# Wywołanie funkcji
wybierz_gre()