ThesisTemplate
==============

This the template I used for my Master's Thesis at Queen's University. 

Queen's provides a vanilla template here: http://www.cs.queensu.ca/sites/gradseries/help/doc_writing/thesistemplate/thesisTemplate.htm 

The original template has been modified by various students in the Queen's School of Computing, the latest prior to my modifications being available here: http://research.cs.queensu.ca/~andrew/

I made several modifications to the latest edition of the template and felt they were worth sharing. Most notably I re-worked the glossary a bit and made it part of the sty file rather than the main Thesis.tex file. I also added a notation page. I tried to re-comment and arrange the main Thesis.tex to better reflect how the pdf will be generated which I hope people newer to LaTeX will find more intuitive. Lastly I wrote a new build script called regenerate.sh which re-builds the entire thesis. This script builds the thesis and the rebuilds the glossary and the notation and then rebuilds the entire document again, alas with LaTeX this double pass build is neccessary.

I left an example of each of the basics (adding a figure, equation, notation etc.) in the background chapter for reference. Also in the figs folder is a sample of plotting with python and matplotlib which by the way I think everyone should at least consider using.

I compiled my Thesis on Linux Mint / Ubuntu using Texlive (which I've read is a lot faster than miktex fyi)
