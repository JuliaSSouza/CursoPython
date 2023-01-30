from statistics import median


def calcular_media(p):

    media = 0

    for i in range(0, len(p)):

        media =+ p[i]

    media = media/len(p)

    return media


m = calcular_media([5, 5, 10])
print(m)