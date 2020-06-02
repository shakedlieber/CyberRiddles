import mido
import urllib.request
import os
import sys

def addOrigin(midi_file, url, url_parts = []):
    for i in range(0, len(url)):
        u = url[i]
        if (u != "https:" and u != ""):
            url_parts.append(u)
    details = "File Details: "
    for i in range(1, len(url_parts)):
        details = details + url_parts[i] + ", "
    print(midi_file.tracks[0])
    midi_file.tracks[0].append(mido.MetaMessage('copyright', text = url_parts[0]))
    midi_file.tracks[0].append(mido.MetaMessage('text', text = details))
    print(midi_file.tracks[0])

def compareMidi(source, secret):
    curr_path = os.path.dirname(os.path.abspath(__file__))
    urllib.request.urlretrieve(secret, curr_path + "\\secret.mid")
    urllib.request.urlretrieve(source, curr_path+"\\source.mid")
    secretFile = mido.MidiFile('secret.mid')
    sourceFile = mido.MidiFile('source.mid')
    secretURL = secret.split("/")
    sourceURL = source.split("/")
    addOrigin(secretFile, secretURL)
    addOrigin(sourceFile, sourceURL)

    sourceFile.save(curr_path+"\\output.mid")
    secretFile.save(curr_path+"\\secondFile.mid")
    print("File:".ljust(11) + "\t\t " + "  First File".ljust(15) + "\t\t" + "Second File\n")
    print("Tracks Number:".ljust(15) + "\t\t" + str(len(sourceFile.tracks)).ljust(15) + "\t\t" + str(len(secretFile.tracks)) + "\n")
    print("Ticks Per Beat:\t\t" + str(sourceFile.ticks_per_beat).ljust(15) + "\t\t" + str(secretFile.ticks_per_beat) + "\n")
    print("Copyrighter:".ljust(15) + "\t\t" + sourceFile.tracks[0][-2].text.ljust(15) + "\t\t" + secretFile.tracks[0][-2].text)


def main():
    print("compares 2 url midi files: ")
    # compareMidi("https://bitmidi.com/uploads/85263.mid", "https://bitmidi.com/uploads/8547.mid")
    source = sys.argv[1]
    secret = sys.argv[2]
    compareMidi(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()


