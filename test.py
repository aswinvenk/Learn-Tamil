import TamilLetters as t
e=t.TamilEluthu()

#e.disp_uyir_mei_category()
#e.disp_uyirmei()
#e.disp_uyirmei_table()
#e.disp_grantha_compound_table()
#e.disp_how_many_Eluthu("இனிய தொடர்கள்")
#print(e.get_TamilChar_list("நீங்கள் ஆங்கிலம் பேசுகிறீர்களா"))

#e.disp_how_many_Eluthu("நீங்கள் ஆங்கிலம் பேசுகிறீர்களா ")

#e.disp_uyir_mei_category()

#print(e.get_TamilChar_list("நீங்கள் ஆங்கிலம் பேசுகிறீர்களா ஃ ஸ்ரீ"))
#e.disp_how_many_Eluthu("நீங்கள் ஆங்கிலம் பேசுகிறீர்களா ஃ ஸ்ரீ")

#x=e.get_uyirmei_table_list() 
#print(e.get_vada_eluthu_list())

#print("ñ ஸ்ரீ ")

#print(e.disp_grantha_compound_table())
#e.disp_uyirmei()

#x=e.get_uyirmei_series_list()
#print(x[::-1])

#e.disp_how_many_Eluthu("நீங்கள் ஆங்கிலம் பேசுகிறீர்களா")


x=e.get_how_many_Eluthu_list("நீங்கள் ஆங்கிலம் பேசுகிறீர்களா")
for i in x:
    if i['no_of_letters']==0:
        pass
    else:
        print(i['eluthu_id'],i['no_of_letters'],i['eluthu'])



