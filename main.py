import random
import time
from assets import *

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################


def create_character():
    name = input("Enter your character's name: ")
    time.sleep(1)
    print("\nChoose your race: Elf, Dwarf, Human or Beastman")
    while True:
        race = input("Race: ").lower()
        if race in ["elf", "dwarf", "human", "beastman"]:
            break
        else:
            pass
    print("\nChoose your class: Rogue, Knight, or Mage")
    while True:
        character_class = input("Class: ").lower()
        if character_class in ["rouge","knight",'mage']:
            break
        else:
            pass

    character = {
        "name": name,
        "race": race,
        "class": character_class,
        "LVL": 1,
        "EXP": 0,
        "MXP": 100,
        "HP": 10,
        "ATK": 0,
        "AGI": 5,
        "DEF": 5,
        "INT": 5,
        "MP": 10,
        "MMP": 10,
        "inventory": {
            "weapons": [],
            "potions": [],
            "armors": [],
            "accessories": []
        },
        "equipped_items": {"weapon": None, "armor": None},
        "floor": 1,
        "MHP": 10,
        "skills": [],
        "GOLD": 100
    }
    if character_class == "rogue":
        character["AGI"] += 7
        character["ATK"] += 3
        character["DEF"] += 2
        character["skills"].append("Slash")
    elif character_class == "knight":
        character["HP"] += 15
        character["MHP"] += 15
        character["ATK"] += 4
        character["DEF"] += 6
        character["skills"].append("Basic Sword Art")
    elif character_class == "mage":
        character["INT"] += 8
        character["MP"] += 10
        character["MMP"] += 10
        character["skills"].append("Fireball")

    if race == "human":
        character["ATK"] += 4
        character["DEF"] += 4
        character["AGI"] += 4
        character["INT"] += 4
        character["HP"] += 10
        character["MHP"] += 10
        character["MP"] += 5
        character["MMP"] += 5
    elif race == "elf":
        character["HP"] += 7
        character["MHP"] += 7
        character["ATK"] += 3
        character["AGI"] += 5
        character["DEF"] += 1
        character["MP"] += 10
        character["MMP"] += 10
    elif race == "dwarf":
        character["ATK"] += 5
        character["HP"] += 3
        character["MHP"] += 3
        character["DEF"] += 10
        character["MP"] += 3
        character["MMP"] += 3
    elif race == "beastman":
        character["ATK"] += 7
        character["DEF"] += 5
        character["HP"] += 3
        character["MHP"] += 3
        character["MP"] += 5
        character["MMP"] += 5

    return character


#################################################################################################################################################
#################################################################################################################################################

def levelup(character):
    """Increase the character's level and stats when they gain enough XP."""
    if character["EXP"] >= character['MXP']:
        # Calculate the level-up
        character["LVL"] += 1
        character["EXP"] -= character['MXP']  # Reseting XP after leveling up
        print(f"{character['name']} leveled up to level {character['LVL']}!")

        # Increase stats upon leveling up
        character["ATK"] += 2
        character["DEF"] += 2
        character["MHP"] += 5
        character["MMP"] += 3
        character["MP"] = character["MMP"]
        character["HP"] = character["MHP"]
        character['MXP'] += 50


################################################################################################################################################
################################################################################################################################################

def add_inventory(character, item_name):
    item = items.get(item_name)
    if item:
        item_class = item["CLASS"]
        character["inventory"][f"{item_class}s"].append(item_name)
        print(f"{item_name} added to inventory!")
    else:
        print(f"Item {item_name} not found.")


#################################################################################################################################################
#################################################################################################################################################

def roll_loot(monster):
    monster_name = monster['name']
    if monster_name not in list(drops.keys()):
        print(f"Monster {monster_name} not found in loot tables.")
        return None
    # Handles dropping gold
    gold_min, gold_max = monster['GOLD']
    gold_dropped = random.randint(gold_min, gold_max)
    print(f"{monster_name} dropped {gold_dropped} gold")
    # Handles dropping item loot
    mdrops = drops[monster_name]
    items = list(mdrops.keys())
    weights = list(mdrops.values())

    dropped_item = random.choices(items, weights=weights, k=1)[0]
    print(f"Rolled loot: {dropped_item}")
    return dropped_item, gold_dropped


################################################################################################################################################
################################################################################################################################################

