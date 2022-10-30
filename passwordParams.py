import argparse

# generate password wordlists based on the parameters provided.


list = []
list_to_write = []


# print all combinations of the values in the list
def writeAllCombinations(list, var, delimiter):
    var = var.split(" ")
    for i in var:
        list.append(i)

    with open("passwords.txt", "w", encoding="UTF8") as f:
        for line in list:
            f.write(line + "\n")

    for i, _ in enumerate(list):
        for item in list:
            list_to_write.append((list[i], item))

    with open("passwords.txt", "w", encoding="UTF8") as f:
        for line in list_to_write:
            f.write(line[0] + delimiter + line[1] + "\n")

        # append the values to the list


# argparse one argument for the input String and one argument for the delimiter
parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", help="input string", required=True, type=str, dest="input", action="store"
)
parser.add_argument(
    "-d",
    help="which delimiter to use",
    action="store",
    default="-",
    required=False,
    dest="delimiter",
)
args = parser.parse_args()


var = args.input
delimiter = args.delimiter or "-"
writeAllCombinations(list=list, var=var, delimiter=delimiter)
