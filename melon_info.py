"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melon(melons_dict):
    """Print each melon with corresponding attribute information."""

    for name, traits in melons_dict.items():
        print(name.upper())
        for traits, value in traits.items():
            print(traits, ":", value)

print_melon(melons_dict)