def use_skill(character, skill_name, target):
    skill = skills.get(skill_name)
    if not skill:
        print(f"{skill_name} is not a valid skill.")
        return
    if character["MP"] < skill["MP_COST"]:
        print(f"Not enough MP to use {skill_name}!")
        return
    total_damage = skill["POWER"]
    scaling_factors = skill["STAT_SCALING"]

    for stat, scale in scaling_factors.items():
        if stat in character:
            total_damage += character[stat] * scale
    character["MP"] -= skill["MP_COST"]

    if skill["TYPE"] == "support":
        restored_amount = min(target["MHP"] - target["HP"], int(total_damage))
        target["HP"] += restored_amount
        print(f"{character['name']} used {skill_name} and restored {restored_amount} HP!")
    else:
        damage = max(1, int(total_damage) - target["DEF"])
        target["HP"] -= damage
        print(f"{character['name']} used {skill_name} and dealt {damage} damage!")


################################################################################################################################################
################################################################################################################################################

# Use Potion
def use_potion(character, potion_name):
    potion = items.get(potion_name)
    if potion and potion["CLASS"] == "potion":
        for stat, value in potion["STATS"].items():
            max_stat = f"M{stat}"
            if stat in ["HP", "MP"]:
                restored_amount = min(character[max_stat] - character[stat], value)
                character[stat] += restored_amount
                print(f"{potion_name} used! {stat} restored by {restored_amount}.")

        character["inventory"]["potions"].remove(potion_name)
    else:
        print(f"{potion_name} is not a valid potion.")


################################################################################################################################################
################################################################################################################################################
"""                                                          EQUIPING/UNEQUIPING ITEMS                                                              """


def unequip_item(character, item_name):
    item = items.get(item_name)
    if item and item_name in character["equipped_items"].values():
        item_class = item["CLASS"]

        for stat, value in item["STATS"].items():
            character[stat] -= value

        character["equipped_items"][item_class] = None

        print(f"{item_name} unequipped. Removed stats: {item['STATS']}.")
    else:
        print(f"{item_name} is not equipped.")


def equip_item(character, item_name):
    item = items.get(item_name)
    if item and item["CLASS"] in ["weapon", "armor", "accessory"]:
        item_class = item["CLASS"]

        equipped_item = character["equipped_items"].get(item_class)
        if equipped_item:
            unequip_item(character, equipped_item)

        character["equipped_items"][item_class] = item_name

        for stat, value in item["STATS"].items():
            character[stat] += value

        print(f"{item_name} equipped! Applied stats: {item['STATS']}.")
    else:
        print(f"{item_name} cannot be equipped.")


################################################################################################################################################
################################################################################################################################################


def learn_skill(character, skill_name):
    if skill_name in skills:
        if skills[skill_name]["CLASS"].lower() == character["class"].lower():
            if skill_name not in character["skills"]:
                character["skills"].append(skill_name)
                print(f"You have learned {skill_name}!")
            else:
                print(f"You already know {skill_name}.")
        else:
            print(f"{skill_name} is not suitable for your class.")
    else:
        print(f"{skill_name} does not exist.")


################################################################################################################################################
################################################################################################################################################

def shop(character):
    print("\nWelcome to the Shop! You have", character['GOLD'], "gold.")
    while True:
        print("\nAvailable Items for Sale:")
        for i, (item_name, details) in enumerate(shop_inventory.items()):
            print(f"{i + 1}. {item_name} - {details['price']} gold")
        print("0. Exit Shop")

        choice = input("\nSelect an item to buy or 0 to exit: ")
        if choice == "0":
            print("Thank you for visiting the shop!")
            break
        item_index = int(choice) - 1
        item_name = list(shop_inventory.keys())[item_index]
        item_price = shop_inventory[item_name]['price']
        if character['GOLD'] >= item_price:
            if shop_inventory[item_name]['skill'] in skills:
                print(f"Learning the skill {shop_inventory[item_name]['skill']}")
                time.sleep(1)
                learn_skill(character, shop_inventory[item_name]['skill'])
            else:
                add_inventory(character, item_name)
            character['GOLD'] -= item_price
            print(f"You purchased {item_name} for {item_price} gold!")
        else:
            print("You don't have enough gold!")


