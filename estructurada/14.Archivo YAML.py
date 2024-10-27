import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Acceder a los valores
valor1 = config['clave1']
valorA = config['claveA']

print(valor1)  # Salida: valor1
print(valorA)  # Salida: valorA