import os
import glob

class CodeReviewChecker:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.messages = []

    def load_code(self, filename):
        with open(filename, 'r') as file:
            return file.readlines()

    def check_concatenation_in_loop(self, code, filename):
        for i, line in enumerate(code):
            if 'for' in line:
                for j in range(i, min(i + 3, len(code))):  # Проверяем следующие три строки после строки с циклом
                    next_line = code[j].strip()
                    if '+' in next_line:
                        self.messages.append(f"Обнаружено склеивание строк в цикле в строке {j+1} файла {filename}: {next_line}")
                        break

    def check_connection_duplication(self, code, filename):
        connect_count = 0
        for i, line in enumerate(code):
            if 'connect(' in line:
                connect_count += 1
                if connect_count > 1:
                    self.messages.append(f"Обнаружено дублирование подключения к базе данных в строке {i+1} файла {filename}: {line.strip()}")
                    break

    def check_f_strings(self, code, filename):
        for i, line in enumerate(code):
            if '%' in line:
                self.messages.append(f"Обнаружено использование старого форматирования строк в строке {i+1} файла {filename}: {line.strip()}")

    def check_backslash_continuations(self, code, filename):
        for i, line in enumerate(code):
            if '\\' in line and line.strip().endswith('\\'):
                self.messages.append(f"Обнаружены продолжения строк с использованием обратного слэша в строке {i+1} файла {filename}: {line.strip()}")

    def run_checks(self):
        file_list = glob.glob(os.path.join(self.folder_path, '**/*.py'), recursive=True)

        # Выводим список файлов
        for file_path in file_list:
            if file_path.endswith('.py'):
                code = self.load_code(file_path)
                self.check_concatenation_in_loop(code, file_path)
                self.check_connection_duplication(code, file_path)
                self.check_f_strings(code, file_path)
                self.check_backslash_continuations(code, file_path)
        return self.messages
