import random
#monster encounter 
#e means enemy
#p means player

def pAttack(pDamage): #player damage
    print("You attack!")
    damage = random.randint(1, 6) + pDamage #random damage add-on
    print("You did", damage, "damage")
    return damage
    
def eAttack(eDamage):
    print("The monster attacks!")
    damage = random.randint(1, 3) + eDamage #random damage add-on
    print("You took", damage, "damage")
    return damage

def getCommand():
    command = input("\nWhat do you do? ")
    
    return command

def main():
    pHealth = 100
    pDamage = 10
    eHealth = 50
    eDamage = 5
    #pAlive = True
    
    print("\nYou encountered a monster\n")
    
    while (eHealth > 0) and (pHealth > 0):
        command = getCommand()
        if command == "attack":
            eHealth -= pAttack(pDamage)  #do damage to enemy
            if eHealth >= 0:
                print("  Monster HP:", eHealth)
            else:
                print("you killed the monster")
        elif command == "run":
            print("You bravely ran away, away!")
            quit()
        
        pHealth -= eAttack(eDamage) 
        if pHealth >= 0:
            print("  HP:", pHealth)
        else:
            print("you died")
            #pAlive = False
        
                
    
    
main()