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
| **1. Daten für drei Arten verstehen:** GBIF-Namen und Kennungen, eine Beispielmeldung je Art sowie geeignete Quellen für Steckbriefe sind dokumentiert. | API, JSON, Datenverständnis und Quellenkritik | **Selbst:** Beispielabfragen ausführen; Artname, Datum, Koordinaten, Quelle und Lizenz untersuchen. | **Codex:** aktuelle Taxonomie, Synonyme und fachliche Quellen prüfen; Grenzen der Artenbestimmung erklären. | Ich kann die benötigten Felder erklären und für jede Art eine passende Fundmeldung zeigen. | geprüft – abgeschlossen am 21.10.2026; fachliche Vorbereitung sowie eigene Beispielmeldungen und Felderklärungen geprüft, Belege unten |
| **2. Kleinen Datenabruf erstellen:** Python speichert zunächst eine Seite mit Fundmeldungen als unveränderte JSON-Datei. | Requests, Funktionen, Dateien, Exceptions | **Selbst:** Abruf, Speicherung und verständliche Fehlermeldungen schreiben. | **Gemeinsam:** Abfrageparameter, Zeitüberschreitung und HTTP-Fehler besprechen; meinen Code prüfen. | Die Datei lässt sich erneut einlesen; ein fehlgeschlagener Abruf meldet einen verständlichen Fehler. | geprüft – abgeschlossen am 22.10.2026; Abruf, Speicherung, separates Einlesen und drei Fehlerfälle bestanden; Belege unter „Abschluss von Meilenstein 2“ |
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

- **Meilenstein und genau ein Arbeitsauftrag:** Übergang zu Meilenstein 3 – Datenmodell entwerfen. Ich schlage selbst zwei Tabellen für Arten und Fundmeldungen mit ihren wichtigsten Spalten vor, zunächst ohne SQL-Code. Meilenstein 3 bleibt bis zum Beginn meiner Bearbeitung offen.
- **Wer bearbeitet ihn?** Ich selbst; Codex unterstützt bei Verständnisfragen.
- **So prüfen wir das nächste Ergebnis:** Mein Tabellenentwurf zeigt die Verknüpfung einer Fundmeldung mit ihrer Art und das Feld, das doppelte GBIF-Fundmeldungen verhindern kann.
- **Bisheriges Ergebnis / offene Schwierigkeit:** Meilensteine 1 und 2 sind abgeschlossen; ihre Belege und Prüfgrenzen sind dokumentiert. Für Meilenstein 3 liegt noch kein Tabellenentwurf vor. Eine Webseite ist noch nicht erstellt.

### Abschluss von Meilenstein 2

**Geprüft – abgeschlossen am 22.10.2026.** Die folgenden Ausführungsergebnisse
wurden von mir im Chat übermittelt und von Codex zusammen mit meinen Erklärungen
und dem im Verlauf gelesenen Code geprüft. Codex hat die Netzwerk- und Fehlerfalltests
nicht selbst ausgeführt.

- **Abruf, Speicherung und Einlesen:** Nach Wiederherstellung der ursprünglichen GBIF-URL und `timeout=10` gab `python3 regenwurm.py` den Statuscode `200` und `Lumbricus terrestris Linnaeus, 1758` aus. Anschließend gab `python3 regenwurm_json_einlesen.py` denselben Namen aus der gespeicherten Datei aus, ohne erneuten API-Abruf.
- **Erklärung:** Ich habe erklärt, dass `json.dump()` Daten als JSON in eine Datei schreibt und `json.load()` JSON aus einer Datei einliest.
- **Verbindungsfehler:** Der Test mit `https://unsinn` führte zu einem Fehler bei der Namensauflösung und zur abgefangenen Meldung `Verbindungsfehler: …`.
- **HTTP-Fehler:** Ein nicht vorhandener GBIF-Endpunkt führte zu `HTTP-Fehler: 404 Client Error: Not Found …`. `response.raise_for_status()` steht direkt nach dem Abruf und vor der Verarbeitung und Speicherung.
- **Timeout:** Ein sehr kleiner positiver Timeout löste eine Zeitüberschreitung beim Verbindungsaufbau aus. Nachdem der `Timeout`-Zweig vor den `ConnectionError`-Zweig verschoben wurde, erschien `API-Fehler: API-Abfrage wegen Zeitüberschreitung fehlgeschlagen.` Die Reihenfolge ist relevant, weil `ConnectTimeout` zu beiden Fehlerklassen gehört.

**Prüfergebnis:** Die Datei lässt sich erneut einlesen; die drei geprüften
Abruffehler werden verständlich gemeldet. Die vereinbarten Kriterien von
Meilenstein 2 sind erfüllt.

### Historischer Pausenstand vom 21.10.2026

