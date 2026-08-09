# Run: python musical_instrument.py
# -----------------------------------------
# Musical Instrument Inventory
# -----------------------------------------

class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f"The {self.name} is fun to play!")

    def get_fact(self):
        return f"The {self.name} belongs to the {self.instrument_type} family."


# Create instrument objects
instrument1 = MusicalInstrument("Guitar", "String")
instrument2 = MusicalInstrument("Trumpet", "Brass")
instrument3 = MusicalInstrument("Flute", "Woodwind")
instrument4 = MusicalInstrument("Drums", "Percussion")


# Store them in an inventory list
inventory = [
    instrument1,
    instrument2,
    instrument3,
    instrument4
]


print("=== Musical Instrument Inventory ===\n")

for instrument in inventory:
    print("Instrument:", instrument.name)
    print("Type:", instrument.instrument_type)
    print(instrument.get_fact())
    instrument.play()
    print()