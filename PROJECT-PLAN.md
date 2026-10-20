# Projektplan: Regenwürmer in Deutschland

## Idee und Lernziel

- **Das soll mein Projekt können:** Eine deutschsprachige Webseite zeigt nachgewiesene Regenwurm-Fundorte auf einer Deutschlandkarte. Eine Artenauswahl und kurze Steckbriefe erklären Unterschiede in Aussehen, Lebensweise und ökologischer Bedeutung.
- **Meine Themenschwerpunkte vom Vortag:** Python, SQL und Data Engineering; festgehalten in `README.md`.
- **Das möchte ich selbst festigen:** API-Abfragen, Listen und Dictionaries, Funktionen, JSON-Dateien, Fehlerbehandlung, relationale Tabellen, JOINs, Aggregationen und SQLite aus Python.
- **Kleinster funktionierender Kern:** Drei Arten, ein manuell erzeugter Datenstand, SQLite-Datenbank, JSON-Export und eine lokal funktionierende Webseite mit Karte, Artenauswahl und drei belegten Kurzporträts.
- **Technischer Ansatz:** Python → SQLite → JSON → Webseite aus HTML, CSS und JavaScript. Python bereitet die Daten vor; die Webseite benötigt keinen eigenen Anwendungsserver. Für die Karte wird Leaflet eingesetzt.
- **Startarten:** *Lumbricus terrestris*, *Lumbricus rubellus* und *Aporrectodea caliginosa*. Ihre aktuellen GBIF-Zuordnungen und verfügbaren Funddaten werden vor dem Import geprüft.

### Datenbasis und fachliche Grenzen

