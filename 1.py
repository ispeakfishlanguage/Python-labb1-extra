def arrayCheck(nums):
    # Fortsätt till det tredje sista elementet för att undvika felet index out of range
    for i in range(len(nums) - 2):
        # Kontrollera om vi har hittat sekvensen 1, 2, 3
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

# Testar funktionen
print(arrayCheck([1, 1, 2, 3, 1]))  # borde ange True
print(arrayCheck([1, 1, 2, 4, 1]))  # borde ange False
print(arrayCheck([1, 1, 2, 1, 2, 3]))  # borde ange True
