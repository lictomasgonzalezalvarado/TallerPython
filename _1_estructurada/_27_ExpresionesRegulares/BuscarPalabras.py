import re

if __name__ == '__main__':
    texto = "Python es un lenguaje de programación poderoso y fácil de aprender. Python es muy popular."

    # Busca todas las ocurrencias de "Python"
    coincidencias = re.findall(r'\bPython\b', texto)
    print(f"La palabra 'Python' aparece {len(coincidencias)} veces en el texto.")