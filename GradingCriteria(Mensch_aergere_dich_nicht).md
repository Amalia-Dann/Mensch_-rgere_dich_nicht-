Eigentlich sind diese Criteria unter folgendem Link zu finden: https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/wiki/Grading-Criteria:-Mensch-ärgere-dich-nicht


# Grading Criteria Programmieren T3INF1004 (Mensch ärgere dich nicht)
____________________________________________________________________________________________________________________________________________
## FACHKOMPETENZ (40 Punkte)

### Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

Um die prozedurale Programmierung gut umsetzen zu können haben wir Klassen zusätzlich zur Main verwendet. In diesen Klassen wurden zum Beispiel Methoden benutzt, welche dann wiederum in den Objekten der Main aufgerufen werden. 
Da wir 16 Figuren haben müsste man theoretisch manche Funktionen 16 mal in den Code mit implementieren. Durch die Klassen und Methoden sparen wir an Code und damit Speicherplatz. Dadurch, dass die Figuren alle die gleichen Eigenschaften besitzen machen wir uns die Wiederverwendbarkeit zu Nutze. 

Die Problematik mit den Koordinaten hat uns gezeigt, dass die Aufteilung in Klassen sehr sinnvoll ist. \
--> Wir konnten einmal die Koordinaten ändern und mussten nicht in jeder Zeile, in der die Koordinaten verwendet werden danach schauen. (Klasse: gamefield) 
--> Dies vereinfacht und verkürzt die Wartungen des Codes enorm. 

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/73f4e159-11e5-4489-95c4-c627a02a1834) 

Die klare Struktur wird bei uns durch die Nutzung von Funktionen sichergestellt. Diese erlauben, dass nicht jede Zeile an Code direkt nacheinander kommt, sondern, dass eine gewisse Struktur und trotzdem die Funktionalität bestehen bleibt.

### Sie können die Syntax und Semantik von Python (10)

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/e30daee4-e7e0-4cdf-9b5b-dc24a39c6ae4)

Diese Funktion wird jedes mal aufgerufen, wenn ein Button (der 16 Figuren) angeklickt wird. Dabei wird die gewürfelte Zahl, die aktuelle Position, sowie Farbe und Figurennummer übergeben. 
In der Funktion selbst wird die Farbe überprüft und wo man sich im Moment befindet (Haus oder Feld). Um sich aus dem Haus zu bewegen, wird die Augenzahl des Würfels überprüft. Nur bei einer sechs darf man auf das Startfeld ziehen. 
Befindet man sich nicht im Haus wird durch eine for-Schleife die aktuelle Position in der Felder-Liste gesucht und um die Augenzahl erhöht. (Die Felder-Liste enthält 40 Einträge, welche wiederum die x- und y-Koordinaten der einzelnen Felder enthält. 
Wenn man sich am Ende der Felder-Liste befindet (Feld vor dem gelben Startfeld) wird diese wieder auf Null gesetzt, was ALLEN Farben ermöglicht, das Feld komplett zu umrunden.  

### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

Wir haben für das Projekt das Tool "Code With Me" von Pycharm verwendet. \
Der Code wurde von Amalia dann immer auf github gepusht. Erst gegen Ende wurden die Veränderungen von Felix sichtbar (wurde aber bereits angesprochen)

### Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/1a5e8380-8b0e-4cf4-b782-892cd5e844ee)

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/2d4a5d39-3a10-4ab0-ad36-2034eea153b9)

In diesem Beispiel haben wir die Datenstruktur Dictionaries verwendet.

Erklärung: \
In der Funktion die die Parameter aktuelle Figur sowie die neue Position der Figur übergeben bekommt, wir in einer Schleife überprüft, ob sich bereits eine andere Figur auf ebendiesem Feld befindet

![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/e84b4cac-76a4-40af-bab7-d28c08f3614a) \
Das Dictionary trägt hierbei dazu bei, dass der Abgleich der Daten ermöglicht wird. 

____________________________________________________________________________________________________________________________________________
## METHODENKOMPETENZ (10 Punkte)

### Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

Für dieses Projekt haben wir Pycharm verwendet. Dazu haben wir uns Videos und Erklärungen angeschaut um uns gut einzuarbeiten. 
Uns hat vor allem die Funktion "Code With Me" sehr gut daran gefallen. 
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/6e6413b2-5b95-4345-9e34-82b0b91a5c3f)


