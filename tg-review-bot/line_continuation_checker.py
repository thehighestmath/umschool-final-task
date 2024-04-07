import os
import subprocess

class CodeReviewChecker:
    def __init__(self, filename):
        self.filename = filename
        self.code = None
        self.messages = []

    def load_code(self):
        with open(self.filename, 'r') as file:
            self.code = file.readlines()

    def check_concatenation_in_loop(self):
        for i, line in enumerate(self.code):
            if 'for' in line:
                for j in range(i, min(i + 3, len(self.code))):  # Проверяем следующие три строки после строки с циклом
                    next_line = self.code[j].strip()
                    if '+' in next_line:
                        self.messages.append(f"Обнаружено склеивание строк в цикле в строке {j+1} файла {self.filename}: {next_line}")
                        break

    def check_connection_duplication(self):
        connect_count = 0
        for i, line in enumerate(self.code):
            if 'connect' in line:
                connect_count += 1
                if connect_count > 1:
                    self.messages.append(f"Обнаружено дублирование подключения к базе данных в строке {i+1} файла {self.filename}: {line.strip()}")
                    break

    def check_f_strings(self):
        for i, line in enumerate(self.code):
            if '%' in line:
                self.messages.append(f"Обнаружено использование старого форматирования строк в строке {i+1} файла {self.filename}: {line.strip()}")

    def check_backslash_continuations(self):
        for i, line in enumerate(self.code):
            if '\\' in line and line.strip().endswith('\\'):
                self.messages.append(f"Обнаружены продолжения строк с использованием обратного слэша в строке {i+1} файла {self.filename}: {line.strip()}")

    def run_checks(self):
        self.load_code()
        self.check_concatenation_in_loop()
        self.check_connection_duplication()
        self.check_f_strings()
        self.check_backslash_continuations()
        return self.messages

if __name__ == "__main__":
    checker = CodeReviewChecker("sample1.py")
    messages = checker.run_checks()
    for message in messages:
        print(message)