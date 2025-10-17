def trim_and_repeat(s: str, offset: int = 0, repetitions: int = 1) -> str:
    """
    Обрезает строку слева на offset символов и повторяет получившуюся строку repetitions раз.
    offset по умолчанию = 0, repetitions = 1.
    Отрицательный offset считается как 0; repetitions <= 0 даёт пустую строку.
    """
    if offset < 0:
        offset = 0
    if repetitions <= 0:
        return ""
    trimmed = s[offset:]  # если offset >= len(s), получится пустая строка
    return trimmed * repetitions