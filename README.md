# PythonTraining1
A C# assignment from my teacher, recreated in Python for practice.
# Initial Assignment:


# Aufgabe

In der heutigen Aufgabe geht es um die Implementierung einer Akkumulatorklasse.

## Übungsziel

Das Übungsbeispiel soll die bisher gelernten Kompetenzen in einer kleinen Einheit zusammenfassen. Diese Einheit sollte von jedem von Ihnen relativ einfach in der heutigen Doppelstunde implementiert werden können.

Die Aufgabenstellung soll Ihnen helfen, Ihre eigenen Fähigkeiten einzuschätzen.

## Übungsaufbau

Bitte halten Sie den folgenden Ablauf ein, wenn Sie die Aufgabe implementieren.

  1. Aufsetzen der Entwicklungsumgebung:
      - Erstellen einer Solution
      - Erstellen Sie folgende Projekte und fügen Sie sie der Solution hinzu:
        - Eine Bibliothek, welche die Klasse `Accumulator` zur Verfügung stellt.
        - Ein Programm, welches die `Accumulator` Klasse verwendet. Stichwort: Ausprobieren, was sie machen.
        - Ein Testprojekt, welches die `Accumulator` Klasse in Ihrer Funktion testet.
      - Stellen Sie sicher, dass die Abhängigkeiten zu Ihrer Bibliothek korrekt gesetzt sind.
      - Stellen Sie sicher, dass Sie alles richtig eingerichtet haben und das `leere` Projekt einwandfrei kompiliert

  2. Implementation
      * Implementieren Sie die Klasse nach der unten geforderten Funktionalität
      * Implementieren Sie die Tests.
      * Stellen Sie sicher, dass Ihre Klasse, Ihre Unittests und Ihr manuelles Testprogramm kompilieren und korrekt funktionieren.

  3. Dokumentation

      * Erstellen Sie eine DocString Dokumentation des öffentlichen Interfaces von `Accumulator`

  4. Formale Kriterien

      * Achten Sie auf korrekte Formatierung
      * Verwenden Sie keine One-Letter Variablennamen
      * Achten Sie darauf, dass Ihr gesamter Sourcecode in Englisch gehalten ist.
      * Vermeiden Sie Warnungen

## Anforderungen an die `Accumulator` Klasse

Die Klasse soll vier Zustandsvariablen beinhalten:

### Zustandsvariablen

1. Bezeichnung <br>
    z.B. `Varta AA`
3. Spannung in `V` <br>
  z.B. `1.2`
3. Maximale Kapazität in `mAh` <br>
  z.B. `1200`
4. Aktuelle verbleibende Kapazität<br>
  z.B. `645`

Und folgende Funktionalität

### Funktionalität

1. Einen Konstruktor, welcher die Bezeichnung als Parameter entgegennimmt.
2. Setter-Methoden für folgende Werte:
  * Spannung
  * Maximale Kapazität
  * Aktuelle Kapazität
3. Eine ToString Methode, welche den kompletten Zustand des Akkumulators als String returniert.
