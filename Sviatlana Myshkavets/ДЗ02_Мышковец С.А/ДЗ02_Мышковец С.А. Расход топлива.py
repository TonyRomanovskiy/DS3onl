def total_fuel_consumption(km, fuel_consum):
    """"
    Рассчитывает расход топлива по маршруту, на вход подается длина маршрута (km) и
    расход топлива на 100 километров (fuel_consume).
    """
    try:
        if km < 0 or fuel_consum < 0:
            raise ValueError("Входные данные < 0")
        else:
            total_fuel_consump = km / 100 * fuel_consum
            return f'Расход топлива на {km} км составит {total_fuel_consump} л.'
    except ValueError as ve:
        print(ve)


print(total_fuel_consumption(900, 10))
