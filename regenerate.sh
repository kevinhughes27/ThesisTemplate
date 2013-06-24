# Build Thesis
pdflatex Thesis.tex

# Bibtex
bibtex Thesis

# Glossary
makeindex -s Thesis.ist -t Thesis.glg -o Thesis.gls Thesis.glo

# Nomenclature
makeindex Thesis.nlo -s nomencl.ist -o Thesis.nls

# Re-Build Thesis
pdflatex Thesis.tex
