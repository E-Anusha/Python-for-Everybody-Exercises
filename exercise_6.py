'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''

'''
text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0')

val = (text[pos:])

fval = float(val)

print(fval)

val1 = int(text.find(':'))
print(text[:val1])
'''

text = '''A method for manipulating the nervous system of a subject located near a monitor, the monitor emitting an electromagnetic field when displaying an image by virtue of the physical display process, the subject having a sensory resonance frequency, the method comprising:creating a video signal for displaying an image on the monitor, the image having an intensity;modulating the video signal for pulsing the image intensity with a frequency in the range 0.1 Hz to 15 Hz; and'''
atpos = text.find(':')
preamble = text[0:(atpos+1)]
atpos1 = text.find(';',atpos)
claim1 = text[(atpos+1):(atpos1+1)]
print(preamble)
print(claim1)
