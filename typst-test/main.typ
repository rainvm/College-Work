#set page(paper: "us-letter", margin: (x: 0.75in, y: 0.75in), numbering: "1")
#set par(leading: 0.55em, first-line-indent: 0em, justify: true)
#set footnote.entry(indent: 0em)
#set text(font: "New Computer Modern", size: 12pt)
#show raw: set text(font: "New Computer Modern Mono")
#show par: set block(spacing: 0.55em)
#show heading: set block(above: 1.4em, below: 1em)
#set heading(numbering: "1.1  ")
#set outline(indent: auto)

// #show: content => locate(loc => [
//     #set math.equation(
//         numbering: (..nums) => ounter(heading)
//         .display()
//     )
// ])
#let s = state("s", 1)
#let head_level(head) = {
    x
}

#set math.equation(numbering: (..nums)=> counter(heading).display(bottom)
)

#outline()

= Introduction
== Nonhomogeneous Linear Differential Equations
This text isd concerned with the solutions to non-homogeneous linear differential equations, which have the form
$ bold(upright(L)) u = phi.alt, $
over an interval a $<=$ x $<=$ b and subject to certain boundary conditions, where *L* is an $n$th order linear ordinary differential operator and where the function $phi.alt$ is integrable on the given interval. #footnote[For *L* to be linear, it must satisfy the condition $ bold(upright(L))(alpha v + beta w) = alpha  v + beta bold(upright(L)) w $ arbitrary functions _v_ and _w_, with $alpha$ and $beta$ being constant.]
We begin by proving a theorem about such operators.

= test
// \begin{theorem}
// 	\(\L\) is linear if and only if it is of the form
// 	\begin{equation} 
// 		\L = a_n(x) \frac{d^n}{dx^n} + a_{n-1}(x) \frac{d^{n-1}}{dx^{n-1}} + \cdots + a_0(x).
// 	\end{equation}
// \end{theorem}

