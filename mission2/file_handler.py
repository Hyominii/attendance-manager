class FileHandler:
    def __init__(self, filename: str):
        self._filename = filename

    def write(self, data: str):
        with open(self._filename, 'w', encoding='utf-8') as f:
            f.write(data)

    def read(self) -> str:
        with open(self._filename, 'r', encoding='utf-8') as f:
            line = f.readline().strip()
            return line

    def read_all_lines(self) -> list:
        with open(self._filename, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
            return lines
