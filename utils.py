def read_input(filepath, conversion_function=None):
    if not conversion_function:
        def conversion_function(x): return x

    with open(filepath) as f:
        return [conversion_function(line.strip()) for line in f]
