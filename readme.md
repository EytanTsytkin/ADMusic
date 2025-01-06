Welcome.

In order to re-create the results using the original data only:
1. run data_preproccessing.py
2. enter leads.ipynb, run all.
3. enter attacks/funds_extraction.ipynb, run all.
4. enter attacks/phishing.ipynb, run all.
5. enter attacks/ato_and_theft.ipynb, run all.
6. enter poc.ipynb, run all.

This sequence should re-create all files, plots and results.

Requierments: 
json
numpy
pandas
matplotlib
seaborn
jupyter kernel

Additional files:
AnalysisPlayground.ipynb is my initial playground and is not requiered to recreate results.
commands.py contains common commands and combinations, for easy filtering.
related_sessions_finder.py contains several functions for fetching related sessions.
                           I ended up not using the weakly related sessions (same ip c class, same rare domain).
sensetivity_calcultor.py contains the functions used to calculte the sensetivity of each session,
                         given its' command, cookie & device age.