// \begin{proof}\(\impliedby\)\\
// 	We prove, by induction, that \(\D^{k}\) is a linear differential operator for all \(k \in \mathbb{N}\). Note: \(f^{(k)}=\D^{k}f\)\\
// 	\textbf{Base Step} Let \(k=1\).\\
// 	\begin{equation*}
// 		\begin{split}
// 			\D (\a u(x) + \b v(x)) &= \lim_{h\to 0} \frac{\a u(x+h) + \b v(x+h)-(\a u(x) + \b v(x))}{h}\\
// 			&=\a \frac{u(x+h) - u(x)}{h} + \b \frac{v(x+h)-v(x)}{h}\\
// 			&= \a \D u + \b \D v
// 		\end{split}
// 	\end{equation*}
// 	\textbf{Induction Step} Suppose that the statement holds for some \(k\in\mathbb{N}\), \(k>1\). Then,
// 	\begin{equation*}
// 		\begin{split}
// 			\D^{k+1} (\a u + \b v) &= \D ( \D^{k}(\a u + \b v))\\
// 			&=\D(\a \D^{k} u + \b \D^{k} v)\\
// 			&=\a \D(\D^{k} u) + \b \D (\D^{k} v)\\
// 			&= \a \D^{k+1} u + \b \D^{k+1} v
// 		\end{split}
// 	\end{equation*}
// 	It follows that 
// 	\begin{equation*}
// 		\sum_{k=0}^{n} a_k(x) D^{k}
// 	\end{equation*}
// 	is also linear because \(a_k(x) D^{k}\) is linear and a sum of linear operators is linear.\\
// 	\(\implies\)\\
// 	Let
// 	\begin{equation*}
// 		\begin{split}
// 			\L u &= f(x, \underbrace{u, u', u'', \dots, u^{(n)}}_\u)\\
// 			&=f(x, \u).
// 		\end{split}
// 	\end{equation*}
// 	Then,
// 	\begin{equation*}
// 		\L (\a v + \b w) = f(x, \a \textbf{v} + \b \textbf{w})
// 	\end{equation*}
// 	and
// 	\begin{equation*}
// 		\a \L v + \b \L w = \a f(x,\textbf{v}) + \b f(x,\textbf{w}).
// 	\end{equation*}
// 	If \(\L\) is linear then 
// 	\begin{equation*}
// 			\L(\a v + \b w) = \a \L v + \b \L w\
// 	\end{equation*}
// 	or
// 	\begin{equation*}
// 		f(x,\a \textbf{v} + \b \textbf{w})= \a f(x, \textbf{v}) + \b f(x, \textbf{u})
// 	\end{equation*}
// 	It follows that 
// 	\begin{equation*}
// 		f(x, \u + \epsilon \v) = f(x, \u) + \epsilon f(x, \v)
// 	\end{equation*}
// 	or
// 	\begin{equation*}
// 		\frac{f(x, \u + \epsilon \v)-f(x,\u)}{\epsilon} = f(x,\v).
// 	\end{equation*}
// 	Next, we take the limit as \(\epsilon \to 0\),
// 	\begin{equation}\label{eq:dirDiv}
// 		\begin{split}
// 			\lim_{\epsilon \to 0}\frac{f(x, \u + \epsilon \v )-f(x,\u )}{\epsilon} &= \D_\v f(x,\u)\\
// 			&= \v \cdot \nabla f(x,\u)\\
// 			&= f(x,\v),
// 		\end{split}
// 	\end{equation}
// 	where \(\D=\langle \frac{\partial}{\partial u}, \frac{\partial}{\partial u'}, \dots, \frac{\partial^(n)}{\partial u^{(n)}\rangle} \)
// 	Let 
// 	\begin{equation*}
// 		\u = \v = \langle 0, \dots, u^{(i)}, 0, \dots, 0 \rangle
// 	\end{equation*}
// 	and
// 	\begin{equation*}
// 		f(x,u^{(i)}) = f(x, \langle 0, \dots, u^{(i)}, 0, \dots, 0 \rangle ).
// 	\end{equation*}
// 	Then it follows from equation (\ref{eq:dirDiv}) that,
// 	\begin{equation*}
// 		u^{(i)}\frac{\partial f(x, u^{(i)})}{\partial u^{(i)}} = f(x,u^{(i)}).
// 	\end{equation*}
// 	We solve this equation with separation of variables, 
// 	\begin{equation*}
// 		\begin{split}
// 			\frac{\partial f(x, u^{(i)})}{f(x,u^{(i)})} &= \frac{\partial u^{(i)}}{u^{(i)}}\\
// 			\int\frac{\partial f(x, u^{(i)})}{f(x,u^{(i)})} &= \int \frac{\partial u^{(i)}}{u^{(i)}}\\
// 		\end{split}
// 	\end{equation*}
// 	Thus, 
// 	\begin{equation*}
// 		f(x,u^{(i)}) = a_i(x)u^{(i)}
// 	\end{equation*} 
// 	and so 
// 	\begin{equation*}
// 		\begin{split}
// 			f(x,\u) &= f(x, \sum_i \langle 0, 0, \dots, u^{(i)}, \dots, 0, 0 \rangle)\\
// 			&=\sum_i f(x,u^{(i)}) \\
// 			&= \sum_i a_i(x)u^{(i)}(x)\\
// 			&= \left[a_n(x) \frac{d^n}{dx^n} + a_{n-1}(x) \frac{d^{n-1}}{dx^{n-1}} + \cdots + a_0(x)\right]u.
// 		\end{split}
// 	\end{equation*}
// \end{proof}

// 	Since \(\L\) is of order \(n\), there will be \(n\) boundary conditions of the general form 
// \begin{equation}
// 	\mathbf{B}_j (u) = c_j;\quad j=1,2,\dots,n,
// \end{equation}
// where the \(\mathbf{B}_j\)'s are prescribed functionals \footnote{A \df{functional} is a transformation with a set of functions as its domain and a set of numbers as its range. To illustrate, consider the functional 
// \begin{equation}
// 	\mathcal{F}(u) = \int_{0}^{1} u^2(x)dx.
// \end{equation}
// The domain of this functional might be the set of functions defined over the interval \([0,1]\) and for which the integral of \(u^2\) from 0 to 1 exists. The range is \([0, \infty)\).
// } and \(c_j\)'s are prescribed constants. We will only consider \(\mathbf{B}_j\)'s that are linear combinations of \(u\) and its derivatives through order \(n-1\) and evaluated at the endpoints, a and b. 

// For \(\mathbf{B}_j\) to be \df{linear}, it must satisfy the condition
// \begin{equation}
// 	\mathbf{B}_j(\alpha v + \beta w) = \alpha \mathbf{B}_j (v) + \beta \mathbf{B}_j(w).
// \end{equation}