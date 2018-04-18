# Librairies importées
import pandas
import csv
import Setup_Scripts.Config as Config

# Variables globales
FILE_TEST = Config.TEST_FILE
file = open(FILE_TEST, 'r')
counter = csv.reader(file)
NB_COL_TEST = len(next(counter))
NB_ROW_TEST = sum(1 for row in counter)
file.close()
FILE_TRAIN = Config.TRAIN_PATH_PRICE_RANGE
file = open(FILE_TRAIN, 'r')
counter = csv.reader(file)
NB_COL_TRAIN = len(next(counter))
NB_ROW_TRAIN = sum(1 for row in counter)
file.close()
nb_col = NB_COL_TEST - 2


def headId(id):
    headers = []
    with open(FILE_TEST, 'r') as fileTest:
        reader = csv.reader(fileTest)
        data = [r for r in reader]
        headers = data[0]
    fileTest.close()
    headers = headers[:len(headers)-2]
    return headers[id]


def maisonId(id):
    maison = []
    with open(FILE_TEST, 'r') as fileTest:
        reader = csv.reader(fileTest)
        data = [r for r in reader]
        for index in range(0, NB_ROW_TEST):
            maison = data[index]
            index += 1
    fileTest.close()
    return maison


def attMoy(sim, col):
    sim = sum(sim)/len(col)
    sim = (len(col)/nb_col)*sim
    return sim


def attIndex(listHeaders):
    headers = []
    with open(FILE_TEST, 'r') as fileTest:
        reader = csv.reader(fileTest)
        data = [r for r in reader]
        headers = data[0]
    fileTest.close()
    headers = headers[:len(headers)-2]
    temp = []
    for index in range(0, nb_col):
        try:
            if headers[index] in listHeaders:
                temp.append(index)
        except IndexError:
            print(f"error with index {index}")
        index += 1
    return temp


def similarity(houseTest, houseTrain):
    # Variables locales
    simil = []

    # Catégoriser les headers
    AllOrNone = ['Street', 'Alley', 'Neighborhood', 'Condition1', 'Condition2', 'RoofStyle',
                 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Foundation',
                 'Heating', 'LotConfig', 'BldgType', 'CentralAir', 'GarageType', 'PavedDrive',
                 'MiscFeature', 'SaleType', 'SaleCondition', 'LowQualFinSF', 'PoolArea']
    colAON = attIndex(AllOrNone)
    QualCond = ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'HeatingQC', 'KitchenQual',
                'FireplaceQu', 'GarageQual', 'GarageCond', 'PoolQC']
    colQC = attIndex(QualCond)
    Range = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF',
             'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageArea', 'WoodDeckSF',
             'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'MiscVal']
    colR = attIndex(Range)
    Maxima = ['OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'BsmtFullBath',
              'BsmtHalfBath', 'FullBath', 'HalfBath','Bedroom', 'Kitchen', 'TotRmsAbvGrd',
              'Fireplaces', 'GarageYrBlt', 'GarageCars']
    colM = attIndex(Maxima)
    Others = ['MSSubClass', 'MSZoning', 'LotShape', 'LandContour', 'Utilities',
             'LandSlope', 'HouseStyle', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
             'Electrical', 'Functional', 'GarageFinish', 'Fence']
    Others.extend(['MoSold', 'YrSold'])
    colO = attIndex(Others)

    # Trouver la similarité entre les deux maisons en entrée

    # Calculez la similarité des attributs AllOrNone
    simAON = []
    for index in range(0, nb_col):
        try:
            if index in colAON:
                if houseTest[index] == houseTrain[index]:
                    simAON.append(1)
        except IndexError:
            print(f"error with index {index}")
        index += 1
    # simil.append(attMoy(simAON, colAON))

    # Calculez la similarité des attributs QualCond
    qcText = ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA']
    qcVal = [1, 4/5, 4/5, 3/5, 2/5, 1/5, 0]
    simQC = []
    for index in range(0, nb_col):
        try:
            if index in colQC:
                tempTest = qcVal[qcText.index(houseTest[index])]
                tempTrain = qcVal[qcText.index(houseTrain[index])]
                temp = 1 - abs(tempTest - tempTrain)
                simQC.append(temp)
        except IndexError:
            print(f"error with index {index}")
        index += 1
    simil.append(attMoy(simQC, colQC))

    # Calculez la similarité des attributs Range
    simR = []
    for index in range(0, nb_col):
        try:
            if index in colR:
                if houseTest[index] == houseTrain[index]:
                    simR.append(1)
        except IndexError:
            print(f"error with index {index}")
        index += 1
    simil.append(attMoy(simR, colR))

    # Calculez la similarité des attributs Maxima
    mList = pandas.read_csv(FILE_TEST)
    simM = []
    for index in range(0, nb_col):
        try:
            if index in colM:
                tempMin = float(min(mList[headId(index)]))
                tempMax = float(max(mList[headId(index)]))
                simM.append((float(houseTest[index]) - tempMin)/(tempMax - tempMin))
        except IndexError:
            print(f"error with index {index}")
        index += 1
    simil.append(attMoy(simM, colM))

    # Calculez la similarité des attributs Others
    simO = []
    for index in range(0, nb_col):
        try:
            if index in colO:
                if houseTest[index] == houseTrain[index]:
                    simO.append(1)
        except IndexError:
            print(f"error with index {index}")
        index += 1
    simil.append(attMoy(simO, colO))

    simTotal = sum(simil)
    return simTotal


def pricing(id, classe):
    # Variables locales
    id = str(id)

    # Trouver la maison avec l'id donné dans FILE_TEST.
    print(f"{id} -> {classe}")
    maison = maisonId(id)
    maison.pop()

    # Filtrer FILE_TRAIN pour garder seulement la classe de maison,
    #   puis calculer la similarité une à la fois en écrasant price
    #   avec la valeur d'une maison ayant une plus grande similarité
    simil = 0
    price = 0
    with open(FILE_TRAIN, 'r') as fileTrain:
        reader = csv.reader(fileTrain)
        data = [r for r in reader]
        for index in range(0, NB_ROW_TRAIN):
            try:
                if data[index][-2] == classe:
                    temp = similarity(maison[:len(maison)-1], data[index][:len(data[index])-2])
                    if temp > simil:
                        simil = temp
                        try:
                            price = float(int(data[index][-1]))
                        except ValueError:
                            pass
                    elif temp == simil:
                        # Calcul de la moyenne de la moyenne au lieu de la vrai moyenne
                        price = float((price + int(data[index][-1]))/2)
            except IndexError:
                print(f"error with index {index}")
            index += 1
    fileTrain.close()
    print('SalePrice : ' + str(price) + '\n')
    return str(price)
