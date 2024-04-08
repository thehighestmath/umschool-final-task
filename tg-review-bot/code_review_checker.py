import os
import glob

from pylint.lint import Run
from pylint.reporters.text import TextReporter



class CodeReviewChecker:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.messages = []

    def load_code(self, filename):
        with open(filename, "r") as file:
            return file.readlines()

    def check_concatenation_in_loop(self, code, filename):
        for i, line in enumerate(code):
            if "for" in line:
                for j in range(
                    i, min(i + 3, len(code))
                ):
                    next_line = code[j].strip()
                    if "+" in next_line:
                        self.messages.append(
                            f"Обнаружено склеивание строк в цикле в строке {j+1} файла {filename}: {next_line}"
                        )
                        break

    def check_connection_duplication(self, code, filename):
        connect_count = 0
        for i, line in enumerate(code):
            if "connect(" in line:
                connect_count += 1
                if connect_count > 1:
                    self.messages.append(
                        f"Обнаружено дублирование подключения к базе данных в строке {i+1} файла {filename}: {line.strip()}"
                    )
                    break

    def check_backslash_continuations(self, code, filename):
        for i, line in enumerate(code):
            if "\\" in line and line.strip().endswith("\\"):
                self.messages.append(
                    f"Обнаружены продолжения строк с использованием обратного слэша в строке {i+1} файла {filename}: {line.strip()}"
                )

    def check_pep8(self):
        with open("pep8-report.out", "w") as f:
            reporter = TextReporter(f)
            Run([self.folder_path], reporter=reporter, do_exit=False)

    def run_checks(self):
        self.check_pep8()

        file_list = glob.glob(os.path.join(self.folder_path, "**/*.py"), recursive=True)

        for file_path in file_list:
            if file_path.endswith(".py"):
                code = self.load_code(file_path)
                self.check_concatenation_in_loop(code, file_path)
                self.check_connection_duplication(code, file_path)
                self.check_backslash_continuations(code, file_path)
        return self.messages


if __name__ == '__main__':
    checker = CodeReviewChecker('sample-repo')
    checker.run_checks()
    print(*checker.run_checks(), sep='\n')