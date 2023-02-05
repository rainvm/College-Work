my.knit = knitr::knit("Lab2.Rnw")
## document.tex is the latex file that will be compiled by the two following command:

system(paste0("pdflatex ", "Lab2.tex")) 
system(paste0("pdflatex ", "Lab2.tex")) 

