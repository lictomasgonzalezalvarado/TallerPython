if __name__ == '__main__':
    # Ejemplo de conversiones en Python

    # Conversión de str a int y float
    num_str = "25"
    num_int = int(num_str)  # Convierte "25" a entero
    num_float = float(num_str)  # Convierte "25" a flotante

    print(f"Original (str): {num_str} -> int: {num_int}, float: {num_float}")

    # Conversión de int a float y str
    num_int = 10
    num_float_from_int = float(num_int)  # Convierte 10 a 10.0 (float)
    num_str_from_int = str(num_int)  # Convierte 10 a "10" (str)

    print(f"Original (int): {num_int} -> float: {num_float_from_int}, str: {num_str_from_int}")

    # Conversión de float a int y str
    num_float = 15.7
    num_int_from_float = int(num_float)  # Convierte 15.7 a 15 (int) - se trunca el decimal
    num_str_from_float = str(num_float)  # Convierte 15.7 a "15.7" (str)

    print(f"Original (float): {num_float} -> int: {num_int_from_float}, str: {num_str_from_float}")

    # Conversión de str a bool
    str_true = "True"
    str_false = "False"
    bool_true = bool(str_true)  # Convierte "True" a True (bool)
    bool_false = bool(str_false)  # Convierte "False" a True (bool), ya que el string no está vacío

    print(f"Original (str): {str_true} -> bool: {bool_true}")
    print(f"Original (str): {str_false} -> bool: {bool_false}")

    # Conversión de int y float a bool
    zero_int = 0
    non_zero_int = 5
    zero_float = 0.0
    non_zero_float = 3.14

    bool_zero_int = bool(zero_int)  # Convierte 0 a False
    bool_non_zero_int = bool(non_zero_int)  # Convierte 5 a True
    bool_zero_float = bool(zero_float)  # Convierte 0.0 a False
    bool_non_zero_float = bool(non_zero_float)  # Convierte 3.14 a True

    print(f"Original (int): {zero_int} -> bool: {bool_zero_int}")
    print(f"Original (int): {non_zero_int} -> bool: {bool_non_zero_int}")
    print(f"Original (float): {zero_float} -> bool: {bool_zero_float}")
    print(f"Original (float): {non_zero_float} -> bool: {bool_non_zero_float}")