Nach einigen Komplikationen haben wir es auch geschafft, Github mit Pycharm zu verbinden und unsere Veränderungen am Code zu pushen. \
https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht
____________________________________________________________________________________________________________________________________________
## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

### Die Studierenden können ihre Software erläutern und begründen. (5)
In unserem ersten großen Projekt in Python haben wir gemeinsam an der Entwicklung eines Spiels gearbeitet. Es war eine spannende und lehrreiche Erfahrung, die uns ermöglichte, unsere Programmierkenntnisse weiter zu vertiefen und an unseren praktischen Fähigkeiten zu arbeiten.

### Felix Hilfe für Amalia:\
Als wir mit dem Projekt begonnen haben, hatte ich noch keine Ahnung von Klassen, Methoden und Co. Grundsätzlich könnte man sagen, dass ich kein Wissen über die objektorientierte Programmierung besessen habe. Felix hingegen, hatte davor schon in Java programmiert und damit auch schon mit Klassen gearbeitet. Mit seiner Hilfe konnte ich recht schnell nachvollziehen, was es mit Klassen und Methoden auf sich hat und wie diese funktionieren. 
Weiterhin hat er sich zuerst mit Pygame beschäftigt und mir daher auch beim Einlernen in die Library sehr geholfen. Wenn ich beim Coden Unterstützung gebraucht habe, hat er mir sehr oft helfen können. In dem Projekt haben wir uns oft gegenseitig ergänzt, wenn ich die Ideen hatte und er die Umsetzung.

### Amalias Hilfe für Felix:\
Während des gesamten Projekts war die Unterstützung von Amalia von großem Wert. Sie hatte in Python schon mehr Erfahrungen als ich und half mir oft dabei, Probleme zu lösen und Herausforderungen zu meistern, denen wir gegenüberstanden. Ihre Geduld und ihr Wissen aus ihrer Oberstufenzeit halfen mir dabei, die Grundlagen der Programmiersprache besser zu verstehen und mich später dann in komplexeren Konzepten zurechtzufinden.
Eine wichtige Lektion, die ich aus dieser Zusammenarbeit gelernt habe, ist die Bedeutung verschiedener Perspektiven beim Programmieren. Amalia und ich hatten oft grundsätzlich verschiedene Ansätze zur Lösung eines Problems. Während ich selbst dazu neigte, mich bei einer bestimmten Methode zu verkopfen, brachte sie neue Ideen und alternative Lösungsansätze ein. Dies führte oft zu neuen Überlegungen und anregenden Diskussionen darüber, welcher Ansatz der beste war. Am Ende war es genau diese Vielfalt an Perspektiven, die es uns ermöglichte, die besten Lösungen zu finden und das Spiel erfolgreich zu entwickeln.

Das Projekt war nicht nur eine Gelegenheit, unsere technischen Fähigkeiten zu verbessern, sondern auch eine Gelegenheit, an Teamarbeit und Kommunikation zu feilen. Durch den Austausch von Ideen (vor allem Brainstorming) und die Zusammenarbeit an einem gemeinsamen Ziel konnten wir unser Projekt verwirklichen.
Insgesamt war die Entwicklung dieses Spiels eine Erfahrung, die uns nicht nur technisch weitergebracht hat, sondern auch unsere Fähigkeiten als Programmierer und Teammitglieder gestärkt hat.

### Sie können existierenden Code analysieren und beurteilen. (5)

Auf dieser Seite des Wikis haben wir das Projekt von Recep, Salma und Katharina nach den Grading Criteria bewertet:

https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/wiki/Grading-Criteria:-Anderes-Projekt-(Hangman)

### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

- Hilfe: 
In der Planungsphase haben wir uns mit einem Studenten aus einem höheren Semester zusammengesetzt und Tipps für die Herangehensweise erhalten.

