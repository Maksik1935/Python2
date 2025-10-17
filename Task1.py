def sum_distance(frm, to):
    """Суммирует все числа от frm до to включительно"""
    # Меняем местами, если порядок обратный
    if frm > to:
        frm, to = to, frm

    total = 0
    for num in range(frm, to + 1):
        total += num

    return total