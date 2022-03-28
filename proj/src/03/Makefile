LATEX = latexmk

default: pdf

.PHONY:

clean:
	${LATEX} -c
	rm -f *.vtc

veryclean: clean
	${LATEX} -C

pdf:
	${LATEX} -pdf

pdf-watcher:
	${LATEX} -pvc -pdf
