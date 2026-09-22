def converter_valor(valor_str):
    if not valor_str:
        return 0

    valor_str = valor_str.strip()

    if not any(char.isdigit() for char in valor_str):
        return 0

    return float(valor_str.replace(".", "").replace(",", "."))