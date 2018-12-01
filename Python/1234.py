while True:
    try:
        novaLinha = ""
        linha = input()

        maiuscula = True

        for l in linha:
            if l == ' ':
                novaLinha += ' '
                continue
            if maiuscula:
                novaLinha += l.upper()
                maiuscula = False
            else:
                novaLinha += l.lower()
                maiuscula = True
        print(novaLinha)
    except EOFError:
        break