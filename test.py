# Test different values
agility = 100 # Max: 100
base_physical_attack = 48.25 # Max: 48.25
level = 50 # Max: 50

def calculate_critical_hit(base_physical_attack, agility, level): 
    critical_hit = base_physical_attack + round(2.5 * ((agility * 16) / 100) + 0.08 * level, 0)
    return critical_hit

critical_hit_value = calculate_critical_hit(base_physical_attack, agility, level)

print(f"Base Physical Attack: {base_physical_attack}\nCritical Hit: {critical_hit_value}")