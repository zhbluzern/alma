# Diverse Python scripts der ZHB Luzern / IZ RZS für Arbeiten rund um Alma.

Stand: Oktober 2024/heka

## get_network_id_from_mms_id.py

Für viele Metadaten-Massenupdates (Normalisierungsprozesse, Importprofile) braucht es die Alma Network ID (NZ ID), oft ist jedoch nur die MMS ID aus der IZ vorhanden. 
Dieses Script ermöglicht die Abfrage der NZ ID (alternativ der CZ ID) mittels Eingabe einer Excelliste mit einer Spalte von MMS ID.
