# 2. ÖDEV 3. SORU

from collections import Counter

def en_sık_harf_bul(metin):
    harfler = [harf for harf in metin if harf.isalpha()]  
    harf_sayilari = Counter(harfler)                        # Harfin sayısını hesaplar
    en_sık_harf, en_sık_gecis = harf_sayilari.most_common(1)[0]  # 
    return en_sık_harf

metin = input("Adınız ve soyadınız geçen en az 7 kelimeli bir metin girin: ")
sık_harf = en_sık_harf_bul(metin)
print(f"Girilen metinde en sık geçen harf: {sık_harf}")