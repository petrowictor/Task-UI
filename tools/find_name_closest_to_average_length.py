def find_name_closest_to_average_length(first_names: list[str]) -> str:
    lengths = [len(name) for name in first_names]
    average_length = sum(lengths) / len(lengths)
    closest_name = min(first_names, key=lambda name: abs(len(name) - average_length))

    return closest_name