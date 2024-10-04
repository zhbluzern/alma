# Diverse Python scripts der ZHB Luzern / IZ RZS für Arbeiten rund um Alma.

Stand: Oktober 2024/heka

## get_network_id_from_mms_id.py

Für viele Metadaten-Massenupdates (Normalisierungsprozesse, Importprofile) braucht es die Alma Network ID (NZ ID), oft ist jedoch nur die MMS ID aus der IZ vorhanden. 
Dieses Python Script ermöglicht die Abfrage der NZ ID (alternativ der CZ ID) mittels Eingabe einer Excelliste mit einer Spalte von MMS ID.

Die Input-Datei muss mindestens eine Spalte namens "MMS ID" mit gültigen MMS ID der Institution Zone enthalten. 
Das Script ergänzt die Datei mit einer Spalte "Network ID" mit der entsprechenden NZ ID (oder bei Community zone records, die CZ ID). Wenn keine NZ oder CZ ID gefunden wird, bleibt die Spalte leer.
Der Name der Inputdatei muss angepasst werden bevor das Script läuft (Variable "input_file"). Die Inputdatei sollte im selben Verzeichnis liegen. 
Aufruf:

```
python get_network_id_from_mms_id.py
```

