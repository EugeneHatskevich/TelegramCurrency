def value_validation(value: str) -> bool:
    try:
        float(value.replace(',', '.'))
        if not('_' in value):
            return True
        else:
            return False
    except ValueError:
        return False
