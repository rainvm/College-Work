import DataAnalysisTools as dat


def main(name):
    xdata1 = [72.2, 77.6, 82.4, 86.3, 88.9]
    xdata2 = [80.1, 81.45, 81.5, 81.34, 82.01]
    xbest1, dx1 = dat.reportMeasurement(xdata1, 0.3)
    print(f"Length 1: ({xbest1:.1f} ± {dx1:.1f}) cm")
    xbest2, dx2 = dat.reportMeasurement(xdata2, 0.05)
    print(f"Length 2: ({xbest2:.2f} ± {dx2:.2f}) cm")
    print("Relative Uncertainty 1: {:.3f}".format(dat.relativeUncertainty(xdata1, 0.3)))
    print("Relative Uncertainty 2: {:.3f}".format(dat.relativeUncertainty(xdata2, 0.05)))



if __name__ == '__main__':
    main('PyCharm')
