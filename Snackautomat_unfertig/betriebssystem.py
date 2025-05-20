class Betriebssystem:
    def __init__(self):
        self.last_event = None

    def verarbeite_event(self, event_typ, wert):
        # Hier wird später die Logik für Münzen und Tasten implementiert
        print(f"Ereignis empfangen: {event_typ} - {wert}")