Dieser Abschnitt hält den damaligen Stand fest. Er wurde durch den Abschluss
vom 22.10.2026 überholt; für die Fortsetzung gilt „Aktueller Schritt“ oben.

- **Status:** Meilenstein 2 ist in Arbeit; auf meinen Wunsch pausiert. Nach dem Neustart beim oben genannten Lernauftrag fortsetzen.
- **Vorhandener Code:** `regenwurm.py` ruft eine Seite von GBIF ab, wandelt die Antwort mit `response.json()` um und speichert das vollständige Objekt mit `json.dump()` nach `data/regenwurm_rohdaten.json`. Der Dateipfad wird relativ zum Skript über `Path(__file__).parent` gebildet. Ausgegeben werden Statuscode und wissenschaftlicher Name der ersten Fundmeldung.
- **Ergebnisbelege:** Ich habe `200` und `Lumbricus terrestris Linnaeus, 1758` als Ausgabe gemeldet und den Attributzugriff sowie die verschachtelten Dictionary-/Listenzugriffe erklärt. Codex hat den Code gelesen und die gespeicherte Datei mit `json.load()` erfolgreich geprüft: gültiges JSON, oberste Felder `offset`, `limit`, `endOfRecords`, `count`, `results`, `facets`; eine Fundmeldung für *Lumbricus terrestris*. Der Netzwerkabruf wurde bei dieser Dateiprüfung nicht erneut ausgeführt.
- **Genauer Wiedereinstieg:** Mein eigener Leseversuch mit `json.load()` und meine Erklärung von Lesen gegenüber Schreiben stehen noch aus. Codex gibt dafür keine fertige Lösung vorab.
- **Weitere offene Punkte:** Zeitüberschreitung, HTTP-Fehler und verständliche Fehlermeldungen behandeln; anschließend die Abschlusskriterien von Meilenstein 2 prüfen.
- **Vor dem Herunterfahren:** Alle offenen Dateien im Editor speichern. Diese Dokumentationsänderung verändert weder Code noch Rohdaten.
- **Nach dem Neustart:** „Bitte am dokumentierten Pausenstand weitermachen.“ Codex liest zuerst den Plan und die direkt relevanten Dateien und gleicht sie mit diesem Stand ab.

Nach Unterbrechungen werden Plan und Projektstand verglichen. Erst nach erfolgreicher Prüfung wird der nächste Meilenstein begonnen; Änderungen an Umfang und Aufgabenverteilung werden gemeinsam festgehalten.

## Fachliche Vorbereitung zu Meilenstein 1

**Prüfdatum: 21.10.2026.** Vom Nutzer beauftragter Codex-Anteil: Taxonomie,
Synonyme, Fachquellen und Bestimmungsgrenzen. Keine Fundmeldungen abgerufen,
keinen Python-/SQL-Code erstellt und keine Steckbriefe vorformuliert.

### Beobachtete GBIF-Zuordnungen

Die öffentlichen Namensabgleiche der GBIF-API v1 und v2 lieferten für alle drei
Namen `SPECIES`, `ACCEPTED` und `EXACT`; v2 außerdem `synonym: false`.
Die Kennungen beziehen sich auf die hier abgefragte GBIF Backbone Taxonomy
(`d7dddbf4-2cf0-4f39-9b2a-bb099caae36c`), nicht auf beliebige Checklisten.

| Akzeptierter Name laut API | Artkennung | Beispiele aus der direkt gelesenen Synonymliste |
| --- | --- | --- |
| *Lumbricus terrestris* Linnaeus, 1758 | `4410657` | *Lumbricus agricola* Hoffmeister, 1843; *Lumbricus infelix* Kinberg, 1866 |
| *Lumbricus rubellus* Hoffmeister, 1843 | `4410669` | *Allolobophora relictus* Southern, 1909; *Helodrilus relictus* Southern, 1909 |
| *Aporrectodea caliginosa* (Savigny, 1826) | `2307759` | *Enterion caliginosum* Savigny, 1826; *Allolobophora caliginosa* (Savigny, 1826); *Nicodrilus caliginosus* (Savigny, 1826) |

