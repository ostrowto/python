from csv_diff import load_csv, compare


diff=compare(
    load_csv(open("Zeszyt1.csv"), key="id"),
    load_csv(open("Zeszyt2.csv"), key="id")
)


zapis=str(diff)

with open("naszWynik2.txt", "w") as f:
    for word in zapis:
        f.writelines(zapis)
        f.write("\n")

