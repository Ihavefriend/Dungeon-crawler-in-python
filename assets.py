"""                                                                 ITEMS                                                                                                                     """
items = {
    "Iron Sword": {"CLASS": "weapon", "STATS": {"ATK": 3, "DEF": 1}, "DISC": "A battle-worn iron sword dropped by the goblins"},
    "Healing Potion": {"CLASS": "potion", "STATS": {"HP": 10}, "DISC": "A mixture of various healing herbs, it tastes very bitter"},
    "Magic Potion": {"CLASS": "potion", "STATS": {"MP": 10}, "DISC": "Restores magical energy with a refreshing taste"},
    "Iron Shield": {"CLASS": "armor", "STATS": {"DEF": 1}, "DISC": "A sturdy shield made of iron, providing basic protection"},
    "Cheese": {"CLASS": "potion", "STATS": {"HP": 20}, "DISC": "A block of cheese? Where did this come from"},
    "Battle Axe": {"CLASS": "weapon", "STATS": {"ATK": 8}, "DISC": "A heavy axe with a sharp blade, often used by orcs"},
    "Bone Armor": {"CLASS": "armor", "STATS": {"DEF": 5}, "DISC": "An armor crafted from bones, offering solid protection"},
    "Troll Club": {"CLASS": "weapon", "STATS": {"ATK": 12}, "DISC": "A large club made from the bones of fallen enemies"},
    "Vampire Fang": {"CLASS": "weapon", "STATS": {"ATK": 6}, "DISC": "A fang from a vampire, sharp and dangerous"},
    "Bloodstone": {"CLASS": "potion", "STATS": {"MP": 50}, "DISC": "A magical stone used by vampires to enhance their powers"},
    "Health Potion": {"CLASS": "potion", "STATS": {"HP": 50}, "DISC": "A potent potion that heals a large amount of health"},
    "Large Healing Potion": {"CLASS": "potion", "STATS": {"HP": 100}, "DISC": "A larger version of the healing potion, restoring more health. This tastes like cherry!"},
    "Elf Bow": {"CLASS": "weapon", "STATS": {"ATK": 7}, "DISC": "A finely crafted bow with intricate elven designs"},
    "Mana Potion": {"CLASS": "potion", "STATS": {"MP": 25}, "DISC": "Restores a moderate amount of magical energy"},
    "Cursed Sword": {"CLASS": "weapon", "STATS": {"ATK": 15, "DEF": -3}, "DISC": "A sword imbued with a dark curse. Use it wisely."},
    "Dark Amulet": {"CLASS": "accessory", "STATS": {"MP": 20, "DEF": 5}, "DISC": "An amulet radiating an eerie energy"},
    "Silver Claw": {"CLASS": "weapon", "STATS": {"ATK": 10}, "DISC": "A claw made of silver, effective against dark creatures"},
    "Beast Hide": {"CLASS": "armor", "STATS": {"DEF": 8}, "DISC": "Durable hide from a werewolf, providing great defense"},
    "Rusty Shield": {"CLASS": "armor", "STATS": {"DEF": 3}, "DISC": "An old shield, not very reliable but better than nothing"},
    "Ancient Helmet": {"CLASS": "armor", "STATS": {"DEF": 10}, "DISC": "A helmet worn by knights of old, offering great protection"},
    "Scale Blade": {"CLASS": "weapon", "STATS": {"ATK": 14}, "DISC": "A sharp blade crafted from lizardman scales"},
    "Dragon Scale": {"CLASS": "armor", "STATS": {"DEF": 12}, "DISC": "A scale from a dragon, radiating immense power"},
    "Spirit Orb": {"CLASS": "accessory", "STATS": {"MP": 30}, "DISC": "A glowing orb filled with the essence of a forest spirit"},
    "Mystic Herb": {"CLASS": "potion", "STATS": {"HP": 40}, "DISC": "A rare herb that restores health when consumed"},
    "Hydra Fang": {"CLASS": "weapon", "STATS": {"ATK": 18}, "DISC": "A sharp fang from a hydra, imbued with poison"},
    "Poison Vial": {"CLASS": "potion", "STATS": {"ATK": 5}, "DISC": "A vial filled with deadly poison. Handle with care."},
    "Shadow Dagger": {"CLASS": "weapon", "STATS": {"ATK": 12}, "DISC": "A small, dark dagger favored by assassins"},
    "Invisibility Cloak": {"CLASS": "accessory", "STATS": {"DEF": 10}, "DISC": "A cloak that makes the wearer hard to detect"},
    "Frost Gem": {"CLASS": "accessory", "STATS": {"MP": 40}, "DISC": "A cold gem that boosts magical powers"},
    "Icy Scales": {"CLASS": "armor", "STATS": {"DEF": 15}, "DISC": "Scales from a frost wyrm, radiating an icy chill"},
    "Demonic Staff": {"CLASS": "weapon", "STATS": {"ATK": 20, "MP": 30}, "DISC": "A staff imbued with demonic power, perfect for mages"},
    "Dark Crystal": {"CLASS": "potion", "STATS": {"MP": 50}, "DISC": "A crystal filled with dark magical energy"},
    "Griffin Feather": {"CLASS": "accessory", "STATS": {"DEF": 12}, "DISC": "A feather that radiates the majesty of a griffin"},
    "Golden Beak": {"CLASS": "weapon", "STATS": {"ATK": 16}, "DISC": "A golden beak from a griffin, sharp and majestic"},
    "Stone Heart": {"CLASS": "accessory", "STATS": {"DEF": 20}, "DISC": "The core of an ancient golem, extremely durable"},
    "Titan Shard": {"CLASS": "weapon", "STATS": {"ATK": 25}, "DISC": "A shard from a golem's body, radiating immense strength"},
    "Dragon's Flame": {"CLASS": "potion", "STATS": {"MP": 60}, "DISC": "A rare flame from a dragon, used to empower spells"},
    "Void Blade": {"CLASS": "weapon", "STATS": {"ATK": 28}, "DISC": "A blade forged in the void, deadly and unbreakable"},
    "Soul Essence": {"CLASS": "accessory", "STATS": {"MP": 50}, "DISC": "A fragment of a soul, used to enhance magical abilities"},
    "Demonic Horn": {"CLASS": "weapon", "STATS": {"ATK": 30}, "DISC": "A sharp horn from an archdemon, filled with malice"},
    "Hellfire Crystal": {"CLASS": "potion", "STATS": {"MP": 70}, "DISC": "A crystal containing flames from the underworld"},
    "Phoenix Feather": {"CLASS": "potion", "STATS": {"HP": 150}, "DISC": "A rare feather that revives and heals the user"},
    "Flame Orb": {"CLASS": "accessory", "STATS": {"MP": 40, "ATK": 10}, "DISC": "An orb containing eternal flames"},
    "Abyssal Crown": {"CLASS": "accessory", "STATS": {"DEF": 25}, "DISC": "A crown worn by the Abyssal Lord, radiating dark energy"},
    "Dark Rune": {"CLASS": "accessory", "STATS": {"MP": 70}, "DISC": "A rune of dark origin, amplifying magical powers"},
    "Heavenly Armor": {"CLASS": "armor", "STATS": {"DEF": 35}, "DISC": "An armor blessed by celestial beings, offering unparalleled protection"},
    "Divine Crystal": {"CLASS": "potion", "STATS": {"MP": 100}, "DISC": "A crystal imbued with divine energy, restoring immense magical power"},
}

