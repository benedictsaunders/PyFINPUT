import src.PyFINPUT.pyfinput as pyfinput
from pprint import pprint

f = pyfinput.input_file("EXAMPLE", case_sensitive=False, assigner="=", comment="#")

f.add_keyword(
    name="KW1",
    default="",
    kw_type=str
)

f.add_keyword(
    name="KW3",
    kw_type=bool
)

f.add_keyword(
    name="KW2",
    default="",
    kw_type=float,
)

f.add_keyword(
    name="KW4",
    default="",
    nkws = 4,
    kw_type=int
)

f.add_keyword(
    name="KW5",
    required=True,
    kw_type=float
)

d = f.parse_file()
pprint(d)