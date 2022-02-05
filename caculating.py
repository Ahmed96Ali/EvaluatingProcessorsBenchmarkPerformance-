# test mode
tabletArray = [
    ['R', 'M', 'Z'],
    ['E', 'F', 'H', 'I', 'K'],
    [417, 83, 66, 39449, 772],
    [244, 70, 153, 35537, 368],
    [134, 70, 135, 66000, 369]
]


def tableDisplayer(tableArray):
    """
    this func is used to display table of required data
    :param tableArray:
    """
    print("{:>27}".format('Processor'))
    print("{:<15}".format('Benchmark'), end=""),
    for item in tabletArray[0]:
        print("{:<15}".format(item), end="")
    print('\n')
    i = 2
    for item in range(len(tableArray[1])):
        print("{:<15}".format(tableArray[1][item]), end="")
        for dataInsider in range(len(tableArray[0])):
            print("{:<15}".format(tableArray[i][item]), end="")
            i += 1
        print('\n')
        i = 2


def normalizedOfRef(tableArray, ref):
    """
    function is used to normalize data
    :param tableArray: array of data
    :param ref: reference
    :return: normalized array
    """
    ref = tableArray[0].index(ref)
    indexOfArray = ref + 2
    normalizeRef = [1 for i in range(len(tableArray[1]))]
    normalizeTableArray = tableArray

    for index in range(len(tabletArray[0])):
        index = index + 2
        if index == indexOfArray:
            continue
        else:
            normalizeTableArray[index] = [round(tableArray[indexOfArray][i] / tableArray[index][i], 3) for i in
                                          range(len(tableArray[1]))]

    normalizeTableArray[indexOfArray] = normalizeRef
    for i, item in enumerate(normalizeTableArray[1]):
        normalizeTableArray[1][i] = f"r{item}"
    return normalizeTableArray


def calculateArithmeticMean(tableArray):
    """
    :param tableArray:
    :return: array of arithemtic mean
    """

    arithmeticMeanArray = []

    for index in range(len(tableArray[0])):
        index = index + 2
        arrayTotal = 0
        for item in tableArray[index]:
            arrayTotal += item
        arithmeticMeanArray.append(round(arrayTotal / len(tableArray[1]), 3))

    return arithmeticMeanArray


def calculateGeometricMean(tableArray):
    """
    :param tableArray:
    :return: array of gemoteric mean
    """
    geometericMeanArray = []
    for index in range(len(tableArray[0])):
        index = index + 2
        arrayTotal = 1
        for item in tableArray[index]:
            arrayTotal *= item

        geometericMeanArray.append(round(arrayTotal ** (1 / len(tableArray[1])), 3))

    return geometericMeanArray


def meansArray(tableArray, arth, geo):
    """
    :param tableArray:
    :param arth:
    :param geo:
    """

    tableArray[1].append("AM")
    tableArray[1].append("GM")

    for index in range(len(tableArray[0])):
        index = index + 2
        tableArray[index].append(arth[index - 2])
        tableArray[index].append(geo[index - 2])


def sortMean(arth, geo):
    """
    sort the proccessor based on arthimetric and geometeric
    :param arth:
    :param geo:
    :return:
    """
    arrayArith = []
    arrayGeo = []
    sortedArth = arth.copy()
    sortedGeo = geo.copy()
    sortedArth.sort(reverse=True)
    sortedGeo.sort(reverse=True)
    for i in range(len(arth)):
        for j in range(len(arth)):
            if sortedArth[i] == arth[j]:
                arrayArith.append(j)
                continue

    for i in range(len(geo)):
        for j in range(len(geo)):
            if sortedGeo[i] == geo[j]:
                arrayGeo.append(j)
                continue

    return [arrayArith, arrayGeo]


def rankMean(tableArray, arraySortted):
    """
    :param tableArray:
    :param arraySortted:
    :return:
    """
    print("Using Arithmetic Mean, this is the ranking of the processors: ")
    for i, item in enumerate(arraySortted[0]):
        i += 1
        print(f"{i}. {tableArray[0][item]}")

    print("Using Geometric Mean, this is the ranking of the processors: ")
    for i, item in enumerate(arraySortted[1]):
        i += 1
        print(f"{i}. {tableArray[0][item]}")


def main():
    tableDisplayer(tabletArray)
    normalizedOfRef(tabletArray, input("Please identify the reference processor: "))
    arithmetric = calculateArithmeticMean(tabletArray)
    geometric = calculateGeometricMean(tabletArray)
    meansArray(tabletArray, arithmetric, geometric)
    tableDisplayer(tabletArray)
    rankMean(tabletArray, sortMean(arithmetric, geometric))


if __name__ == "__main__":
    main()
