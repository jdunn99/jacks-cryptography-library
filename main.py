from operations import operations
from number_theory import modular


# operations.all_shifts("hello world")

# txt = "VVHQWVVRHMUSGJGTH"


# # print(operations.coinc("VVHQWVVRHMUSGJGTH", 5))
# # print(operations.frequency(operations.choose(txt, 5, 1)))
# # val = operations.choose(txt, 5, 1)

# # print(operations.vigvec(txt, 5, 1))
# print(operations.corr([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.25, 0.5, 0.0, 0.0, 0.0, 0.0]))

# vvhq = "vvhqwvvrhmusgjgthkihtssejchlsfcbgvwcrlryqtfsvgahwkcuhwauglqhnslrljshbltspisprdxljsveeghlqwkasskuwepwqtwvspgoelkcqyfnsvwljsniqkgnrgybwlwgoviokhkazkqkxzgyhcecmeiujoqkwfwvefqhkijrclrlkbienqfrjljsdhgrhlsfqtwlauqrhwdmwlgusgikkflryvcwvspgpmlkassjvoqxeggveyggzmljcxxljsvpaivwikvrdrygfrjljslveggveyggeiapuuisfpbtgnwwmuczrvtwglrwugumnczvile"
# q = "themethodusedforthepreparationandreadingofcodemessagesissimpleintheextremeandatthesametimeimpossibleoftranslationunlessthekeyisknowntheeasewithwhichthekeymaybechangedisanotherpointinfavoroftheadoptionofthiscodebythosedesiringtotransmitimportantmessageswithouttheslightestdangeroftheirmessagesbeingreadbypoliticalorbusinessrivalsetc"
# print(operations.corr(operations.vigvec(vvhq, 5, 1)))

# print(operations.vigenere(vvhq, [-2, -14, -3, -4, -18]))

# print(operations.lfsr([1, 1, 1, 0, 0], [1, 1, 0, 0, 1], 50))

print(modular.primitive_root(11))
