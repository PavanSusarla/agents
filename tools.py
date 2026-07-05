from langchain_core.tools import tool
import ast
import operator

# Allowed operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def evaluate(node):
    if isinstance(node, ast.Constant):  # numbers
        return node.value

    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)

    elif isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](evaluate(node.operand))

    raise ValueError("Unsupported expression")


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Example:
    25*18+76
    (50+10)/2
    5**3
    """

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)
        return str(result)

    except Exception as e:
        return f"Error: {e}"