- Pygame:
Dadurch, dass unser Spiel eine graphische Oberfläche hat, hat uns die Library von Pygame sehr viel weiterhelfen können. 
Zusätzlich zum Unterricht haben wir uns in diese genauer eingearbeitet um uns verschiedene Sachen zu vereinfachen. 
Wir haben die Library verwendet um die Maus zu tracken, sowie Tastatureingaben zu speichern. Somit konnten wir auch fremde Graphiken in das Spiel integrieren, wie zum Beispiel der Hintergrund des Startbildschirms (wurde von KI erstellt). Zusätzlich hatten wir die Möglichkeit aus den Fragen der Community und den Tutorials (https://www.pygame.org/wiki/tutorials) zu lernen. 

- GUI:
Da wir eine Vorstellung eines 2D Spielbrett hatten, wollten wir die Grafiken nicht missen. Dafür mussten wir uns grundlegende Fähigkeiten im Themengebiet Benutzeroberflächen aneignen. In unserer Oberfläche sind z.B. Buttons, Text(eingabe)felder und Bilder zu finden. 
Dabei war Pygame auch eine große Hilfe ereignisgesteuerte Programmierung zu implementieren.

- Objektorientierte Programmierung: 
Um die Aufgabe eines größeren Projekts zu meistern, haben wir es uns zur Aufgabe gemacht, uns in die objektorentierte Programmierung einzuarbeiten. Auch wenn Python dafür nicht üblich verwendet wird, hatte es für unser Projekt viele Vorteile (siehe oben). 

- Python-Kenntnisse:
Zusätzlich zu den ganzen neuen Dingen, die wir gelernt haben, haben wir auch unsere Grundkenntnisse vertieft und erweitert. Nur dadurch war das Projekt machbar.

____________________________________________________________________________________________________________________________________________
## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

- Idee:
Der Plan war von Anfang an klar, dass wir kein vollständig automatisiertes Spiel haben wollten, da sonst der Spielspaß verloren geht. Das Ziel war eine moderne, digitale Alternative zum klassischen Brettspiel. 
Die Programmierung des Spiels ermöglicht eine starke Individualität je nach Spieler und deren Wünschen.
Beispiele:
--> Um aus den Häusern rauszukommen kann man einmal oder aber auch dreimal Würfeln
--> Man kann sich selbst aus dem Spiel schlagen. 

==> Wir sind stolz darauf, dass die Figuren und den Würfel erfolgreich umgesetzt wurden und man diese auch selbst bedienen kann. 

- Zeitmanagement: Trotz unserer verschiedenen Hobbies, Plänen, etc. haben wir es gemanaged Termine und Deadlines zu vereinbaren um das Projekt weiterhin am Laufen zu halten. Wir haben uns als Ziel gesetzt unsere vorher festgelegten Meilensteine Schritt für Schritt zu erreichen. Dazu haben wir uns regelmäßig (auf Discord und Präsenz) getroffen und immer wieder einige Zeit geplant, gecodet und verbessert.

- Probleme: \
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/ae6c06ef-7701-4eb8-8fd9-e53064a2a0e3)\
Bei Problemen, die beim Coden entstanden sind, Beispiele siehe oben, haben wir uns nicht runterkriegen lassen sondern zusammengesetzt und die Planung wieder aufgenommen und verändert. 

- Reflexion: 
Dadurch, dass wir immer wieder gecodet haben, hat sich eine Routine entwickelt ungefähr 4 oder 5 Mal die Woche zu Coden. 
Besonders froh sind wir über die vorherige Planung, da wir dadurch einigen Problemen wie z.B. Planlosigkeit und Zeitmangel aus dem Weg gehen konnten. 

- Funktionalität:
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/b872fa88-8e7c-43d0-a8d3-c8ea596001c1)
Dieser Aufbau der Funktionalität hat uns vor allem beim Schreiben der Methoden und Funktionen geholfen, da das Schaubild die Schwierigkeiten des Spiels möglichst einfach herunterbricht. 

____________________________________________________________________________________________________________________________________________
## Kenntnisse in prozeduraler Programmierung:

## - Algorithmenbeschreibung
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/52ae2d0f-c619-4a2b-8c3e-b6e853ae51c2)

## - Datentypen
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/2aded521-9595-4d8b-b942-9e9a27d8858e)

## - Operatoren
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/3447f941-b62e-4e51-955c-ddd38b7f2ede)

## - Kontrollstrukturen
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/e3655640-b12b-427d-9437-76018fa8347f)

## - Funktionen
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/31f6f012-96e9-4466-bd81-6e726cc6ddf8)

## - Stringverarbeitung
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/fd1350c3-b55f-4111-9e19-33320a90e8f5)

## - Strukturierte Datentypen
![image](https://github.com/Amalia-Dann/Mensch_aergere_dich_nicht/assets/125802798/6d432d3c-963d-4d6f-8788-a007e30db118)

