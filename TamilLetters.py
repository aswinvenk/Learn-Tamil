import json
import pandas as pd

class TamilEluthu():
    def __init__(self):
        with open("tamilLetters.json","r") as fp:
            self.e=json.loads(fp.read())
        #   symbols
        self.symbols=self.e[4]['eluthu']

        #   vada eluthu
        self.vada=self.e[3]["eluthu"]

        #   mei eluthu
        self.mei_eluthu=[]
        for i in range(len(self.e[1]['eluthu'])):
            self.mei_eluthu.append(self.e[1]['eluthu'][i]+self.symbols[0])

        #   uyir eluthu
        self.uyir_eluthu=self.e[0]['eluthu']

        #   ayutha eluthu
        self.ayutha_eluthu=self.e[2]['eluthu']

        #   uyir-mei eluthu
        self.uyirmei_eluthu=[]
        for i in range(len(self.e[1]['eluthu'])):
            for j in range(1,len(self.symbols)):
                self.uyirmei_eluthu.append(self.e[1]['eluthu'][i]+self.symbols[j])

        #   grouping uyir-mei series!
        self.uyirmei_series = []
        for i in range(0,len(self.uyirmei_eluthu),12):
            self.uyirmei_series.append(self.uyirmei_eluthu[i:i+12])

        #                         vada eluthukal
        #   vada series
        v = []
        for i in range(len(self.vada)-2):
            for j in range(len(self.symbols)-1):
                v.append(self.vada[i]+self.symbols[j+1])
        self.vada_series = []
        for i in range(0,len(v),12):
            self.vada_series.append(v[i:i+12])
        #   vada eluthukal
        self.vada_eluthu = []
        for i in range(len(self.vada)-2):
            self.vada_eluthu.append(self.vada[i]+self.symbols[0])
        self.vada_eluthu.append(self.vada[-1])

        #   ENTIRE VADA SET OF LETTERS:
        self.vada_full_series = []
        for i in range(len(self.vada_series)):
            self.vada_full_series.append(self.vada_eluthu[i])
            for j in self.vada_series[i]:
                self.vada_full_series.append(j)
        self.vada_full_series.append(self.vada_eluthu[-1])
        self.vada_full_series.append(self.vada[-2])

        #   UYIRMEI TABLE
        self.uyirmei_table=pd.DataFrame(self.uyirmei_series,columns=[self.uyir_eluthu],index=[self.mei_eluthu])

        #  GRANTHA TABLE
        self.vada_table=pd.DataFrame(self.vada_series,columns=[self.uyir_eluthu],index=[self.vada_eluthu[:-1]])


    # dislpay methods

    def disp_uyir_eluthu(self):
        print(self.uyir_eluthu)
        
    def disp_mei_eluthu(self):
        print(self.mei_eluthu)

    def disp_grantha_eluthu(self):
        print(self.vada_eluthu)
    
    def disp_grantha_compound_table(self):

        """
        Displays the vada eluthukkal (grantha letters) compounded with vowels
        """
        #print(tabulate(self.vada_table, headers='keys', tablefmt='psql'))
        print(self.vada_table.to_markdown())

    def disp_uyirmei_table(self):
        print(self.uyirmei_table.to_markdown())
    

    # IMPORTANT DISPLAY

    def disp_uyirmei(self):
        """
        Learning Tamil UyirMei Eluthu (printing basic rules of uyir-mei)
        Make use of the:
        ## >obj.disp_uyirmei()
        to learn uyirmei eluthukal PROPERLY.

        This code is used to print uyirmei eluthukal when the 

        """

        series=[]
        seriesL=[]
        for i in range(len(self.mei_eluthu)):
            for j in range(len(self.uyir_eluthu)):
                y=self.mei_eluthu[i], "+", self.uyir_eluthu[j], "=", self.uyirmei_series[i][j]
                seriesL.append(y)
            series.append({self.mei_eluthu[i]:seriesL})
            seriesL=[]

        #Printing Uyir_eluthu list
        print("Uyir_eluthu List :")
        for i in range(len(self.uyir_eluthu)):
            print(i+1, ":", self.uyir_eluthu[i] )

        print("\n")

        #Printing Mei_eluthu list
        print("Mei_eluthu List :")
        for i in range(len(self.mei_eluthu)):
            print(i+1,":", self.mei_eluthu[i] )

        print("\n")

        
        #You can print the series as : series[consonantNo][e.meieluthu[consonantNo]]

        #Getting input from user and printing the series:

        x=int(input("Enter the consonant (mei eluthu) number  : "))
        print("The consonent corresponding to the number",x,"is :",self.mei_eluthu[x-1])
        for i in (series[x-1][self.mei_eluthu[x-1]]):
            for j in i:
                print(j, end="  ")
            print("\n")

        #printing the entire uyir_mei table

        x=input("Do you want the entire Uyir Mei table (y/n) : ").casefold()

        if (x=='y'):
            print(self.uyirmei_table.to_markdown())
        elif(x=='n'):
            pass
        else:
            print("Incorrect entry! If you need the table, Please type y")

    def disp_uyir_mei_category(self):
        """
        A method to display the uyir eluthu or mei eluthu category. 


        What are Uyir Eluthu and Mei Eluthu
        There are 30 Prime letters in tamil : 12 uyir eluthu (vowels) and 18 mei eluthu (consonants)
        The vowels are categorized based on the length as:
        1. short (kuril) : 5 letters
        2. long(nedil) : 5 letters
        The short vowels are pronounced for a duration 1 unit (1 maathirai), while the long vowels take two units (2 maathirai).
        The other two vowels ஐ(ai) and ஔ(au) are diphthongs formed by joining the letters அ(a)+இ(i) and அ(a)+உ(u).
        Since these two are a combination two short letters, their pronunciation takes 2 units of time, that is they fall under nedil category.
        ஐ(ai) and ஔ(au) can also be spelt அய் and அவ்.
        This form is known as eḻuttuppōli and is generally not recommended."""

        print("Uyir Eluthu (vowels) :", self.uyir_eluthu)
        print("Mei Eluthu (consonants) :", self.mei_eluthu)

        self.choice=input("Enter which category you want : (vowels / consonants) ").casefold()

        if(self.choice=='vowels'):
            
            print("\n Classification of Uyir Eluthu (vowels)")
            
            self.kuril=self.uyir_eluthu[:8:2]
            self.kuril.append(self.uyir_eluthu[9])
            print("Kuril eluthu :",self.kuril)

            self.nedil=self.uyir_eluthu[1:8:2]
            self.nedil.append(self.uyir_eluthu[10])
            print("Nedil Eluthu :",self.nedil)
            
            # print Kuril and Nedil Eluthukkal
            df=pd.DataFrame({"Kuril eluthu":self.kuril,"Nedil Eluthu":self.nedil})
            print(df.to_markdown())
            
            choice1=input("Do you want to continue (y/n) : ").casefold()

            if (choice1=='y'):
                print("Dipthongs are sound formed by the combination of two vowels in a single syllable")
                print("in which the sound begins as one vowel and moves towards another")
                self.dipthongs=[self.uyir_eluthu[8],self.uyir_eluthu[11]]
                print("tamil letters have 2 dipthongs : ",self.dipthongs)

                print("\nClassification of dipthongs as a table")
                self.df1=pd.DataFrame({"dipthong":self.dipthongs, "Letter 1":[self.kuril[0],self.kuril[0]],"Letter 2":[self.kuril[1],self.kuril[2]],"eḻuttuppōli":[self.kuril[0]+self.mei_eluthu[10],self.kuril[0]+self.mei_eluthu[13]]})
                print(self.df1.to_markdown())
            else:
                pass

            self.choice1=input("Do you want to continue (y/n) : ").casefold()

            if (self.choice1=='y'):

                self.classification = {
                        "Front":
                            {
                                'Close': 
                                    {
                                        'short' : self.kuril[1],
                                        'long' : self.nedil[1]
                                    },
                                'Mid':
                                    {
                                        'short' : self.kuril[3],
                                        'long' : self.nedil[3]
                                    }
                            },
                        "Central":
                            {
                                'Open':
                                    {
                                        'short' : self.kuril[0],
                                        'long'  : self.nedil[0]
                                    }
                            },
                        "Back":
                            {
                                'Close': 
                                    {
                                        'short' : self.kuril[2],
                                        'long' : self.nedil[2]
                                    },
                                'Mid':
                                    {
                                        'short' : self.kuril[4],
                                        'long' : self.nedil[4]
                                    }
                            }
                        }
                print("\nMonophthongs : From where the vowel is uttered\n")
                self.monothong=pd.DataFrame(self.classification)
                print(self.monothong.to_markdown())
            else:
                pass


        
        elif(self.choice=='consonants'):
        
            print("\n Classification of Mei Eluthu (consonants):")
            
            print("\nConsonants are classified as Vallinam, Mellinam and Idaiyinam.\n")
            
            # vallinam
            self.vallinam=self.mei_eluthu[:10:2]
            self.vallinam.append(self.mei_eluthu[-2])
            
            # mellinam
            self.mellinam=self.mei_eluthu[1:11:2]
            self.mellinam.append(self.mei_eluthu[-1])
            
            #idaiyinam
            self.idaiyinam=self.mei_eluthu[10:16]
            
            self.consonant_category=pd.DataFrame({"Vallinam":self.vallinam,"Mellinam":self.mellinam,"Idaiyinam":self.idaiyinam})
            print(self.consonant_category.to_markdown())

        else:
            print("You can only classify  உயிர் எழுத்துக்கள் (vowels) and மெய் எழுத்துக்கள் (consonants)")

    def disp_how_many_Eluthu(self,x):
        self.sentence=TamilEluthu().get_TamilChar_list(x)

        """
        If your input is "தொடர்கள்", 
        then,

        ## >> obj.disp_how_many_Eluthu("தொடர்கள்")
        
        Will give this output:

        uyir eluthu:             0
        mei eluthu:              2
        ayutha eluthu:           0
        uyirmei eluthu:          3
        vada eluthu:             0
        
        """
        print("\nYour input has ", len(self.sentence), " characters. They can be sorted as:")
        u=m=a=um=v=s=d=0
        list_u=[]
        list_m=[]
        list_um=[]
        list_a=[]
        list_v=[]

        for i in range(len(self.sentence)):
            if (self.sentence[i] in self.uyir_eluthu):
                u=u+1
                list_u.append(self.sentence[i])
            elif (self.sentence[i] in self.mei_eluthu):
                m=m+1
                list_m.append(self.sentence[i])
            elif (self.sentence[i] in self.uyirmei_eluthu):
                um=um+1
                list_um.append(self.sentence[i])
            elif (self.sentence[i] in self.ayutha_eluthu):
                a=a+1
                list_a.append(self.sentence[i])
            elif (self.sentence[i] in self.vada_full_series):
                v=v+1
                list_v.append(self.sentence[i])
            elif(self.sentence[i] == " "):
                s=s+1
            elif(self.sentence[i]=="."):
                d=d+1

        print("\nuyir eluthu:","\t\t",u,"\nmei eluthu:","\t\t",m,"\nuyirmei eluthu:","\t",um,"\nayutha eluthu:","\t\t",a,"\nvada eluthu:","\t\t",v)
        if(s>0):
            print("Your input has ", s, " spaces.")
        print('\nuyir',list_u,'\nmei',list_m,'\nuyirmei',list_um,'\nayutha',list_a,'\nvada',list_v)

   
    #  return as list methods
   
    def get_uyir_eluthu_list(self):
        """
        Returns the Uyir eluthukkal as a list
        """
        return self.uyir_eluthu
    
    def get_mei_eluthu_list(self):
        """
        Returns the Mei eluthukkal as a list
        """
        return self.mei_eluthu
    
    def get_uyirmei_eluthu_list(self):
        """
        Returns the UyirMei eluthukkal as a list
        """
        return self.uyirmei_eluthu
    
    def get_uyirmei_series_list(self):
        """
        Returns user specific series as a list
        """
        #Printing Mei_eluthu list
        print("Mei_eluthu List :")
        for i in range(len(self.mei_eluthu)):
            print(i+1,":", self.mei_eluthu[i])
        print("\n")
        x=int(input("Enter the consonant (mei eluthu) number  : "))
        print("The consonant corresponding to the number",x,"is :",self.mei_eluthu[x-1])
        return self.uyirmei_series[x-1]

    def get_ayutha_eluthu_list(self):
        """
        returns the ayutha eluthu as list
        """
        return self.ayutha_eluthu
    
    def get_grantha_eluthu_list(self):
        """
        returns the basic vada eluthukkal (Grantha consonants) as list
        """
        return self.vada_eluthu

    def get_grantha_eluthu_complete_list(self):
        """
        returns the complete vada eluthukal Grantha compound letters as list
        """
        return self.vada_full_series[:-1]

    def get_uyirmei_table_list(self):
        
        """
        Returns the uyirmei eluthukkal as a pandas table
        """
        return self.uyirmei_table

    def get_grantha_compound_table_list(self):

        """
        Returns the vada eluthukkal (grantha letters) compounded with vowels
        """
        self.vada_table=pd.DataFrame(self.vada_series,columns=[self.uyir_eluthu],index=[self.vada_eluthu[:-1]])
        return self.vada_table

    #  LIST IMPORTANT

    def get_TamilChar_list(self,x):

        """
        Getting a sentence in Tamil "correctly" in python
        Also finding the number of Uyir, Mei, UyirMei, Ayutha and Vada ELuthukkal

        Making use of the module TamilLetters.py for getting the name in right format 
        and categorising the eluthukal.

        For example, if you want to get the letters of "தொடர்கள்", it has 5 characters.
        But Python looks at this as: [ த, ொ,ட,ர,  ்,க,ள,  ்]
        
        using 
        ## >> obj.getTamilChar_list("தொடர்கள்")
        
        we get the output as a list
        
        [தொ,ட,ர்,க,ள்]

        """
        self.sentence=x
        """getting the name as a list"""
        self.name_list=[]
        for i in range(len(self.sentence)):
            self.name_list.append(self.sentence[i])
            
        """Normally the list will not be in right format"""
        #print("List not in right format:",name_list)

        
        """Merging letters with spl characters"""    
        for i in range(len(self.name_list)):
            for j in range(len(self.symbols)):
                if(self.name_list[i]==self.symbols[j]):
                    self.name_list[i-1]=(self.name_list[i-1]+self.name_list[i])
        #print("Merged :",name_list)

        """Removing the extra symbols"""
        xxx=[]           
        for i in range(len(self.name_list)):
            for j in range(len(self.symbols)):
                if(self.name_list[i]==self.symbols[j]):
                    xxx.append(self.name_list[i])
        for i in range(len(xxx)):
            self.name_list.remove(xxx[i])

        #print(name_list)
            
        """Checking for vada letters"""

        # KSHA
        for i in range(len(self.name_list)-1):
            if(self.name_list[i]+self.name_list[i+1]==self.vada[5]):
                self.name_list[i]=self.name_list[i]+self.name_list[i+1]
                self.name_list[i+1]="todelete"
        self.name_list=list(filter(lambda x: x!="todelete",self.name_list))

        # SHREE
        for i in range(len(self.name_list)-1):
            if(self.name_list[i]+self.name_list[i+1]==self.vada_eluthu[3]+self.uyirmei_series[11][3] or self.name_list[i]+self.name_list[i+1]==self.vada_eluthu[1]+self.uyirmei_series[11][3]):
                self.name_list[i]=self.name_list[i]+self.name_list[i+1]
                self.name_list[i+1]="todelete"
        self.name_list=list(filter(lambda x: x!="todelete",self.name_list))

        return(self.name_list)

    def get_how_many_Eluthu_list(self,x):
        
        self.sentence=TamilEluthu().get_TamilChar_list(x)

        """
        If your input is "தொடர்கள்", 
        then,

        ## >> obj.disp_how_many_Eluthu("தொடர்கள்")
        
        Will give this output:

        uyir eluthu:             0
        mei eluthu:              2
        ayutha eluthu:           0
        uyirmei eluthu:          3
        vada eluthu:             0
        
        """
        # print("\nYour input has ", len(self.sentence), " characters. They can be sorted as:")
        u=m=a=um=v=s=d=0
        list_u=[]
        list_m=[]
        list_um=[]
        list_a=[]
        list_v=[]

        for i in range(len(self.sentence)):
            if (self.sentence[i] in self.uyir_eluthu):
                u=u+1
                list_u.append(self.sentence[i])
            elif (self.sentence[i] in self.mei_eluthu):
                m=m+1
                list_m.append(self.sentence[i])
            elif (self.sentence[i] in self.uyirmei_eluthu):
                um=um+1
                list_um.append(self.sentence[i])
            elif (self.sentence[i] in self.ayutha_eluthu):
                a=a+1
                list_a.append(self.sentence[i])
            elif (self.sentence[i] in self.vada_full_series):
                v=v+1
                list_v.append(self.sentence[i])
            elif(self.sentence[i] == " "):
                s=s+1
            elif(self.sentence[i]=="."):
                d=d+1

        print("\nuyir eluthu:","\t\t",u,"\nmei eluthu:","\t\t",m,"\nuyirmei eluthu:","\t",um,"\nayutha eluthu:","\t\t",a,"\nvada eluthu:","\t\t",v)
        if(s>0):
            print("Your input has ", s, " spaces.")
        print('\nuyir',list_u,'\nmei',list_m,'\nuyirmei',list_um,'\nayutha',list_a,'\nvada',list_v)

    