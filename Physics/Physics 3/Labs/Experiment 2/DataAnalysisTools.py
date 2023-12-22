import numpy as np


def statisticalUncertainty(xdata):
    n = len(xdata)
    return np.sqrt((np.sum((xdata - np.mean(xdata)) ** 2)) / (n * (n - 1)))


def totalUncertainty(xdata, typeBUnc=0):
    return 2 * np.sqrt(statisticalUncertainty(xdata) ** 2 + typeBUnc ** 2)


def reportMeasurement(xdata, typeBUnc=0):
    return np.mean(xdata), totalUncertainty(xdata, typeBUnc)


def relativeUncertainty(xdata, typeBUnc=0):
    (x, dx) = reportMeasurement(xdata, typeBUnc)
    return dx / x * 100


def discrepancy(xbest1, dx1, xbest2, dx2):
    delta = np.abs(xbest1 - xbest2)
    sig = dx1 + dx2
    return delta, sig, delta < sig


def combineMeasurement(xresults, dxresults):
    w = []
    mult = []
    for i in range(len(dxresults)):
        w.append(1 / (dxresults[i] ** 2))
        mult.append(xresults[i] * w[i])
    return ((np.sum(mult)) / np.sum(w),
            1 / np.sqrt(np.sum(w)))


def lineFit(x, y):
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean([i ** 2 for i in x])
    Exy = np.mean(np.multiply(x, y))
    return (Exy - (Ex * Ey)) / (Exx - (Ex ** 2)), ((Exx * Ey) - (Ex * Exy)) / (Exx - Ex ** 2)


def lineFitWt(x, y, dy):
    w = [1 / (dy[i] ** 2) for i in range(len(dy))]
    b = ((np.sum(np.multiply(w, [i ** 2 for i in x])) * np.sum(np.multiply(w, y))) - (
            np.sum(np.multiply(w, x)) * np.sum(np.multiply(np.multiply(w, x), y)))) / (
                np.sum(w) * np.sum(np.multiply(np.multiply(x, x), w)) - (np.sum(np.multiply(w, x))) ** 2)
    m = (np.sum(w) * np.sum(np.multiply(np.multiply(w, x), y)) - (np.sum(np.multiply(w, x)) * np.sum(
        np.multiply(w, y)))) / (np.sum(w) * np.sum(np.multiply(np.multiply(x, x), w)) - np.sum(np.multiply(w, x)) ** 2)
    dm = np.sqrt(np.sum(w) / (np.sum(w) * np.sum(np.multiply(np.multiply(x, x), w)) - (np.sum(np.multiply(w, x))) ** 2))
    db = np.sqrt(np.sum(np.multiply(np.multiply(x, x), w)) / (np.sum(w) * np.sum(np.multiply(np.multiply(x, x), w)) - (
        np.sum(np.multiply(w, x))) ** 2))
    return m, b, dm, db


def fitQuality(x, y, dy, m, b):
    n = len(y)
    total = 0
    for i in range(n):
        total += ((y[i] - m * x[i] - b) / dy[i]) ** 2
    return 1 / (n - 2) * total


def relativeError(measured, accepted):
    return np.abs((measured - accepted) / accepted)


def dataIntersectionPoint(x, y1, y2, x_unc = 0, y1_unc = 0, y2_unc = 0):
    idx = np.argwhere(np.diff(np.sign(y1 - y2)) != 0).flatten()
    xInt = []
    x_uncInt = []
    yInt = []
    y_uncInt = []
    for i in idx:
        xInt.append((x[i] + x[i+1])/2)
        x_uncInt.append((x_unc[i] + x_unc[i+1])/2)
        yInt.append((y1[i] + y1[i+1] + y2[i] + y2[i+1])/4)
        y_uncInt.append((y1_unc[i] + y1_unc[i+1] + y1_unc[i] + y1_unc[i+1])/4)
    return xInt, yInt, x_uncInt, y_uncInt
