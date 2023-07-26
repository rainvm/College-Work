#import "typst-test\preamble\defs.typ": *
#sec("Introduction")
== Nonhomogeneous Linear Differential Equations
This text is concerned with the solutions to non-homogeneous linear differential equations, which have the form
$ bold(upright(L)) u = phi.alt, $
over an interval a $<=$ x $<=$ b and subject to certain boundary conditions, where *L* is an $n$th order linear ordinary differential operator and where the function $phi.alt$ is integrable on the given interval. #footnote[For *L* to be linear, it must satisfy the condition $ bold(upright(L))(alpha v + beta w) = alpha  v + beta bold(upright(L)) w $ arbitrary functions _v_ and _w_, with $alpha$ and $beta$ being constant.]
We begin by proving a theorem about such operators.