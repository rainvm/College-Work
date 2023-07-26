#set page(paper: "us-letter", margin: (x: 0.75in, y: 0.75in), numbering: "1")
#set par(leading: 0.55em, first-line-indent: 0em, justify: true)
#set footnote.entry(indent: 0em)
#set text(font: "New Computer Modern", size: 12pt)
#show raw: set text(font: "New Computer Modern Mono")
#show par: set block(spacing: 0.55em)
#show heading: set block(above: 1.4em, below: 1em)
#set heading(numbering: "1.1  ")
#set outline(indent: auto)

#let sec_state = state("s", 0)
#let eq_state = state("e", 0)
#let th_state = state("t", 0)

#let sec(title) = block[
    #sec_state.update(s =>
        eval(str(s) + "+ 1")
    )
    = #title 
    #eq_state.update("0")
]

#let eq(nums) = {
    show: content => [  
        #eq_state.update(e => 
            eval(str(e) + "+ 1")
        )
        (#sec_state.display().#eq_state.display())
    ]
    nums
}

#let neq(body) = math.equation(block: true, numbering: (..nums) => eq(nums), body)

#let theorem_counter = counter("theorem")
#let theorem(body) = block[
    #th_state.update(t =>
        eval(str(t) + "+ 1")
    )
    *Theorem #sec_state.display().#th_state.display()* _ #body _
]