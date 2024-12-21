class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve_and_print(self):
        print(eval(self.expression))

expression = "3 + 4 * 2 - (1 / 2)"
solver = ExpressionSolver(expression)
solver.solve_and_print()
