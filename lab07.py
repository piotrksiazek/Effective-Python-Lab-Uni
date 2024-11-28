import argparse

parser = argparse.ArgumentParser(
    description="Obliczanie wartości pochodnej numerycznej z podanymi parametrami."
)

parser.add_argument(
    "-f", "--function", type=str, required=True,
    help="Funkcja")

parser.add_argument(
    "-x0", "--start_point", type=float, required=True, 
    help="Ustalony punkt startowy"
)
parser.add_argument(
    "-hs", "--step_size", type=float, required=True, 
    help="Wielkość kroku w obliczeniach pochodnej"
)
parser.add_argument(
    "-n", "--steps", type=int, required=True, 
    help="Ilość kroków metody"
)
parser.add_argument(
    "-e", "--accuracy", type=float, required=False, default=1e-5,
    help="Dokładność obliczeń (domyślnie: 1e-5)"
)
parser.add_argument(
    "--help_extended", action="help",
    help="Wyświetl rozszerzoną pomoc z opisem działania programu"
)

# python3 lab07.py -f "x**2" -x0 1 -hs 0.001 -n 100 -e 0.001

def evaluate_function(expression, x):
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Błąd przy obliczaniu wartości funkcji {x}: {e}")

args = parser.parse_args()

def newtons_method():
    x = args.start_point
    for i in range(args.steps):
        f_x =evaluate_function(args.function, x)
        f_x_plus_h = evaluate_function(args.function, x + args.step_size)
        derivative = (f_x_plus_h - f_x) / args.step_size
        x = x - f_x / derivative
        if abs(f_x) < args.accuracy:
            break
    return x


print(newtons_method())


