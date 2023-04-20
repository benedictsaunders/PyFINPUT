import PyFINPUT
from pprint import pprint

f = PyFINPUT.input_file("EXAMPLE", case_sensitive=False, assigner="=", comment="#", blocker="%", endblock="end_")

f.add_keyword(
    name="KW1",
    default="",
    kw_type=str,
    nkws=2
)

f.add_keyword(
    name="KW3",
    kw_type=bool,
    nkws=3
)

f.add_keyword(
    name="KW2",
    default="",
    kw_type=float,
    required=False,
    nkws=1
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

f.add_block(
    name="a_block",
    type=int,
    default=[[1,2], [3,4], [5,6]],
    minlines=1,
    nperline=0,
    required=False
)

d = f.parse_file()
pprint(d)