**Belege:** Namensabgleich v1 für [L. terrestris](https://api.gbif.org/v1/species/match?name=Lumbricus%20terrestris),
[L. rubellus](https://api.gbif.org/v1/species/match?name=Lumbricus%20rubellus) und
[A. caliginosa](https://api.gbif.org/v1/species/match?name=Aporrectodea%20caliginosa);
Gegenprüfung v2 für [L. terrestris](https://api.gbif.org/v2/species/match?scientificName=Lumbricus%20terrestris),
[L. rubellus](https://api.gbif.org/v2/species/match?scientificName=Lumbricus%20rubellus) und
[A. caliginosa](https://api.gbif.org/v2/species/match?scientificName=Aporrectodea%20caliginosa).
Synonymlisten: [4410657](https://api.gbif.org/v1/species/4410657/synonyms?limit=100),
[4410669](https://api.gbif.org/v1/species/4410669/synonyms?limit=100),
[2307759](https://api.gbif.org/v1/species/2307759/synonyms?limit=100).
Alle drei Listen meldeten `endOfRecords: true`; die Tabelle zeigt eine Auswahl.

### Fachquellen und ihre Reichweite

- **Tauwurm und Bodenfunktionen:** Das [LfL-Merkblatt „Regenwürmer in bayerischen Ackerböden“](https://www.lfl.bayern.de/mam/cms07/publikationen/daten/merkblaetter/regenwuermer-ackerboeden_lfl-merkblatt.pdf),
  PDF-Seiten 2–4, erläutert Bodenlockerung, Stoffeinmischung und Lebensformen.
  Es nennt *L. terrestris* als Tiefgräber und *A. caliginosa* als Mineralbodenart.
  Die Größen- und Farbangaben der Übersicht gelten für Lebensformgruppen;
  sie sind keine artspezifischen Bestimmungsschlüssel.
- **A. caliginosa:** [Bart et al. (2018)](https://doi.org/10.1007/s11356-018-2579-9),
  insbesondere „Taxonomic considerations“ und „Morphology and life history traits“,
  behandelt Merkmale, Lebensraum, Lebensweise und ökologische Funktionen.
  Die Übersicht bezieht sich ausdrücklich auf *A. caliginosa* im engeren Sinn;
  ihre Aussagen gelten nicht automatisch für den gesamten Artenkomplex.
- **L. rubellus und Lebensform:** Der im Suchindex gelesene Auszug des [OPAL-Qualitätsberichts des Imperial College](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/opal-soil/OPAL-Data-Quality-Assessment-Report---Final-%281%29.pdf),
  Abschnitt 6.4.3, Tabelle 6.3 (gedruckte Seite 41), ordnet *L. rubellus* den
  Streubewohnern, *L. terrestris* den Tiefgräbern und *A. caliginosa* den
  bodenfressenden Mineralbodenarten zu. Britische Erfassungsdaten belegen keine
  deutsche Verbreitung; Lebensform und allgemeine Bodenfunktionen sind getrennt zu belegen.
  Der direkte PDF-Aufruf war mit HTTP 403 gesperrt; der Gesamtbericht wurde nicht geprüft.
- **Ergänzende Merkmalsquelle:** [Reynolds (2022), Fachmonografie der Canadian Food Inspection Agency](https://publications.gc.ca/site/eng/9.924984/publication.html?wbdisable=true),
  enthält laut geprüftem Katalog Artbeschreibungen und biologische Angaben.
  Für *L. rubellus* war ein Diagnoseauszug auffindbar. Der vollständige PDF-Abruf
  gelang nicht (Webwerkzeug: Größenlimit; Download lieferte HTML statt PDF).
  Daher vor Übernahme konkreter Größen- oder Farbangaben im jeweiligen Artkapitel
  nachlesen; diese Angaben sind hier nicht vollständig geprüft.

### Grenzen und Konsequenzen für die spätere Karte

- Ein exakter GBIF-Namensabgleich bestätigt die Zuordnung eines Namens, nicht die
  Bestimmung eines einzelnen Tieres. Auch die API-`confidence` ist kein Maß für
  die biologische Bestimmungssicherheit einer Fundmeldung.
- [James et al. (2010)](https://doi.org/10.1371/journal.pone.0015629) trennen
  *L. terrestris* und *L. herculeus* anhand von DNA-Daten; äußerliche Größenmerkmale
  überlappen. Die API führt [L. herculeus, 8706177](https://api.gbif.org/v1/species/8706177)
  als eigene akzeptierte Art. Ältere *terrestris*-Meldungen können deshalb fachlich
  unsicher sein; *herculeus* nicht pauschal als Synonym zusammenführen.
- Bei *A. caliginosa* unterscheiden sich Artkonzepte: Die gelesene GBIF-Synonymliste
  enthält etwa *A. tuberculata* und *Allolobophora nocturna*, während Bart et al.
  entsprechende Literatur ausdrücklich aus ihrer engeren Betrachtung ausschließen.
  Auch [A. trapezoides](https://api.gbif.org/v1/species/match?name=Aporrectodea%20trapezoides)
  wird von der abgefragten API einem anderen akzeptierten Namen
  (`acceptedUsageKey: 8566954`, `speciesKey: 2307759`) zugeordnet; Fachliteratur
  behandelt es teilweise als eigene Art. Vor dem Import diesen Grenzfall anhand
  tatsächlicher Meldungen gemeinsam abgrenzen; noch keine Importregel umgesetzt.
- Die [Earthworm Society of Britain](https://www.earthwormsoc.org.uk/identification)
  erläutert die erforderlichen Bestimmungsmerkmale und die Grenzen einfacher
  Feldschlüssel und Fotos. Ein Kurzporträt ersetzt keinen Bestimmungsschlüssel.

Die fachliche Vorbereitung und die nachfolgend dokumentierten eigenen
Beispielmeldungen mit Felderklärungen schließen Meilenstein 1 gemeinsam ab.
Die selbst verfassten Steckbriefe mit Belegen für konkrete Aussagen folgen
in Meilenstein 5; die dort genannten Quellen- und Bestimmungsgrenzen gelten weiter.

## Eigene Beispielmeldungen und Abschluss von Meilenstein 1

**Abgeschlossen am 21.10.2026.** Ich habe die Beispielabfragen selbst ausgeführt,
für die weiteren Arten den Parameter `taxonKey` angepasst und die Felder erklärt.
Codex hat meine im Chat übermittelten Ausschnitte und Erklärungen geprüft.
Die Live-Daten wurden dabei nicht unabhängig gegengeprüft; vollständige
JSON-Antworten und einzelne GBIF-Fundkennungen (`key`) sind hier nicht dokumentiert.
Die Suchantworten können sich bei einem erneuten Abruf ändern.

### Ausgeführte Beispielabfragen

- [Lumbricus terrestris](https://api.gbif.org/v1/occurrence/search?taxonKey=4410657&country=DE&hasCoordinate=true&hasGeospatialIssue=false&limit=1)
- [Lumbricus rubellus](https://api.gbif.org/v1/occurrence/search?taxonKey=4410669&country=DE&hasCoordinate=true&hasGeospatialIssue=false&limit=1)
- [Aporrectodea caliginosa](https://api.gbif.org/v1/occurrence/search?taxonKey=2307759&country=DE&hasCoordinate=true&hasGeospatialIssue=false&limit=1)

Alle drei Abfragen filtern auf Deutschland (`country=DE`), vorhandene Koordinaten
(`hasCoordinate=true`) und keine von GBIF markierten geografischen Probleme
(`hasGeospatialIssue=false`). `limit=1` begrenzt die Antwort auf höchstens eine Meldung.

### Übermittelte Werte

| Feld | Lumbricus terrestris | Lumbricus rubellus | Aporrectodea caliginosa |
| --- | --- | --- | --- |
| `scientificName` | Lumbricus terrestris Linnaeus, 1758 | Lumbricus rubellus Hoffmeister, 1843 | Aporrectodea caliginosa (Savigny, 1826) |
| `eventDate` | `2026-01-15T00:00` | `2026-03-15T18:23` | `2026-03-27T00:00` |
| `decimalLatitude` | `49.152138` | `49.782333` | `50.903912` |
| `decimalLongitude` | `9.278395` | `6.707246` | `6.854914` |
| `datasetKey` | `6ac3f774-d9fb-4796-b3e9-92bf6c81c084` | `50c9509d-22c7-4a22-a47d-8c48425ef4a7` | `6ac3f774-d9fb-4796-b3e9-92bf6c81c084` |
| `license` | `http://creativecommons.org/licenses/by/4.0/legalcode` | `http://creativecommons.org/licenses/by-nc/4.0/legalcode` | `http://creativecommons.org/licenses/by/4.0/legalcode` |

### Geprüfte Felderklärungen und besprochene Präzisierungen

- `scientificName`: wissenschaftlicher Name der zugeordneten Art einschließlich Namensautor und Jahr; kein unabhängiger Nachweis der korrekten Bestimmung des einzelnen Tieres.
- `eventDate`: angegebenes Funddatum, gegebenenfalls mit Uhrzeit. `T00:00` allein belegt keine tatsächlich beobachtete Uhrzeit.
- `decimalLatitude` und `decimalLongitude`: Breitengrad und Längengrad des angegebenen Fundortes.
- `datasetKey`: Kennung des Herkunftsdatensatzes, der mehrere Fundmeldungen enthalten kann. Die erste und dritte Meldung haben denselben Herkunftsdatensatz. Die einzelne Fundmeldung wird über `key` identifiziert.
- `license`: Lizenzangabe der bereitgestellten Daten. Die erste und dritte Meldung nennen CC BY 4.0, die zweite CC BY-NC 4.0; die Lizenz muss pro Meldung berücksichtigt werden.

**Prüfergebnis:** Für jede der drei Startarten liegt ein Beispielausschnitt mit
allen vereinbarten Feldern vor. Die Abfrageanpassung und die Felderklärungen
erfüllen zusammen mit der fachlichen Vorbereitung die Prüfkriterien von
Meilenstein 1. Der aktuelle Stand von Meilenstein 2 ist unter „Aktueller Schritt“ dokumentiert.
