import copy

# Custom Exception for MonsterManager
class MonsterManagerError(Exception):
    pass

# Prototype Interface
class MonsterPrototype:

    def clone(self):
        """
        Creates and returns a clone of the monster object.
        """
        pass

# Concrete Prototypes
class MonsterA(MonsterPrototype):

    def __init__(self, health, attack_power, speed):
        self.health = health
        self.attack_power = attack_power
        self.speed = speed

    def clone(self):
        """
        Clones the MonsterA prototype and returns the cloned instance.
        """
        return copy.deepcopy(self)

class MonsterB(MonsterPrototype):

    def __init__(self, health, attack_power, speed, special_ability):
        self.health = health
        self.attack_power = attack_power
        self.speed = speed
        self.special_ability = special_ability

    def clone(self):
        """
        Clones the MonsterB prototype and returns the cloned instance.
        """
        return copy.deepcopy(self)

# Client
class MonsterManager:

    def __init__(self):
        self.monster_prototypes = {}

    def register_prototype(self, name, prototype):
        """
        Registers a monster prototype with the given name.
        """
        self.monster_prototypes[name] = prototype

    def create_monster(self, name, **attributes):
        """
        Creates a new monster by cloning the specified prototype and customizing its attributes.
        """
        
        try:
            if name in self.monster_prototypes:
                prototype = self.monster_prototypes[name]
                monster = prototype.clone()

                # Customize the cloned monster's attributes
                for attr, value in attributes.items():
                    setattr(monster, attr, value)

                return monster
            else:
                raise ValueError(f"Prototype '{name}' not found.")
        except Exception as e:
            raise MonsterManagerError(f"Error creating monster: {str(e)}")

# Usage example
if __name__ == "__main__":
    try:
        # Create a MonsterManager instance
        monster_manager = MonsterManager()

        # Create and register monster prototypes
        monster_a_prototype = MonsterA(100, 10, 5)
        monster_manager.register_prototype("MonsterA", monster_a_prototype)

        monster_b_prototype = MonsterB(150, 15, 7, "Fireball")
        monster_manager.register_prototype("MonsterB", monster_b_prototype)

        # Create new monsters by cloning prototypes and customizing their attributes
        monster_a = monster_manager.create_monster("MonsterA", health=80)
        monster_b = monster_manager.create_monster("MonsterB", special_ability="Ice Beam", speed=8)

        # Create more monsters
        monster_c = monster_manager.create_monster("MonsterA", health=120, attack_power=12, speed=6)
        monster_d = monster_manager.create_monster("MonsterB", health=180, attack_power=20, special_ability="Thunderbolt")

        # Print the attributes of the cloned and customized monsters
        print("Monster A:")
        print(f"Health: {monster_a.health}")
        print(f"Attack Power: {monster_a.attack_power}")
        print(f"Speed: {monster_a.speed}\n")

        print("Monster B:")
        print(f"Health: {monster_b.health}")
        print(f"Attack Power: {monster_b.attack_power}")
        print(f"Speed: {monster_b.speed}")
        print(f"Special Ability: {monster_b.special_ability}\n")

        print("Monster C:")
        print(f"Health: {monster_c.health}")
        print(f"Attack Power: {monster_c.attack_power}")
        print(f"Speed: {monster_c.speed}\n")

        print("Monster D:")
        print(f"Health: {monster_d.health}")
        print(f"Attack Power: {monster_d.attack_power}")
        print(f"Speed: {monster_d.speed}")
        print(f"Special Ability: {monster_d.special_ability}")
    except MonsterManagerError as e:
        print(f"Monster Manager Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")