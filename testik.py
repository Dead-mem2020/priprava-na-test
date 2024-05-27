# Funkce s parametrem, která kontroluje, zda je číslo sudé
def is_even(number):
    return number % 2 == 0

# Hlavní část programu
def main():
    # 1. Použití obou typů cyklů
    # Cyklus s pevným počtem opakování
    repeat_count = int(input("Zadejte, kolikrát se má cyklus s pevným počtem opakování opakovat: "))
    print("Cyklus s pevným počtem opakování:")
    for i in range(repeat_count):
        print(f"Opakování {i + 1}")

    # Cyklus s podmínkou
    max_count = int(input("Zadejte maximální počet opakování pro cyklus s podmínkou: "))
    print("Cyklus s podmínkou:")
    count = 0
    while count < max_count:
        print(f"Opakování {count + 1}")
        count += 1

    # 2. Funkce s parametrem (už jsme definovali výše)

    # 3. Operace s polem (list)
    my_list = []

    # Přidání do pole pomocí čísla
    number = int(input("Zadejte číslo, které chcete přidat do pole: "))
    my_list.append(number)
    
    # Přidání do pole pomocí názvu (přidáme hodnotu proměnné)
    value_to_add = int(input("Zadejte další číslo, které chcete přidat do pole: "))
    my_list.append(value_to_add)

    print(f"Pole po přidání prvků: {my_list}")

    # Odebrání prvku z pole
    number_to_remove = int(input("Zadejte číslo, které chcete odebrat z pole: "))
    if number_to_remove in my_list:
        my_list.remove(number_to_remove)
        print(f"Pole po odebrání prvku: {my_list}")
    else:
        print(f"Číslo {number_to_remove} není v poli.")

    # 4. Použití různých datových typů
    my_int = int(input("Zadejte celé číslo: "))
    my_string = input("Zadejte nějaký text: ")
    my_float = float(input("Zadejte desetinné číslo: "))
    my_boolean = input("Zadejte True nebo False: ").strip().lower() == 'true'

    print(f"Integer: {my_int}, String: {my_string}, Float: {my_float}, Boolean: {my_boolean}")

    # 5. Vstup a výstup s přetypováním
    user_input = input("Zadejte celé číslo: ")
    user_number = int(user_input)
    print(f"Zadal jste číslo: {user_number}")

    # 6. Práce s podmínkou a logickými funkcemi AND, OR, NOT
    if is_even(user_number) and my_boolean:
        print("Číslo je sudé a boolean je True")
    elif not is_even(user_number) or not my_boolean:
        print("Číslo je liché nebo boolean je False")

# Spuštění hlavní části programu
if __name__ == "__main__":
    main()