shop_inventory = {
    "Iron Sword": {"price": 10},
    "Healing Potion": {"price": 8},
    "Magic Potion": {"price": 12},
    "Iron Shield": {"price": 15},
    "Cheese": {"price": 5},
    "Battle Axe": {"price": 20},
    "Bone Armor": {"price": 25},
    "Large Healing Potion": {"price": 30},
    # Skill Books
    "Skill Book: Arrow Storm (Rouge)": {"price": 20, "skill": "Arrow Storm"},
    "Skill Book: Berserk (Knight)": {"price": 25, "skill": "Berserk"},
    "Skill Book: Heal (Mage)": {"price": 30, "skill": "Heal"},
    "Skill Book: Ember Strike (Knight)": {"price": 18, "skill": "Ember Strike"},
    "Skill Book: Frost Spear (Mage)": {"price": 22, "skill": "Frost Spear"},
    "Skill Book: Phantom Strike (Rouge)": {"price": 24, "skill": "Phantom Strike"},
    "Skill Book: Crushing Blow (Knight)": {"price": 26, "skill": "Crushing Blow"},
    "Skill Book: Earthen Lance (Mage)": {"price": 28, "skill": "Earthen Lance"},
    "Skill Book: Gales Edge (Rouge)": {"price": 30, "skill": "Gales Edge"},
    "Skill Book: Lighting Arc (Mage)": {"price": 32, "skill": "Lightning Arc"}
}
"""                                                           LOOT TABLES                                                                                                                     """

