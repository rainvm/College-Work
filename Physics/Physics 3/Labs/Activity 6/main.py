import numpy as np
import plotly.graph_objects as go
import plotly.express as ex

import DataAnalysisTools as dat


def main():
    problem4()


def problem4():
    f = open("Ass3_Data.txt")
    data = [i.split(",") for i in np.array(f.read().split("\n"))]
    r, dr, i, di = ([float(j[0]) for j in data], [float(j[1]) for j in data], [float(j[2]) for j in data],
                    [float(j[3]) for j in data])
    v = np.multiply(r, i)
    dv = np.abs(v)*np.sqrt(np.square(np.divide(di, i)) + np.square(np.divide(dr, r)))
    m, b, dm, db = dat.lineFitWt(r, v, dv)
    rfit = np.linspace(100, 11000000, 100000)
    vfit = m*rfit + b
    fig = go.Figure(data=[
        go.Scatter(x=r, y=v, line=dict(width=0), error_y=dict(
            type='data',
            array=dv,
            visible=True
        )),
        go.Scatter(x=rfit, y=vfit)
    ])
    q = dat.fitQuality(r, v, dv, m, b)
    print(f"Q = {q}")
    fig.show()


def problem3():
    f = open("data.txt")
    data = [i.split() for i in np.array(f.read().split("\n"))]
    t = []
    v = []
    dv = []
    for i in data:
        t.append(float(i[0]))
        v.append(float(i[1]))
        dv.append(float(i[2]))
    m, b = dat.lineFit(t, v)
    tfit = np.linspace(2, 24, 10000)
    fit = m*tfit+b
    mw, bw, dmw, dbw = dat.lineFitWt(t, v, dv)
    fitw = mw*tfit+bw
    q = dat.fitQuality(t, v, dv, m, b)
    qw = dat.fitQuality(t, v, dv, mw, bw)
    fig = go.Figure(
        data=[
            go.Scatter(
                x=t, y=v,
                error_y=dict(
                    type='data',
                    array=dv,
                    visible=True
                ),
                line=dict(width=0)
            ),
            go.Scatter(x=tfit, y=fit),
            go.Scatter(x=tfit, y=fitw)

        ]
    )
    fig.show()

    print(f"lineFit: m={m}, b={b}, q={q}")
    print(f"lineFitWt: m={mw} b={bw}, q={qw}")
    print(f"m_w ± dm_w = ({mw:.2f} ± {dmw:.2f})")
    print(f"b_w ± db_w = ({bw:.2f} ± {dbw:.2f})")


def problem2():
    f = open("millikan.txt")
    data = [i.split() for i in np.array(f.read().split("\n"))]
    x = []
    y = []
    for i in data:
        x.append(float(i[0]))
        y.append(float(i[1]))
    m, b = dat.lineFit(x, y)
    x1 = np.linspace(10 ** 14, 1.5 * 10 ** 15, 10000)
    fig = go.Figure(data=[
        go.Scatter(x=x, y=y, line=go.scatter.Line(width=0)),
        go.Scatter(x=x1, y=([m * i + b for i in x1]))
    ])
    fig.show()
    e = 1.602176634e-19
    h = m * e
    print(f"Measured Planck Constant: {h}")
    print(f"Relative Error: {dat.relativeError(h, 6.62607015e-34) * 100:.2f}%")


def problem1():
    xdata1 = [72.2, 77.6, 82.4, 86.3, 88.9]
    xdata2 = [80.1, 81.45, 81.5, 81.34, 82.01]
    xbest1, dx1 = dat.reportMeasurement(xdata1, 0.3)
    print(f"Length 1: ({xbest1:.1f} ± {dx1:.1f}) cm")
    xbest2, dx2 = dat.reportMeasurement(xdata2, 0.05)
    print(f"Length 2: ({xbest2:.2f} ± {dx2:.2f}) cm")
    print("Relative Uncertainty 1: {:.1f}%".format(dat.relativeUncertainty(xdata1, 0.3)))
    print("Relative Uncertainty 2: {:.1f}%".format(dat.relativeUncertainty(xdata2, 0.05)))
    if dat.discrepancy(xbest1, dx1, xbest2, dx2)[2]:
        print("The measurements agree.")
    else:
        print("The measurements do not agree.")
    xbest, dx = dat.combineMeasurement([xbest1, xbest2], [dx1, dx2])
    print(f"The combined measurement is ({xbest:.1f} ± {dx:.1f}) cm")


if __name__ == '__main__':
    main()
