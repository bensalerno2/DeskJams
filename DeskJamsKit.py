import simpleaudio as sa


class DeskJamKit():

    def __init__(self, master=None):
        self.master = master


    def client_exit(self):
        exit()

    def play_kick(self):
        filename = "Sounds/TastyKick.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_snare(self):
        filename = "Sounds/Snare.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_hat(self):
        filename = "Sounds/hat.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_ride(self):
        filename = "Sounds/Ride.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_clap(self):
        filename = "Sounds/Clap.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_walkIt(self):
        filename = "Sounds/WalkItTalkIt.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_rockstar(self):
        filename = "Sounds/Rockstar.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_bell(self):
        filename = "Sounds/Bell.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_Gyalchester(self):
        filename = "Sounds/Gyalchester.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_gucci(self):
        filename = "Sounds/Gucci.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()

    def play_suge(self):
        filename = "Sounds/RicFlair.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()








