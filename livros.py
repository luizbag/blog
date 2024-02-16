with open("livros.csv", mode="r", encoding="utf-8") as f:
    data = [tuple(line.strip().split(';')) for line in f.readlines()]

for titulo, autor in data:
    fileName = "_".join(titulo.replace(':','').replace('"', '').replace(',','').split()) + ".md"
    with open("_leituras/" + fileName, mode="w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: page\n")
        f.write("title: " + titulo + "\n")
        f.write("autor: " + autor + "\n")
        f.write("status: lido\n")
        f.write("revisado: false\n")
        f.write("---\n")
    