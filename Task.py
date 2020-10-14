'''
def count_strs():
  a = 1
  while a <= 3:
    n = 0
    with open(f"{a}.txt.txt", "r") as first:
      print(first.name)
      for strings in first:
        if strings.strip(" "):
          n = n + 1
        #print(f"{strings} - это {n} строка {a} файла")
      print(n)
    a = a + 1
count_strs()
'''

def count_strs():
    f1 = []
    f2 = []
    f3 = []
    n1 = 0
    n2 = 0
    n3 = 0
    with open(f"1.txt.txt", "r") as first:
        with open(f"2.txt.txt", "r") as second:
            with open(f"3.txt.txt", "r") as third:

                for strings in third:
                    if strings.strip(" "):
                        n3 = n3 + 1
                        f3.append(f"{strings} - {n3} строчка 3 файла")

            for strings in second:
                if strings.strip(" "):
                    n2 = n2 + 1
                    f2.append(f"{strings} - {n2} строчка 2 файла")

        for strings in first:
            if strings.strip(" "):
                n1 = n1 + 1
                f1.append(f"{strings} - {n1} строчка 1 файла")

    if n2 > n1 and n2 > n3:
        if n1 > n3:
            print(third.name, "\n", f3, "\n\n", first.name, "\n", f1, "\n\n", second.name, "\n", f2)
        else:
            print(first.name, "\n", f1, "\n\n", third.name, "\n", f3, "\n\n", second.name, "\n", f2)
    if n1 > n2 and n1 > n3:
        if n2 > n3:
            print(third.name, "\n", f3, "\n\n", second.name, "\n", f2, "\n\n", first.name, "\n", f1)
        else:
            print(second.name, "\n", f2, "\n\n", third.name, "\n", f3, "\n\n", first.name, "\n", f1)
    if n3 > n2 and n3 > n1:
        if n2 > n1:
            print(first.name, "\n", f1, "\n\n", second.name, "\n", f2, "\n\n", third.name, "\n", f3)
        else:
            print(second.name, "\n", f2, "\n\n", first.name, "\n", f1, "\n\n", third.name, "\n", f3)


count_strs()