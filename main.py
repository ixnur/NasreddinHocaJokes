import random

class NasreddinHoca:
    def __init__(self, isim):
        self.isim = isim
        self.fikralar = {
            'tr': [
                "Çocuklar, pazara gelen Nasreddin Hoca'nın etrafını sarmış. 'Hoca, bana düdük al!' demiş biri. 'Bana da, bana da!' demiş bir diğeri.",
                "İçlerinden sadece biri Nasreddin Hoca’nın düdük parasını vermiş. Hoca, parayı alıp pazara gitmiş.",
                "Akşam pazardan dönünce çocuklar etrafını sarmış. Her biri düdüğünü istemiş. Cebinden bir düdük çıkaran hoca, parayı veren çocuğa vermiş.",
                "Diğer çocuklar hep bir ağızdan bağırmış: 'Hani bizim düdüğümüz?' Nasrettin Hoca gülerek, 'Parayı veren düdüğü çalar,' demiş.",
                
                "Nasreddin Hoca bir gün gölün kıyısına gider. Elinde koca bir kaşık yoğurdu da yanına almış.",
                "Nasreddin Hoca, kaşığındaki yoğurdu göle sokmuş ve yoğurdu göle boşaltmış.",
                "Adam, Hoca’ya bakmış ve kahkaha atarak: 'Ne diyorsun be Hoca, çıldırmış olmalısın. Koskoca göl hiç maya tutar mı?' demiş.",
                "Hoca gülümsemesini hiç bozmadan: 'Peki ama ya tutarsa,' demiş.",
                
                "Eşeği ile kasabaya alışverişe giden Nasreddin Hoca;",
                "kitap, elma, limon gibi birçok ağır şey almış. Aldıklarını kocaman bir çuvala yerleştirmiş.",
                "Çuvalı da sırtına alıp eşeğine binmiş. Yolda giderken Hoca’yı gören köylüler:",
                "– Ey Hoca, çuvalı niye kendi sırtına aldın?, diye sormuşlar.",
                "Hoca: 'Ne yapayım? Zavallı hayvan zaten beni taşıyor, çuvalı da ona taşıtmaya gönlüm razı olmadı,' demiş.",
                
                "Nasreddin Hoca bir gün evde otururlarken karısına:",
                "– Hanım iyi dinle, size vasiyetimdir. Ben öldüğümde beni baş aşağı gömün,' demiş.",
                "Karısı şaşırmış: 'Hoca o ne demek? Neden böyle bir şey istiyorsun,' demiş.",
                "Hoca ciddi bir şekilde: 'Yarın öbür gün kıyamet koparsa her şey ters düz olacak.",
                "O zaman ben de düz olarak ayağa kalkabilirim,' demiş.",
                
                "Nasreddin Hoca bir gün bir işi için Konya’ya gitmiş. Yolda giderken bir adam Hoca’yı durdurmuş:",
                "– Pardon Amca, bugün ayın kaçı biliyor musun?, demiş.",
                "Hoca: 'Ne bileyim yahu! Ben buraların yabancısıyım,' demiş.",
                
                "Nasreddin Hoca bir gün yolda giderken bir adamla karşılaşmış. Adamla sohbet etmeye başlamış.",
                "Bir saat havadan sudan konuştuktan sonra Hoca:",
                "– Kusura bakma arkadaş. Ben seni tanıyamadım, adın neydi?, diye sormuş.",
                "Adamcağız çok şaşırmış:",
                "'Madem beni tanımadın, neden benimle bir saattir sohbet ediyorsun?, demiş.",
                "Nasreddin Hoca: 'Kıyafetlerin benimkine çok benziyordu. Ben de seni ben sandım,' demiş.",
                
                "Nasreddin Hoca’nın iki oğlu varmış. Oğullarından biri çömlekçilik yaparak geçimini sağlarmış.",
                "Hoca bir gün oğlunun yanına onu ziyarete gitmiş.",
                "Oğlu dertli bir şekilde: 'Baba çok heyecanlıyım çünkü bütün paramı bu çömleklere yatırdım.",
                "Hava güneşli olur da kururlarsa zengin olacağım.",
                "Yağmur yağarsa hepsi çatlayacak ve anam ağlayacak,' demiş.",
                "Hoca dertli bir şekilde diğer oğluna gitmiş. Oğlu o sırada tarlasında oturmuş düşünüyormuş:",
                "– Ah baba hoş geldin. Bütün paramı bu tarlaya yatırdım. Eğer güneşli olursa güzel bir hasat alırım.",
                "Yağmur yağarsa ekinler çürür ve anam ağlayacak,' demiş.",
                "Hoca, her iki oğlunu da dinledikten sonra kendi kendine gülmüş:",
                "– İyi ki bir kızımız yok. Onun parasını da kuymuş olacaktık,' demiş.",
                
                "Nasreddin Hoca bir gün pazardan bir kilo tuz alır. Eve dönerken yolun kenarında bir grup çocuk görür.",
                "Çocuklardan biri koşarak gelir ve Hoca’nın elindeki tuzu ister.",
                "Hoca şaşkın bir şekilde çocuğa bakar ve sorar: 'Peki, ama neden bu kadar tuz istiyorsun?",
                "Çocuk gülerek cevap verir: 'Annem yemekte tuz unuttu, onun yerine bunu götüreceğim.",
                
                "Nasreddin Hoca bir gün camiye gitmiş. Cemaat namaz kılarken Hoca sağa sola bakınıyormuş.",
                "Cami imamı rahatsız olmuş ve Hoca’ya seslenmiş: 'Hoca, namaza niye odaklanmıyorsun?",
                "Hoca cevaplamış: 'Namazda aklım sürekli para dağıtma hayaliyle meşgul. Bir gün zengin biri ölürse, belki bana da bir şeyler düşer diye bekliyorum.",
                
                "Nasreddin Hoca bir gün kuyumcudan çıkarken yanında bir sürü çocuk belirmiş. Çocuklardan biri sormuş:",
                "– Hoca amca, sen altın mı aldın?, demiş.",
                "Hoca gülerek cevap vermiş: 'Evet, altın aldım.",
                "Çocuklar sevinçle bağırmış: 'Ne zamandan beri altın alıyorsun Hoca amca?",
                "Hoca cevaplamış: 'Ne zaman borç para bulsam, hemen altın alıyorum,' demiş."
            ],
            'en': [
                "Children surrounded Nasreddin Hoca at the market. One of them said, 'Hoca, buy me a whistle!' Another one said, 'Me too, me too!'",
                "Only one of them gave Nasreddin Hoca the money for the whistle. Hoca took the money and went to the market.",
                "When he returned from the market, children surrounded him again. Each one asked for their whistle. Hoca took out a whistle from his pocket and gave it to the child who gave him the money.",
                "Other children shouted all together: 'What about our whistles?' Nasreddin Hoca laughed and said, 'The one who pays steals the whistle.'",
                
                "One day Nasreddin Hoca went to the edge of the lake. He carried a large spoonful of yogurt with him.",
                "Nasreddin Hoca dipped the spoon with yogurt into the lake and emptied the yogurt into the lake.",
                "A man looked at Hoca and laughed, saying, 'What are you saying, Hoca? Have you gone crazy? Can a big lake like this catch yeast?'",
                "Hoca, still smiling: 'Well, but what if it does catch?,' he said.",
                
                "Nasreddin Hoca went to the market with his donkey to do some shopping;",
                "he bought many heavy things like books, apples, lemons. He put everything in a big sack.",
                "He put the sack on his back and rode his donkey. As he was going on the road, villagers who saw him asked:",
                "– Hey Hoca, why did you put the sack on your own back?, they asked.",
                "Hoca: 'What can I do? The poor animal is already carrying me, and I didn't want to burden it with the sack,' he said.",
                
                "One day, Nasreddin Hoca was sitting at home when he said to his wife:",
                "– Dear, listen carefully, it is my will. Bury me upside down when I die,' he said.",
                "His wife was surprised: 'Hoca, what does that mean? Why do you want such a thing?,' she said.",
                "Hoca, seriously: 'If doomsday comes one day, everything will be upside down.",
                "Then, if I'm buried upside down, I might be able to stand up normally,' he said.",
                
                "Nasreddin Hoca went to Konya for some business one day. On the way, a man stopped Hoca:",
                "– Excuse me, Uncle, do you know what day it is today?, he said.",
                "Hoca: 'How should I know? I'm a stranger around here,' he said.",
                
                "One day, Nasreddin Hoca met a man while walking on the road. He started chatting with the man.",
                "After an hour of talking about this and that, Hoca asked:",
                "– Sorry, my friend. I couldn't recognize you, what was your name again?, he said.",
                "The man was very surprised:",
                "'Since you didn't recognize me, why have you been talking to me for an hour?,' he said.",
                "Nasreddin Hoca: 'Your clothes looked very similar to mine. I thought you were me,' he said.",
                
                "Nasreddin Hoca had two sons. One of his sons made a living by making pottery.",
                "One day, Hoca went to visit his son. The son was worried: 'Father, I'm very excited because I invested all my money in these pots.",
                "If the weather is sunny and they dry, I will become rich.",
                "If it rains, they will all crack, and my mother will cry,' he said.",
                "Hoca went sadly to his other son. The son was sitting in his field, thinking:",
                "– Ah, welcome father. I invested all my money in this field. If it's sunny, I'll have a good harvest.",
                "If it rains, the crops will rot, and my mother will cry,' he said.",
                "Hoca, after listening to both of his sons, laughed to himself:",
                "– It's a good thing we don't have a daughter. We would have spent her money too,' he said.",
                
                "One day, Nasreddin Hoca bought a kilo of salt from the market. On the way home, he saw a group of children by the side of the road.",
                "One of the children ran up and asked for the salt in Hoca's hand.",
                "Hoca looked at the child in surprise and asked: 'Okay, but why do you need so much salt?",
                "The child replied with a smile: 'My mom forgot to put salt in the food, so I'm going to take this instead.'",
                
                "One day, Nasreddin Hoca went to the mosque. While the congregation was praying, Hoca was looking around.",
                "The mosque imam got uncomfortable and called out to Hoca: 'Hoca, why aren't you focused on prayer?",
                "Hoca replied: 'My mind is constantly occupied with the dream of distributing money during the prayer. I'm waiting for the day when a rich person dies, maybe something will come to me.'",
                
                "One day, when Nasreddin Hoca came out of the jeweler's shop, a bunch of children appeared by his side. One of the children asked:",
                "– Uncle Hoca, did you buy gold?, he said.",
                "Hoca laughed and replied: 'Yes, I bought gold.'",
                "The children shouted with joy: 'Since when have you been buying gold, Uncle Hoca?",
                "Hoca replied: 'Whenever I find borrowed money, I immediately buy gold,' he said."
            ]
            }
        self.onceki_fikra_index = None
    def bir_fikra_getir(self):
        yeni_index = self.onceki_fikra_index
        while yeni_index == self.onceki_fikra_index:
            yeni_index = random.randint(0, len(self.fikralar[self.dil]) - 1)

        self.onceki_fikra_index = yeni_index
        return f"{self.isim} diyor ki:\n{self.fikralar[self.dil][yeni_index]}"

secilen_dil = input("Lütfen dil seçin/Please select your language (tr/en): ").lower()
kullanici_isim = input("Lütfen isminizi girin/Write your name: ")
nasreddin_hoca = NasreddinHoca(kullanici_isim, secilen_dil)
print(nasreddin_hoca.bir_fikra_getir())
