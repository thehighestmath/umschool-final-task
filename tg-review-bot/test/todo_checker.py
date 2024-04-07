from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker
from pylint.lint import PyLinter


class TodoIssueChecker(BaseChecker):
    __implements__ = IRawChecker

    def process_module(self, node):
        # raise Exception(1)
        with node.stream() as stream:
            for (lineno, line)) in enumerate(stream):
                if ha


def register(linter: PyLinter) -> None:
    linter.register_checker(TodoIssueChecker(linter))