Die [verlinkte GBIF-Checkliste deutscher Regenwürmer](https://www.gbif.org/dataset/694de993-b8fb-4ec6-be05-268349510d67) dient als fachlicher Ausgangspunkt. Sie beruht auf einer Veröffentlichung von 2014 und enthält selbst keine kartierbaren Fundmeldungen. Die Koordinaten kommen aus weiteren GBIF-Datensätzen; Artenporträts benötigen ergänzende Fachquellen.

Die Karte zeigt **dokumentierte Nachweise**, keine vollständigen oder sicher aktuellen Verbreitungsgebiete. Fehlende Punkte bedeuten keine Abwesenheit. Datenstand, Quellen und Nutzungsbedingungen werden sichtbar angegeben.

## Meilensteine und Aufgabenverteilung

**Selbst:** durch Material_CTF vorbereitet; ich bearbeite die Aufgabe, Codex gibt bei Bedarf Hinweise und prüft meinen Lösungsweg.  
**Gemeinsam:** neue Anwendung bekannter Grundlagen; ich entwickle die Lösung mit gezielter Unterstützung.  
**Codex:** geht über die dokumentierten Kursgrundlagen hinaus; Codex sollte diesen abgegrenzten Teil nach Beauftragung übernehmen und verständlich erklären.

| Meilenstein / Ergebnis | Lernthema | Mein Anteil | Möglicher Codex-Anteil | Prüfung | Status / Beleg |
| --- | --- | --- | --- | --- | --- |
| **1. Daten für drei Arten verstehen:** GBIF-Namen und Kennungen, eine Beispielmeldung je Art sowie geeignete Quellen für Steckbriefe sind dokumentiert. | API, JSON, Datenverständnis und Quellenkritik | **Selbst:** Beispielabfragen ausführen; Artname, Datum, Koordinaten, Quelle und Lizenz untersuchen. | **Codex:** aktuelle Taxonomie, Synonyme und fachliche Quellen prüfen; Grenzen der Artenbestimmung erklären. | Ich kann die benötigten Felder erklären und für jede Art eine passende Fundmeldung zeigen. | offen |
| **2. Kleinen Datenabruf erstellen:** Python speichert zunächst eine Seite mit Fundmeldungen als unveränderte JSON-Datei. | Requests, Funktionen, Dateien, Exceptions | **Selbst:** Abruf, Speicherung und verständliche Fehlermeldungen schreiben. | **Gemeinsam:** Abfrageparameter, Zeitüberschreitung und HTTP-Fehler besprechen; meinen Code prüfen. | Die Datei lässt sich erneut einlesen; ein fehlgeschlagener Abruf meldet einen verständlichen Fehler. | offen |
| **3. SQLite-Datenbank aufbauen:** Arten und Fundmeldungen sind über Schlüssel verknüpft. | Tabellen, Datentypen, Primär- und Fremdschlüssel, Python-SQLite | **Selbst:** Schema und parametrisierten Import schreiben; Transaktionen verwenden. | **Gemeinsam:** Modell prüfen und bei der Zuordnung von GBIF-Namen unterstützen. | Ein JOIN zeigt Artname und Fundort; ein erneuter Import desselben Datensatzes erzeugt keine zusätzliche Zeile. | offen |
| **4. Verwendbaren Datenstand erzeugen:** Alle Ergebnisse der vereinbarten Abfragen werden seitenweise geladen, geprüft und ausgewertet. | Schleifen, Datenbereinigung, GROUP BY und COUNT | **Selbst:** Import erweitern, unbrauchbare Werte erkennen und SQL-Auswertungen schreiben. | **Gemeinsam:** GBIF-Seitennavigation und Abbruchbedingungen erarbeiten. **Codex:** fachliche Grenzfälle bei Taxonomie und Koordinaten beurteilen. | Importprotokoll nennt übernommene und verworfene Meldungen; SQL-Zählungen stimmen mit dem gespeicherten Bestand überein. | offen |
| **5. Daten für die Webseite exportieren:** Ein Python-Skript erzeugt JSON aus SQL-Abfragen; drei Kurzporträts liegen mit Quellen vor. | JOINs, JSON-Export und verständliche Datenaufbereitung | **Selbst:** Abfragen und Export schreiben; Porträts in eigenen Worten verfassen. | **Codex:** Exportstruktur für die Karte festlegen sowie Fachangaben und Quellen prüfen. | Export ist gültiges JSON; Fundzahlen stimmen mit SQLite überein; jedes Porträt enthält belegte Aussagen. | offen |
| **6. Lokale Webseite fertigstellen:** Karte, Artenauswahl, Funddetails, Porträts und Quellen funktionieren zusammen. | HTML/CSS und JavaScript-Ereignisse; neue Kartenintegration | **Selbst:** Texte, einfache Seitenstruktur und Gestaltung bearbeiten; bekannte DOM- und Ereignisgrundlagen anwenden. | **Codex:** Leaflet, Laden der JSON-Dateien, Marker und Kartenfilter integrieren; lokalen Start einrichten und erklären. | Artenwechsel zeigt passende Punkte und Porträts; Fundpunkte nennen Datum und Quelle; leere oder nicht ladbare Daten werden verständlich angezeigt. | offen |
| **7. Kern abschließen:** Der gesamte Ablauf ist reproduzierbar dokumentiert. | Fehlersuche, Dokumentation und Ergebnisprüfung | **Selbst:** Ablauf durchführen, Ergebnisse erklären und offene Grenzen dokumentieren. | **Codex:** gezielt Fehlerfälle und Integration prüfen; Startanleitung gegenlesen. | Vom gespeicherten Rohdatenstand lassen sich Datenbank und Webexport neu erzeugen; die Webseite startet nach Anleitung. | offen |

Status: **offen**, **in Arbeit** oder **geprüft**. „Geprüft“ benötigt ein beobachtetes Ergebnis mit Beleg, etwa eine SQL-Ausgabe oder einen dokumentierten Funktionstest.

Ein Planeintrag ist kein Umsetzungsauftrag. Meine Lernbereiche bearbeite ich selbst; Codex bietet die Übernahme abgegrenzter Aufgaben außerhalb dieser Bereiche an. Die Verteilung können wir gemeinsam anpassen.

## Festlegungen für den kleinen Kern

- Importiert werden deutsche Vorkommensnachweise der drei ausgewählten Arten mit Koordinaten, ohne von GBIF markierte geografische Probleme. Meldungen ohne ausreichende Artzuordnung werden ausgeschlossen.
- GBIF-Fundkennungen verhindern doppelte Importe derselben Meldung. Unterschiedliche Meldungen desselben Fundereignisses werden zunächst nicht automatisch zusammengeführt.
- Gespeichert werden Artzuordnung, Koordinaten, vorhandenes Funddatum, Koordinatenunsicherheit, Herkunft, Lizenz und Abrufdatum. Unbekannte Angaben bleiben als solche erkennbar.
- Steckbriefe vergleichen Größe, Färbung, Lebensraum, Lebensweise und ökologische Rolle, soweit verlässliche Quellen vorliegen. Im Kern werden keine Fotos benötigt.
- Die Webseite liest ausschließlich den exportierten Datenstand. Aktualisierungen werden bewusst manuell gestartet.
- Karte und Bibliotheken erhalten die erforderlichen Quellenangaben. Veröffentlichung und Hosting gehören zu einer späteren Erweiterung.

## Mögliche spätere Erweiterungen

| Erweiterung | Mein möglicher Lernanteil | Voraussichtlicher Codex-Anteil |
| --- | --- | --- |
| Weitere Regenwurmarten | Datenimporte, SQL-Auswertungen und Steckbriefe ergänzen | Taxonomie und fachliche Zuordnung prüfen |
| Filter nach Zeitraum und Datenquelle | SQL-Bedingungen und JavaScript-Ereignisse vertiefen | Komplexere Filter mit der Karte verbinden |
| Diagramme zu Fundmeldungen | Aggregationen und Interpretation erarbeiten | Diagrammbibliothek integrieren |
| Bilder und Artenvergleich | Inhalte recherchieren und Vergleichskriterien entwickeln | Bildlizenzen und Vergleichsansicht prüfen |
| Webseite veröffentlichen | Anleitung nachvollziehen und Veröffentlichung prüfen | Statisches Hosting einrichten |
| Automatische Aktualisierung | Importablauf und Protokolle verstehen | Zeitsteuerung, Wiederholungen und Überwachung einrichten |
| Boden- oder Landnutzungsdaten ergänzen | Zusätzliche Tabellen und JOINs entwickeln | Räumliche Verknüpfungen und fachliche Grenzen bearbeiten |

## Aktueller Schritt

- **Meilenstein und genau ein Arbeitsauftrag:** Meilenstein 1 – eine GBIF-Fundmeldung von *Lumbricus terrestris* aus Deutschland abrufen und die Felder für Artname, Datum, Koordinaten, Quelle und Lizenz erläutern.
- **Wer bearbeitet ihn?** Ich selbst; Codex unterstützt bei Verständnisfragen.
- **So prüfen wir das Ergebnis:** Die Antwort liegt vor und ich kann die genannten Felder sowie fehlende Angaben erklären.
- **Bisheriges Ergebnis / offene Schwierigkeit:** Die grundsätzliche Datenverfügbarkeit wurde geprüft. Projektcode und Webseite sind noch nicht erstellt.

Nach Unterbrechungen werden Plan und Projektstand verglichen. Erst nach erfolgreicher Prüfung wird der nächste Meilenstein begonnen; Änderungen an Umfang und Aufgabenverteilung werden gemeinsam festgehalten.
