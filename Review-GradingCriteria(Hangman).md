Eigentlich sind diese Criteria unter folgendem Link zu finden: https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/wiki/Grading-Criteria:-Hangman


# Grading Criteria Programmieren T3INF1004

Bei diesen Grading Criteria handelt es sich um unsere Bewertung eine anderen Projekts. Wir bewerten am 12.02.2024.

Das passende Github zum Projekt findet man unter: 

https://github.com/salmuuki/miniature-potato/tree/programmingwithuuki/Hangmanpics

# FACHKOMPETENZ (40 Punkte)

## Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
Der vorliegende Code verwendet mehrere Funktionen die das Spiel steuern und den Code in mehrere Abschnitte unterteilen. Das ermöglicht die Unterscheidung in verschiedene Schwierigkeiten. Zudem wird der Code sequenziell ausgeführt, beginnend mit der hauptmenü Funktion. Zudem werden auch Variablen verwendet um Informationen zu speichern.

### Verbesserungsmöglichkeiten: 

Obwohl der Code prozedural ist, könnte er durch die Verwendung von Klassen und objektorientierter Programmierung weiter strukturiert und organisiert werden. Zum Beispiel könnten Hangman-Spiel-Objekte erstellt werden, um den Zustand und die Logik eines Spiels zu verwalten.

## Sie können die Syntax und Semantik von Python (10)

### Verwendung von Kommentaren: 

Kommentare wurden eingefügt, um den Code zu erklären. Insbesondere die Funktionen und deren Zweck werden beschrieben. Dies erleichtert anderen Entwicklern das Verständnis des Codes.

### Verwendung von Konstanten: 

Konstanten wie Fenstergröße, Farben und Schwierigkeitsstufen wurden am Anfang des Codes definiert und dann im gesamten Programm verwendet. Dies macht den Code wartbarer, da Änderungen an diesen Werten an einer zentralen Stelle vorgenommen werden können.

### Konsistente Benennung:

Die Benennung von Variablen und Funktionen ist konsistent und beschreibend. Dadurch wird die Lesbarkeit des Codes erhöht. 

### Verwendung von Rechtecken für Kollisionserkennung: 

Die Verwendung von Rechtecken zur Erkennung von Mauskollisionen mit Buttons ist eine effiziente Methode. Rechtecke sind einfacher zu berechnen und bieten eine zuverlässige Möglichkeit, Interaktionen zwischen Maus und Benutzeroberfläche zu überprüfen.

## Verbesserungsvorschläge:

### Doppelte Initialisierung von Pygame: 

In den Funktionen spiel_leicht(), spiel_mittel() und spiel_schwer() wird Pygame jeweils zweimal initialisiert. Dies ist ineffizient und kann zu unerwartetem Verhalten führen. Es sollte nur einmal in der Hauptfunktion hauptmenü() initialisiert werden.

### Unnötige Schleifen: 

In den genannten Funktionen gibt es zwei Schleifen, die praktisch denselben Code ausführen. Dies könnte in eine separate Funktion extrahiert werden, um Redundanz zu vermeiden und den Code zu vereinfachen.

### Bildpfade als Liste: 

Die Bildpfade werden als Liste von Zeichenketten definiert. Es könnte besser sein, eine Datenstruktur wie ein Dictionary zu verwenden, um die Zuordnung von Versuchen zu Bildpfaden klarer zu machen und den Code leichter verständlich zu gestalten.

### Kommentare:

Für eine bessere Verständlichkeit des Codes sollten mehr Kommentare verwendet werden.

Durch die Berücksichtigung dieser Punkte könnte der Code weiter verbessert werden, sowohl in Bezug auf seine Effizienz als auch auf seine Wartbarkeit und Lesbarkeit.

## Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

Auf Github sieht man bis jetzt nur Commits und Änderungen von einer Person. 

## Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

In dem gegebenen Code wurden verschiedene Datenstrukturen verwendet, einschließlich Listen und Dictionaries.

### Listen: 

Listen werden verwendet, um Wörter zu speichern. Beispielsweise werden in den Funktionen spiel_leicht(), spiel_mittel(), und spiel_schwer() Listen verwendet, um die Wörter auszuwählen, mit denen das Spiel gespielt wird. 

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/41bada59-ebde-4c39-9d47-aa2683d6e215)

### Dictionaries: 

Die Funktion ist_button_gedrueckt() verwendet ein Dictionary, um zu überprüfen, welcher Button gedrückt wurde, und gibt dann entsprechend True zurück.

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/50312503-ea8e-4980-9045-7197c4bc1745)

# METHODENKOMPETENZ (10 Punkte)

## Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

### Verwendete Bibiliotheken:

- Pygame
- Sys
- Random

### Github

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/c198d0bc-eb3c-4925-87b9-b8e214d27f5d)

# ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

## Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

Die Idee das Spiel von der realen Welt auf den Bildschirm zu bringen erfordert genaues reindenken in die Spiellogik. 
Wir finden es gut, dass die Möglichkeit einer Datenbank implementiert werden soll. Auch die Umsetzung der Buchstabeneingabe gefällt uns sehr.

# Kenntnisse in prozeduraler Programmierung:

## - Algorithmenbeschreibung

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/689d1e92-f8f4-49e9-b959-cada4898f11e)

## - Datentypen

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/1d8286cc-615d-4952-87d6-101da8ad359a)

## - Operatoren

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/bb5bfea1-2663-4db5-b15c-8cad0079bc78)

## - Kontrollstrukturen

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/3d4e7c82-6b33-4d7d-852e-713c5ed05784)

## - Funktionen

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/4be2de6a-0de1-44dc-9d96-db1ecfb28538)

## - Stringverarbeitung

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/d8279976-b89a-45dc-b005-15777b71275a)

## - Strukturierte Datentypen

Listen und Dictionaries siehe oben

# Verbesserungsvorschläge:

### Optimierung:

Reduzieren des redundanten Code und nutzen von effektiv Schleifen und Datenstrukturen, um Duplikate zu vermeiden.

### Benutzererfahrung:

Verbesserung der Benutzererfahrung durch Feedback und die Integration von Soundeffekten oder Animationen.

### Code-Dokumentation:

Hinzufügen von Kommentaren und Docstrings, um den Code zu erklären und die Wartung zu erleichtern.
