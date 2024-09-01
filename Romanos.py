#Crear un sistema que me regrese los numeros romanos al ingresar cualquier palabras
# i = 1
# v = 5
# x = 10
# l = 50
# c = 100
# d = 500
# m = 1000 
def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in roman:
        value = roman_values.get(char, 0)
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    
    return total

def suma_numeros_romanos_en_palabra(palabra):
    """Suma todos los números romanos válidos en una palabra dada respetando el orden."""
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    solo_romanos = [char for char in palabra.upper() if char in roman_values]
    
    return roman_to_int(''.join(solo_romanos))


palabra = input("Introduce una palabra: ")
resultado = suma_numeros_romanos_en_palabra(palabra)
print(f"La palabra '{palabra}' en números romanos es: {resultado}")