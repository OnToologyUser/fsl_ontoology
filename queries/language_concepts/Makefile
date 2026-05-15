all:
	make concepts.run
	make instances.run
	make subclasses.run
	make used_instances.run
	make used_subclasses.run
	make properties.run
	make software_languages.run
	make programming_languages.run
	python3 summary.py

summary.csv: *.log summary.py
	python3 summary.py

%.run:
	python3 $*.py > $*.log

clean:
	rm -f *.log *.csv
