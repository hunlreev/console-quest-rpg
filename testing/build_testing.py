strength = 50
endurance = 50
intelligence = 50
willpower = 50
agility = 50
speed = 50
level = 1

physical_attack = round(1.0 + 10.5 * (strength / 100) * (1 + 0.07 * level), 0)

magical_attack = round(1.0 + 10.5 * (intelligence / 100) * (1 + 0.07 * level), 0)

critical_hit = round(1.5 * (1 + agility / 100) + physical_attack + 0.09 * level, 0)

dodge_chance = round(agility / 200 + 0.002 * level, 2)

critical_chance =  round(agility / 400 + 0.002 * level, 2)

spell_cost_values = max(8, round(40 * (1.4 - 0.012 * willpower - 0.0005 * level), 0))

health_values = round(endurance * (2 + level * 0.025), 0)

mana_values = round(intelligence * (2 + level * 0.025), 0)

stamina_values = round(strength * (2 + level * 0.025), 0)

print("Physical Attack:", physical_attack)
print("Magical Attack:", magical_attack)
print("Critical Hit:", critical_hit)
print("Dodge Chance:", dodge_chance)
print("Critical Chance:", critical_chance)
print("Spell Cost:", spell_cost_values)
print("\nHealth:", health_values)
print("Mana:", mana_values)
print("Stamina:", stamina_values)