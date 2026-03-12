from kokoro import KPipeline
import soundfile as sf

af_voices = ["alloy","aoede","bella:!","heart","jessica","kore","nicole","nova","river","sarah","sky"]
bf_voices =["alice","emma","isabella","lily"]
if_voices=["sara"]

am_voices=["adam","echo","eric","fenrir","liam","michael","onyx","puck","santa"]
bm_voices=["daniel","fable","george","lewis"]
im_voices=["nicola"]

voices = {
    "af_voices": af_voices,
    "bf_voices": bf_voices,
    "if_voices": if_voices,
    "am_voices": am_voices,
    "bm_voices": bm_voices,
    "im_voices": im_voices
}

gender = input("Male(m) or Female(f)\n")
language = input("Language:\nBritish English(b)\nAmerican English(a)\nItalian(i)\n")
x =""
lang=""

if(language=="a" or language=="A" ):
    #print("american english")
    x="a"
    lang=x
elif(language=="b" or language=="B"):
    #print("british english")
    x="b"
    lang=x
elif(language=="I" or language=="i"):
    #print("italian")
    x="i"
    lang=x
else:
    print ("Invalid value for language") 

if(gender=="M" or gender=="m" ):
    #print("male")
    x=x+"m"
elif( gender=="F" or gender=="f"):
    #print("female")
    x=x+"f"
else:
    print ("Invalid value for gender")

#print("\n")
y=x
y=y+"_voices"


name = input("\n".join(voices[y])+"\n")
x=x+"_"+name
#print(x)
#print("\n")
#print(lang)

pipeline = KPipeline(lang_code=lang)

text = input("Write a sentence\n")

generator = pipeline(
    text, voice=x,
    speed=1,split_pattern=r'\n+' #speed

)

for i,(gs,ps,audio) in enumerate (generator):
    print(i)
    print(gs)
    print(ps)
    sf.write(f'{i}.wav',audio,24000)