drops = {
    "Goblin": {"Iron Sword": 70, "Healing Potion": 30},
    "Giant Rat": {"Cheese": 60, "Iron Shield": 40},
    "Orc": {"Battle Axe": 50, "Magic Potion": 50},
    "Skeleton Warrior": {"Bone Armor": 75, "Health Potion": 25},
    "Troll": {"Troll Club": 80, "Large Healing Potion": 20},
    "Vampire": {"Vampire Fang": 60, "Bloodstone": 40},
    "Dark Elf Archer": {"Elf Bow": 70, "Mana Potion": 30},
    "Cursed Knight": {"Cursed Sword": 65, "Dark Amulet": 35},
    "Werewolf": {"Silver Claw": 55, "Beast Hide": 45},
    "Haunted Armor": {"Rusty Shield": 50, "Ancient Helmet": 50},
    "Lizardman Warrior": {"Scale Blade": 60, "Dragon Scale": 40},
    "Forest Spirit": {"Spirit Orb": 70, "Mystic Herb": 30},
    "Hydra": {"Hydra Fang": 50, "Poison Vial": 50},
    "Shadow Assassin": {"Shadow Dagger": 65, "Invisibility Cloak": 35},
    "Frost Wyrm": {"Frost Gem": 60, "Icy Scales": 40},
    "Demonic Mage": {"Demonic Staff": 55, "Dark Crystal": 45},
    "Griffin": {"Griffin Feather": 70, "Golden Beak": 30},
    "Ancient Golem": {"Stone Heart": 75, "Titan Shard": 25},
    "Dark Dragon": {"Dragon Scale": 60, "Dragon's Flame": 40},
    "Void Reaper": {"Void Blade": 55, "Soul Essence": 45},
    "Archdemon": {"Demonic Horn": 65, "Hellfire Crystal": 35},
    "Phoenix": {"Phoenix Feather": 50, "Flame Orb": 50},
    "Abyssal Lord": {"Abyssal Crown": 60, "Dark Rune": 40},
    "Celestial Guardian": {"Heavenly Armor": 70, "Divine Crystal": 30},
}
"""                                                                         FLOORS                                                                                 """
floors = {
    1: {
        "monsters": [
            {"name": "Goblin", "EXP": 50, "GOLD": (3, 6), "HP": 20, "ATK": 5, "DEF": 2},
            {"name": "Giant Rat", "EXP": 40, "GOLD": (2, 5), "HP": 15, "ATK": 2, "DEF": 1}
        ],
        "difficulty": "F"
    },
    2: {
        "monsters": [
            {"name": "Orc", "EXP": 60, "GOLD": (5, 10), "HP": 20, "ATK": 5, "DEF": 8},
            {"name": "Skeleton Warrior", "EXP": 100, "GOLD": (8, 15), "HP": 14, "ATK": 10, "DEF": 2}
        ],
        "difficulty": "E"
    },
    3: {
        "monsters": [
            {"name": "Troll", "EXP": 200, "GOLD": (15, 25), "HP": 30, "ATK": 12, "DEF": 5},
            {"name": "Vampire", "EXP": 300, "GOLD": (20, 35), "HP": 40, "ATK": 15, "DEF": 6}
        ],
        "difficulty": "D"
    },
    4: {
        "monsters": [
            {"name": "Dark Elf Archer", "EXP": 150, "GOLD": (10, 20), "HP": 25, "ATK": 18, "DEF": 4},
            {"name": "Cursed Knight", "EXP": 250, "GOLD": (15, 30), "HP": 30, "ATK": 20, "DEF": 10}
        ],
        "difficulty": "D+"
    },
    5: {
        "monsters": [
            {"name": "Werewolf", "EXP": 350, "GOLD": (25, 40), "HP": 50, "ATK": 25, "DEF": 12},
            {"name": "Haunted Armor", "EXP": 450, "GOLD": (30, 50), "HP": 40, "ATK": 20, "DEF": 20}
        ],
        "difficulty": "C"
    },
    6: {
        "monsters": [
            {"name": "Lizardman Warrior", "EXP": 400, "GOLD": (35, 55), "HP": 60, "ATK": 28, "DEF": 15},
            {"name": "Forest Spirit", "EXP": 500, "GOLD": (40, 60), "HP": 30, "ATK": 20, "DEF": 30}
        ],
        "difficulty": "C+"
    },
    7: {
        "monsters": [
            {"name": "Hydra", "EXP": 600, "GOLD": (50, 80), "HP": 80, "ATK": 35, "DEF": 20},
            {"name": "Shadow Assassin", "EXP": 700, "GOLD": (60, 90), "HP": 50, "ATK": 40, "DEF": 10}
        ],
        "difficulty": "B"
    },
    8: {
        "monsters": [
            {"name": "Frost Wyrm", "EXP": 750, "GOLD": (65, 100), "HP": 70, "ATK": 45, "DEF": 25},
            {"name": "Demonic Mage", "EXP": 850, "GOLD": (75, 110), "HP": 60, "ATK": 50, "DEF": 15}
        ],
        "difficulty": "B+"
    },
    9: {
        "monsters": [
            {"name": "Griffin", "EXP": 900, "GOLD": (80, 120), "HP": 100, "ATK": 50, "DEF": 30},
            {"name": "Ancient Golem", "EXP": 1000, "GOLD": (85, 130), "HP": 120, "ATK": 40, "DEF": 50}
        ],
        "difficulty": "A"
    },
    10: {
        "monsters": [
            {"name": "Dark Dragon", "EXP": 1500, "GOLD": (100, 150), "HP": 200, "ATK": 60, "DEF": 40},
            {"name": "Void Reaper", "EXP": 1800, "GOLD": (120, 180), "HP": 150, "ATK": 70, "DEF": 30}
        ],
        "difficulty": "A+"
    },
    11: {
        "monsters": [
            {"name": "Archdemon", "EXP": 2000, "GOLD": (150, 200), "HP": 250, "ATK": 80, "DEF": 50},
            {"name": "Phoenix", "EXP": 2200, "GOLD": (180, 230), "HP": 180, "ATK": 90, "DEF": 40}
        ],
        "difficulty": "S"
    },
    12: {
        "monsters": [
            {"name": "Abyssal Lord", "EXP": 3000, "GOLD": (200, 300), "HP": 300, "ATK": 100, "DEF": 60},
            {"name": "Celestial Guardian", "EXP": 3500, "GOLD": (250, 350), "HP": 250, "ATK": 110, "DEF": 50}
        ],
        "difficulty": "SS"
    }
}
"""                                                                                             SKILLS                                                                                                          """
skills = {
    "Slash": {
        "TYPE": "attack",
        "CLASS": "ROUGE",
        "POWER": 10,
        "MP_COST": 0,
        "DISC": "A Swift strike with your dagger.",
        "STAT_SCALING": {"ATK": 1.0},
    },
    "Basic Sword Art": {
        "TYPE": "attack",
        "CLASS": "KNIGHT",
        "POWER": 10,
        "MP_COST": 0,
        "DISC": "A basic sword Art.",
        "STAT_SCALING": {"ATK": 1.0},
    },
    "Fireball": {
        "TYPE": "attack",
        "CLASS": "MAGE",
        "POWER": 15,
        "MP_COST": 5,
        "DISC": "A fire spell that burns enemies.",
        "STAT_SCALING": {"ATK": 1.3},
    },
    "Heal": {
        "TYPE": "support",
        "CLASS": "MAGE",
        "POWER": 20,
        "MP_COST": 8,
        "DISC": "Heals the caster or an ally.",
        "STAT_SCALING": {"INT": 1},
    },
    "Arrow Storm": {
        "TYPE": "attack",
        "CLASS": "ROUGE",
        "POWER": 15,
        "MP_COST": 10,
        "DISC": "A powerful barrage of arrows.",
        "STAT_SCALING": {"ATK": 1.2},
    },
    "Berserk": {
        "TYPE": "attack",
        "CLASS": "KNIGHT",
        "POWER": 25,
        "MP_COST": 8,
        "DISC": "A powerful strike that costs not only mana, but also your sanity",
        "STAT_SCALING": {"ATK": 2},
    },
    "Hammer Smash": {
        "TYPE": "attack",
        "CLASS": "KNIGHT",
        "POWER": 30,
        "MP_COST": 15,
        "DISC": "A strong strike on the ground, it shakes up the enemies",
        "STAT_SCALING": {"ATK": 0.9},
    },
    "Ember Strike": {
        "TYPE": "attack",
        "CLASS": "KNIGHT",
        "POWER": 20,
        "MP_COST": 6,
        "DISC": "A fiery slash that scorches the enemy.",
        "STAT_SCALING": {"ATK": 1.5},
    },
    "Frost Spear": {
        "TYPE": "attack",
        "CLASS": "MAGE",
        "POWER": 25,
        "MP_COST": 7,
        "DISC": "A piercing spear of ice that freezes enemies.",
        "STAT_SCALING": {"INT": 1.6},
    },
    "Phantom Strike": {
        "TYPE": "attack",
        "CLASS": "ROUGE",
        "POWER": 22,
        "MP_COST": 8,
        "DISC": "A swift strike that leaves afterimages.",
        "STAT_SCALING": {"ATK": 1.8},
    },
    "Crushing Blow": {
        "TYPE": "attack",
        "CLASS": "KNIGHT",
        "POWER": 35,
        "MP_COST": 10,
        "DISC": "A heavy downwards slash that can cut through stone.",
        "STAT_SCALING": {"ATK": 2.0},
    },
    "Earthen Lance": {
        "TYPE": "attack",
        "CLASS": "MAGE",
        "POWER": 28,
        "MP_COST": 9,
        "DISC": "A lance of earth that pierces through enemies.",
        "STAT_SCALING": {"INT": 1.7},
    },
    "Gales Edge": {
        "TYPE": "attack",
        "CLASS": "ROUGE",
        "POWER": 30,
        "MP_COST": 10,
        "DISC": "A cutting wind attack that slashes foes.",
        "STAT_SCALING": {"ATK": 2.0},
    },
    "Lightning Arc": {
        "TYPE": "attack",
        "CLASS": "MAGE",
        "POWER": 32,
        "MP_COST": 12,
        "DISC": "An arcing lightning strike that zaps multiple enemies.",
        "STAT_SCALING": {"INT": 2.2},
    },
}


