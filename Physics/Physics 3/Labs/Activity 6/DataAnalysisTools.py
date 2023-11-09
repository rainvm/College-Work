import numpy as np


def statisticalUncertainty(xdata):
    n = len(xdata)
    return np.sqrt((np.sum((xdata - np.mean(xdata)) ** 2)) / (n * n - 1))


def totalUncertainty(xdata, typeBUnc=0):
    return 2 * np.sqrt(statisticalUncertainty(xdata) ** 2 + typeBUnc ** 2)


def reportMeasurement(xdata, typeBUnc=0):
    return np.mean(xdata), totalUncertainty(xdata, typeBUnc)


def relativeUncertainty(xdata, typeBUnc=0):
    (x, dx) = reportMeasurement(xdata, typeBUnc)
    return dx / x


def discrepancy(xbest1, dx1, xbest2, dx2):
    delta = np.abs(xbest1 - xbest2)
    sig = dx1 + dx2
    return delta, sig, delta < sig


def combineMeasurement(xresults, dxresults):
    w = 1 / np.multiply(dxresults, dxresults)
    return ((np.sum(np.multiply(xresults, w))) / np.sum(w),
            1/np.sqrt(np.sum(w)))
