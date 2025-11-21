# RSS Read and Feed

RSS Read and Feed ist ein kleines Übungsprojekt, das ursprünglich dafür gedacht war, verschiedene GoF‑Design‑Patterns für die Abschlussprüfung zum Fachinformatiker Anwendungsentwicklung zu trainieren.
Gleichzeitig soll es einen Einblick in meinen Python‑Programmierstil geben.

Das Projekt ist ein YouTube‑RSS‑Reader, der YouTube‑Videos und Shorts einliest, in eigene DTO‑Objekte konvertiert und so aufbereitet, dass sie später in andere Systeme eingespeist werden können – zum Beispiel:

- Discord‑Bot
- Webserver / Webhook

## Was macht dieses Modul?

1. Ruft ein YouTube‑RSS‑Feed über HTTP ab
    – Beispiel:
    `https://www.youtube.com/feeds/videos.xml?channel_id=<ID>`

2. Erkennt automatisch anhand des Response‑Headers, ob der Inhalt JSON oder XML ist
    – dafür gibt es die Parser‑Factory.

3. Parst den Feed in ein einheitliches Dictionary, unabhängig vom Format.

4. Wählt über eine Strategie‑Factory automatisch den passenden Feed‑Konverter, z. B. für YouTube.

5. Erzeugt daraus sauber strukturierte Python‑DTOs (FeedItem / YoutubeVideoItem)
    – inkl. Titel, Autor, IDs, Description, Veröffentlichungsdatum, Typ (Video oder Short) usw.

6. Bereitet die Daten für weitere Verarbeitung/Weiterleitung vor.

Das finale Ergebnis ist eine Liste von einheitlichen Python‑Objekten, die alle notwendigen Informationen enthalten, um weiterverarbeitet zu werden.

## Eingesetzte Design‑Patterns

Hinweis: In einem echten Projekt würde ich wesentlich sparsamer mit Patterns umgehen. Hier dienen viele davon vor allem dem Lernen und Üben, nicht der Effizienz.

- Factory-Method
- Builder
- Decorator
- Strategy
- Singleton (als Metaclass)