################################################################################################################################################
################################################################################################################################################
def combat(character, monster):
    time.sleep(1)
    print(f"\nA wild {monster['name']} appears!")
    while character["HP"] > 0 and monster["HP"] > 0:
        print(
            f"\n{character['name']}'s HP: {character['HP']}/{character['MHP']} | MP: {character['MP']} / {character['MMP']} | LVL: {character['LVL']} | XP: {character['EXP']}/{character['MXP']}")
        print(f"{monster['name']}'s HP: {monster['HP']}")

        print(f"\nWhat will {character['name']} do?")
        action = input("1. Attack 2. Flee 3. Open Inventory: ")
        # Attacking
        if action == "1":
            print("\nChoose a skill to use:")
            for i, skill in enumerate(character["skills"]):
                print(f"{i + 1}. {skill} - {skills[skill]['DISC']}")
            skill_choice = int(input("Select skill: ")) - 1
            if 0 <= skill_choice < len(character["skills"]):
                if skills[character["skills"][skill_choice]]["CLASS"] != "support":
                    use_skill(character, character["skills"][skill_choice], monster)
                elif skills[character["skills"][skill_choice]]["CLASS"] == "support":
                    use_skill(character, character["skills"][skill_choice], character)
                    continue
            else:
                print("Invalid skill choice!")
        # Fleeing (ends the current run)
        elif action == "2":
            print(f"{character['name']} fled the battle!")
            return False
        # Opening the inventory
        elif action == "3":  # Inventory Menu
            print("\nYour Inventory:")
            print(f"1. Weapons: {character['inventory']['weapons']}")
            print(f"2. Armor: {character['inventory']['armors']}")
            print(f"3. Accessories: {character['inventory']['accessories']}")
            print(f"4. Potions: {character['inventory']['potions']}")
            print(f"5. Gold: {character['GOLD']}")

            inventory_action = input("\nChoose an option (1: Equip Item | 2: Use Potion): ")

            if inventory_action == "1":  # Equip Items
                equip_choice = input("Equip what? (weapon, armor, accessory): ").lower()
                if equip_choice in ["weapon", "armor", "accessory"]:
                    available_items = character["inventory"][f"{equip_choice}s"]
                    if not available_items:
                        print(f"You have no {equip_choice}s!")
                        continue

                    print(f"Available {equip_choice}s: {available_items}")
                    item_name = input(f"Enter the {equip_choice} to equip: ").title()

                    if item_name in available_items:
                        equip_item(character, item_name)
                    else:
                        print(f"You don't have {item_name}.")

            elif inventory_action == "2":  # Use Potions
                if not character["inventory"]["potions"]:
                    print("You have no potions!")
                else:
                    print(f"Available Potions: {character['inventory']['potions']}")
                    potion_name = input("Enter the potion to use: ")

                    if potion_name in character["inventory"]["potions"]:
                        use_potion(character, potion_name)
                    else:
                        print("You don't have that potion.")
            continue

        if monster["HP"] > 0:
            damage = random.randint(monster["ATK"] - 3, monster["ATK"] + 3)
            print(f"{monster['name']} attacks and deals {damage} damage!")
            character["HP"] -= damage

    if character["HP"] > 0:
        print(f"\n{character['name']} defeated the {monster['name']}!\n")
        # Loot Handling
        loot, gold = roll_loot(monster)
        add_inventory(character, loot)
        character['GOLD'] += gold

        # EXP handling
        character["EXP"] += monster["EXP"]
        print(f"{character['name']} gained {monster['EXP']} XP!")
        levelup(character)
        return True
    else:
        print(f"\n{character['name']} was defeated by the {monster['name']}.")
        return False
    time.sleep(1)


################################################################################################################################################
################################################################################################################################################

def rest_floor(character):
    print("\n-------------Rest Floor----------------")
    time.sleep(2)
    print(
        f"{character['name']} has rested! {character['MHP'] - character['HP']} HP, {character['MMP'] - character['MP']} MP has been restored!")
    character["MP"] = character["MMP"]
    character["HP"] = character["MHP"]
    # Shop functionality finally added
    shop(character)


################################################################################################################################################
################################################################################################################################################

def explore_floor(character):
    current_floor = floors[character['floor']]
    print(f"\n-------Floor {character['floor']}------- ")

    for monster in current_floor['monsters']:
        if not combat(character, monster):
            print("Game Over!")
            return False
    time.sleep(3)
    return True


################################################################################################################################################
################################################################################################################################################

def next_floor(character):
    if character['floor'] == 1 or 6 or 9 or 12:  # change it to 3 later
        print(f"{character['name']} finds a crevice? where does this lead")
        character['floor'] += 1
        rest_floor(character)
        return True
    if character['floor'] < 13:
        character['floor'] += 1
        print(f"\n{character['name']} moves to Floor {character['floor']}!")
        return True
    else:
        print("You've reached the boss floor! Prepare for the final battle!")
        return False


################################################################################################################################################
################################################################################################################################################

def main_game():
    print("Welcome to the Dungeon!")
    character = create_character()

    while True:
        if not explore_floor(character):
            break

        if character['floor'] == 12:
            print(f"Congratulations, {character['name']}! You've reached the boss floor!")



        next_floor(character)

    print("\nGame Over!")
    print(f"{character['name']} reached floor {character['floor']}.")
    print("Inventory:", character['inventory'])


################################################################################################################################################
################################################################################################################################################
if __name__ == "__main__":
    main_game()
