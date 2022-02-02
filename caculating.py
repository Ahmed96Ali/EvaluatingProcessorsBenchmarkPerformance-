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

    normlize = [1 for i in range(len(tableArray[1]))]
    print(normlize)



def calculateArithmeticMean(tableArray):
    """
    :param tableArray:
    :return:
    """
def calculateGeometricMean(tableArray):
    """
    :param tableArray:
    :return:
    """




