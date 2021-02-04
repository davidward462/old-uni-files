#character creation
import character

def main():
 
	print("make your character")
	
	name = input("Name: ")
	health = int(input("Health: "))
	weapon = input("Weapon: ")
	armour = input("Armour: ")
	
	player = character.character(name, health, weapon, armour)
	
	print()
	print(player.name)
	print(player.health)
	print(player.weapon)
	print(player.armour)
	
 
main()