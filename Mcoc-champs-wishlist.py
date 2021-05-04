champList = ["Storm", "Juggernaut", "Hulk", "Thor", "Rhino", "Hawkeye", "Drax", "Abomination",
             "Kang the Conqueror", "Superior Iron Man", "Rocket", "Doctor Strange", "Cap America(WII)",
             "Black Widow", "Void", "Sentry", "Luke Cage", "Groot", "Miles Morales", "Cyclops", "Old Balls",
             "Venompool", "She-Hulk", "Wolverine X-23", "Ms.Marvel", "Agent Venom", "Red Hulk", "Crossbones",
             "Black Panter(CW)", "Falcon", "Civil Warrior", "Nightcrawler", "Iron Fist(Immortal)", "Loki",
             "Gambit", "Karnak", "Rogue", "Quake", "Ultron", "Phoenix", "Ghost Rider", "Mordo", "Doctor Voodoo",
             "Hyperion", "Howard the Duck", "Gwenpool", "Cable", "The Hood", "Iceman", "Dormammu", "Archangel",
             "Starky Spidey", "Vulture", "Nebula", "Angela", "Carnage", "King Groot", "Medusa", "Morningstar",
             "M.O.D.O.K.", "Mephisto", "Psylocke", "Kingpin", "Hela", "Thor Rags", "Hulk Rags", "Sabretooth",
             "Doc Ock", "Bishop", "Taskmaster", "Yondu", "Cap Beardo", "Green Goblin", "Yellow Jacket",
             "Ant-Man", "Domino", "Deadpool", "Colossus", "Wolverine", "Magneto", "Deadpool", "Goldpool",
             "Magik", "Blade", "Winter Soldier", "Black Panter OG", "Punisher", "Daredevil", "Moon Knight",
             "Elektra", "Wasp", "Cap America", "Electro", "Joe Fixit", "Spider-Gwen", "Killmonger",
             "Black Bolt", "Gamora", "Ronan", "Thanos", "Symbiote Spidey", "Iron Fist", "Guillotine",
             "Thor Jane", "Iron Man", "Vision", "Star-Lord", "Ultron", "Hulkbuster", "Iron Patriot",
             "War Machine", "Ghost", "Sentinel", "Masacre", "IMIW", "Corvus Glaive", "Proxima Midnight",
             "Wolverine Weapon X", "Heimdall", "Korg", "Red Skull", "Omega Red", "Venom the Duck",
             "Symbiote Supreme", "Aegon", "Champion", "Darkhawk", "Night Thrasher", "Thing", "Diablo",
             "CMM", "Cap Marvel", "Venom", "Ronin", "Cull Obsidian", "Ebony Maw", "Human Torch",
             "Annihilus", "Nick Fury", "Havok", "Mister Sinister", "Punisher 2099", "Invisible Woman",
             "Namor", "Mysterio", "Stealthy Spidey", "Spiderman", "Sunspot", "Warlock", "Vision (Aarkus",
             "Emma Frost", "Beast", "Black Widow Claire Voyant", "Doctor Doom", "Elsa Bloodstone",
             "Man-Thing", "Mister Fantastic", "Guillotine 2099", "Silver Surfer", "Squirrel Girl",
             "Nova", "Longshot", "Mojo", "Mole Man", "Terrax", "Storm (Pyramid X)", "Sorcerer Supreme",
             "Red Guardian", "Black Widow Deadly Origin", "Tigra", "Hit-Monkey", "Guardian", "Sasquatch",
             "Dragon Man", "Air-Walker", "White Mags", "Professor X", "Apocalypse", "Cosmic Ghost Rider",
             "Red Goblin", "Immortal Hulk", "Immortal Abomination", "DDHK", "Scarlet Witch", "Spider-Ham",
             "Jubilee", "Stryfe", "Psycho-Man", "Super-Skrull", "Mangog", "Odin", "Jabari Panter", "Sivler Centurion"]


fiveStarBestPull = ["Red Hulk", "Crossbones", "Quake", "Ghost Rider", "Hyperion", "Iceman", "Dormammu", "Archangel",
                    "Starky Spidey", "Vulture", "Angela", "Medusa", "Kingpin", "Hulk Rags", "Magneto", "Magik", "Blade",
                    "Black Panter OG", "Killmonger", "Star-Lord", "Corvus Glaive", "Wolverine Weapon X", "Omega Red",
                    "Venom the Duck", "Venom", "Human Torch", "Nick Fury", "Havok", "Namor", "Stealthy Spidey", "Warlock",
                    "Emma Frost", "Black Widow Claire Voyant", "Guillotine 2099", "Silver Surfer", "Sorcerer Supreme",
                    "Black Widow Deadly Origin", "Tigra", "Hit-Monkey", "Guardian", "Professor X", "Apocalypse",
                    "Cosmic Ghost Rider", "Scarlet Witch", "Spider-Ham", "Stryfe", "Odin", "Jabari Panter", "Sivler Centurion"]

sixStarBestPull = ["Void", "Luke Cage", "She-Hulk", "Red Hulk", "Crossbones", "Falcon", "Howard the Duck", "Iceman", "Archangel",
                   "Vulture", "Angela", "Morningstar", "Kingpin", "Hela", "Hulk Rags", "Sabretooth", "Cap Beardo", "Colossus",
                   "Wolverine", "Magneto", "Black Panter OG", "Killmonger", "Star-Lord", "Ghost", "Corvus Glaive", "Proxima Midnight",
                   "Wolverine Weapon X", "Omega Red", "Venom the Duck", "Symbiote Supreme", "Aegon", "Thing", "CMM", "Venom",
                   "Cull Obsidian", "Human Torch", "Nick Fury", "Havok", "Namor", "Stealthy Spidey", "Sunspot", "Warlock",
                   "Emma Frost", "Black Widow Claire Voyant", "Doctor Doom", "Elsa Bloodstone", "Mister Fantastic", "Guillotine 2099",
                   "Silver Surfer", "Mojo", "Mole Man", "Terrax", "Sorcerer Supreme", "Red Guardian", "Black Widow Deadly Origin",
                   "Tigra", "Hit-Monkey", "Guardian", "Sasquatch", "Dragon Man", "Professor X", "Apocalypse", "Cosmic Ghost Rider",
                   "Immortal Hulk", "Immortal Abomination", "DDHK", "Scarlet Witch", "Spider-Ham", "Stryfe", "Odin", "Jabari Panter",
                   "Sivler Centurion"]

starLevel = input("What star level are you spinning? ")
champLandedOn = input("Which champion did you land on? ")

if starLevel == "5":
    if champLandedOn in champList:
        if(champLandedOn in fiveStarBestPull):
            print("Great pull Congrats!")
        else:
            print("Darn better luck next time!")

if starLevel == "6":
    if champLandedOn in champList:
        if(champLandedOn in sixStarBestPull):
            print("Great pull Congrats!")
        else:
            print("Darn better luck next time!")
