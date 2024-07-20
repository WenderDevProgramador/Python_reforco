def converter_temperatura(temperatura, escala):
    """
    Converte temperaturas entre Celsius e Fahrenheit.
    
    Parâmetros:
    temperatura (float): A temperatura a ser convertida.
    escala (str): A escala da temperatura fornecida ('C' para Celsius, 'F' para Fahrenheit).
    
    Retorna:
    float: A temperatura convertida na outra escala.
    """
    if escala.upper() == 'C':
        # Converte de Celsius para Fahrenheit
        return (temperatura * 9/5) + 32
    elif escala.upper() == 'F':
        # Converte de Fahrenheit para Celsius
        return (temperatura - 32) * 5/9
    else:
        raise ValueError("A escala deve ser 'C' para Celsius ou 'F' para Fahrenheit")

# Exemplos de uso:
celsius = 25
fahrenheit = 77

print(f"{celsius}°C é igual a {converter_temperatura(celsius, 'C')}°F")
print(f"{fahrenheit}°F é igual a {converter_temperatura(fahrenheit, 'F')}°C")
