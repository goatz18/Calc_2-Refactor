# pylint: skip-file

from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
import pandas as pd
data = pd.read_csv("../fileutilities/addition.csv")
data = pd.read_csv("../fileutilities/subtraction.csv")
data = pd.read_csv("../fileutilities/multiplication.csv")
data = pd.read_csv("../fileutilities/division.csv")

