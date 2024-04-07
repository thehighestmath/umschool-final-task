# from pylint.checkers import BaseChecker
# # from pylint.interfaces import IAstroidChecker
# import astroid
# from pylint.lint import PyLinter


# class SensitiveDataChecker(BaseChecker):
#     # implements = IAstroidChecker
#     name = "sensitive-data-checker"
#     msgs = {
#         "W9001": (
#             "Possible hardcoded sensitive data (%s) found.",
#             "hardcoded-sensitive-data",
#             "Hardcoded sensitive data such as passwords, tokens, private keys, etc., should not be hardcoded in source code.",
#         ),
#     }

#     def process_module(self, node):
#         """Process a module. The module's content is accessible via node.stream()"""
#         stream = node.stream()
#         for line_num, line in enumerate(stream):
#             if "password" in line or "secret" in line:
#                 self.add_message(
#                     "hardcoded-sensitive-data", line=line_num, args=(line.strip(),)
#                 )


# class FStringChecker(BaseChecker):

#     # implements = IAstroidChecker
#     name = "f-string-checker"
#     msgs = {
#         "C9002": (
#             "Old string formatting method used instead of f-string",
#             "old-string-format",
#             "Use f-strings to make string formatting clearer and faster.",
#         ),
#     }

#     def visit_binop(self, node):
#         if (
#             node.op == "%"
#             and isinstance(node.left, astroid.Const)
#             and "%" in node.left.value
#         ):
#             self.add_message("old-string-format", node=node)

#     def visit_call(self, node):
#         if isinstance(node.func, astroid.Attribute) and node.func.attrname == "format":
#             self.add_message("old-string-format", node=node)


# class LineContinuationChecker(BaseChecker):
#     # implements = IRawFileChecker
#     name = "line-continuation-checker"
#     msgs = {
#         "W9002": (
#             "Line continuation character (\\) found",
#             "line-continuation-char",
#             "Prefer using parentheses for line continuation.",
#         ),
#     }

#     def process_module(self, node):
#         with node.stream() as stream:
#             for line_num, line in enumerate(stream, 1):
#                 if line.rstrip("\n").endswith("\\"):
#                     self.add_message("line-continuation-char", line=line_num)


# class IteratingOverRangeChecker(BaseChecker):
#     # implements = IAstroidChecker
#     name = "range-iteration-checker"
#     msgs = {
#         "W9004": (
#             "Iterating over range(len(...)) detected",
#             "iter-over-range",
#             "Iterate directly over the sequence",
#         ),
#     }

#     def visit_for(self, node):
#         if (
#             isinstance(node.iter, astroid.Call)
#             and isinstance(node.iter.func, astroid.Name)
#             and node.iter.func.name == "range"
#             and isinstance(node.iter.args[0], astroid.Call)
#             and node.iter.args[0].func.attrname == "len"
#         ):
#             self.add_message("iter-over-range", node=node)


# def register(linter: PyLinter) -> None:
#     # linter.register_checker(SensitiveDataChecker(linter))
#     # linter.register_checker(FStringChecker(linter))
#     linter.register_checker(LineContinuationChecker(linter))
#     # linter.register_checker(IteratingOverRangeChecker(linter))


# from astroid import nodes
# from pylint.checkers import BaseChecker
# from pylint.lint import PyLinter
# from pylint.interfaces import IRawFileChecker


# class MyAstroidChecker(BaseChecker):
#     name = "the-shenk-checker"
#     msgs = {
#         "W0042": (
#             "Variable name not equal to 'the_shenk'",
#             "wrong-var-name",
#             "Search for variable with name TheShenk",
#         )
#     }

#     def visit_assignname(self, node: nodes.AssignName) -> None:
#         raise Exception(1)
#         if node.name != "the_shenk":
#             self.add_message("wrong-var-name", node=node)

from pylint.checkers import BaseChecker
from pylint.interfaces import ITokenChecker
from pylint.lint import PyLinter

class LineContinuationChecker(BaseChecker):
    implements = ITokenChecker

    name = 'line-continuation-checker'
    msgs = {
        'C9002': (
            "Found line continuation character (\\)",
            'line-continuation-character',
            "Used when a line continuation character (\\) is found."
        ),
    }

    def process_tokens(self, tokens):
        for token_type, token, (start_row, start_col), _, _ in tokens:
            if token == "\\":
                self.add_message('C9002', line=start_row)

def register(linter: PyLinter) -> None:
    """Required method to auto register this checker."""
    linter.register_checker(LineContinuationChecker(linter))