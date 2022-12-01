def parse_input(path):
    file = open(path, 'r')
    content = file.read().split('\n')
    file.close()
    return content