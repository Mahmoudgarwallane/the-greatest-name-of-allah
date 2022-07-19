# coding=utf-8
from bs4 import BeautifulSoup
import requests as re

def replace_harakat(string):
    return string.replace(" ُ ".strip(), "") \
        .replace(" ّّ ".strip(), "") \
        .replace(" َ ".strip(), "") \
        .replace(" ِ ".strip(), "") \
        .replace(" ْ ".strip(), "") \
        .replace(" ٌ ".strip(), "") \
        .replace(" ٍ ".strip(), "") \
        .replace(" ً ".strip(), "") \
        .replace(" ۚ  ".strip(), "") \
        .replace(" ۗ    ".strip(), "") \
        .replace("  ۖ    ".strip(), "") \

def Html2Txt(HtmlFileName):
    # open existing html file
    surat_al_bakarah = open(HtmlFileName + ".html", "r", encoding="utf8")
    # read the content to be able to play with it
    contents = surat_al_bakarah.read()
    # control the html file with beautiful soup
    text = BeautifulSoup(contents, "lxml")
    # create txt file to put in the formatted data it's done with a permission a => create new file
    f = open(HtmlFileName + ".txt", "a", encoding="utf8")
    # find ayah
    Ays = text.findAll("a")
    # write them in the new text file with some formatting
    for i in Ays:
        f.write(i.text.strip() + " ")
    print("file created !! ")
    f.close()


asmaa_lah_lhosna =   "اللَّهُ  الأحدُ  الأعلى  الأكرم  الإله  الأَوَّلُ  الآخِرُ  الظَّاهِرُ  الْبَاطِنُ  الْبَارِئُ  الْبَرُّ  الْبَصِيرُ  التَّوَّابُ  الْجَبَّارُ  الحافظُ  الْحَسِيبُ  الْحَفِيظُ  الحفيُّ  الْحَقُّ  المبينُ  الْحَكِيمُ  الْحَلِيمُ  الْحَمِيدُ  الْحَيُّ  الْقَيُّومُ  الْخَبِيرُ  الْخَالِقُ  الخلاّقُ  الرّؤوفُ  الرَّحْمَنُ  الرَّحِيمُ  الرَّزَّاقُ  الرَّقِيبُ  السَّلامُ  السَّمِيعُ  الشّاكرُ  الشَّكُورُ  الشَّهِيدُ  الصَّمَدُ  العالمُ  الْعَزِيزُ  الْعَظِيمُ  الْعَفُوُّ  الْعَلِيمُ  الْعَلِيُّ  الْغَفَّارُ  الْغَفُورُ  الْغَنِيُّ  الْفَتَّاحُ  الْقَادِرُ  القاهر  الْقُدُّوسُ  القدير  القريب  الْقَوِيُّ  الْقَهَّارُ  الْكَبِيرُ  الْكَرِيمُ  اللَّطِيفُ  الْمُؤْمِنُ  الْمُتَعَالِي  الْمُتَكَبِّرُ  الْمَتِينُ  الْمُجِيبُ  الْمَجِيدُ  المحيط  الْمُصَوِّرُ  الْمُقْتَدِرُ  الْمُقِيتُ  الْمَلِكُ  المليك  المولى  الْمُهَيْمِنُ  النّصير  الْوَاحِدُ  الْوَارِثُ  الْوَاسِعُ  الْوَدُودُ  الْوَكِيلُ  الْوَلِيُّ الْوَهَّابُ "


surat_al_bakarah = open("surat_al_bakarah.txt", "r", encoding="utf8")
SuratAlBakarah = surat_al_bakarah.read()

surat_aal_iimran = open("surat_aal_iimran.txt", "r", encoding="utf8")
SuratAalIimran = surat_aal_iimran.read()

surat_taha = open("surat_taha.txt", "r", encoding="utf8")
SuratTaha = surat_taha.read()


for word in replace_harakat(asmaa_lah_lhosna).split():
    if word in replace_harakat(SuratAalIimran) and word in replace_harakat(SuratTaha) and word in replace_harakat(SuratAlBakarah) :
        print(word)

print("###############################################################################")
for word in asmaa_lah_lhosna.split():
    if word in SuratAalIimran and word in SuratTaha and word in SuratAlBakarah :
        print(word)

# print(replace_harakat(new_text))


#for i in "آمنّا":
    #print(i)


# source > https://equran.me/read-2.html"
