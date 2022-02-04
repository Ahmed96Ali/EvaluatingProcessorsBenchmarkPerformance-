# test mode
tabletArray = [
    ['R', 'M', 'Z'],
    ['E', 'F', 'H', 'I', 'K'],
    [417, 83, 66, 39449, 772],
    [244, 70, 153, 35537, 368],
    [134, 70, 135, 66000, 396]
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
            normalizeTableArray[index] = [tableArray[indexOfArray][i] / tableArray[index][i] for i in
                                          range(len(tableArray[1]))]

    normalizeTableArray[indexOfArray] = normalizeRef
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
        arithmeticMeanArray.append(arrayTotal / len(tableArray[1]))

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

        geometericMeanArray.append(arrayTotal ** (1/len(tableArray[1])))

    return geometericMeanArray

def meansArray(tableArray, arth, geo):
    """
    :param tableArray:
    :param arth:
    :param geo:
    """

    tableArray[1].append("Arithmetic Mean")
    tableArray[1].append("Geometric Mean")

    for index in range(len(tableArray[0])):
        index = index + 2
        tableArray[index].append(arth[index-2])
        tableArray[index].append(geo[index-2])


def rankMean(arth, geo):
    """
    ranking the proccessor based on arthimetric and geometeric
    :param arth:
    :param geo:
    :return:
    """
    indexArith = 0
    indexGeo = 0
    MaxArth = max(arth)
    MaxGeo = max(geo)
    print("Using Arithmetic Mean, this is the ranking of the processors: ")
    for i in range(len(arth)):
        for i in range(len(arth)):
            """
            """





    print("Using Arithmetic Mean, this is the ranking of the processors: ")
    for item in geo:
        """
        """




def main():
    normalizedOfRef(tabletArray, 'R')
    arithmetric = calculateArithmeticMean(tabletArray)
    geometric = calculateGeometricMean(tabletArray)
    meansArray(tabletArray, arithmetric, geometric)
    tableDisplayer(tabletArray)

if __name__ == "__main__":
    main()