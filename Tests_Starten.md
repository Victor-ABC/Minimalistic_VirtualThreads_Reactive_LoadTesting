### Für alle 3 Microservices
 - Bauen mit Maven
 - Erzeugen eines Docker images (1. Befehl im Dockerfile)
 - Starten eines Docker images (2. Befehl im Dockerfile)

### (4.) im Batch-File
 - Es können die VUs angepasst werden
 - wenn die "Schrittlänge" verändert wird (z.B. von 100 bis 1000 in 100er oder 200er schritten), muss in der Analysis.py Datei an 2 Stellen
   der Wert angepasst werden.
 - Doppelklick auf die batch datei. (Für Macos/Linux: sh ./run.sh)

### Wenn ein weiterer Test durchgeführt soll, müssen die generierten output-Dateien im K6 Ordner gelöscht werden
- output/analysis/final_metrics.csv
- output/k6/summary_*.json
- output/resources/metric_output_*.csv

