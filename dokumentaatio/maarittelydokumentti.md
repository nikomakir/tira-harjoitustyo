# Määrittelydokumentti

Tämä ohjelma tehdään harjoitustyönä osana tietojenkäsittelytieteen kandiohjelmaa (TKT) Helsingin yliopiston kurssille Aineopintojen harjoitustyö: Algoritmit ja tekoäly. Ohjelmointikielenä toimii Python (en hallitse muita kieliä siinä määrin, että pystyisin vertaisarvioimaan niitä). Dokumentaatio ja ohjelman kieli on suomi, mutta ohjelmakoodi kirjoitetaan englanniksi.

## Tieteellinen laskin

Tavoitteena on toteuttaa tietellinen laskin, joka laskee matemaattisen lausekkeen arvon ja palauttaa sen käyttäjälle. Tämä arvo voidaan myös sijoittaa muuttujaan ja tallennettuja muuttujia voi käyttää laskutoimituksissa. Lauseke voi koostua lukuarvoista, muuttujista, peruslaskutoimituksista sekä yhden tai kahden parametrin funktioista.

Tavanomaisessa muodossa olevan laskutoimituksen laskeminen on ongelmallista, koska lauseke saattaa sisältää sulkuja ja eri arvojärjestyksen eli presedenssin laskutoimituksia. Tällöin koko lauske pitäisi lukea ensin loppuun saakka, jotta voidaan olla varmoja laskujärjestyksestä. Ihmisille tuttua kirjoitusmuotoa kutsutaan infix -notaatioksi. Niin kutsutun Shunting yard -algoritmin avulla voidaan annettu infix -notaatio muuttaa postfix -notaatioksi eli niin kutsutuksi Reverse Polish -notaatioksi (RPN). Shunting yard -algoritmi käyttää pinoa ja jonoa muunnoksessa. Reverse Polish notaatiossa ei tarvita sulkuja, ja operaattori kohdistuu aina kahteen edelliseen operandiin. Näin saatu jono voidaan tehokkaasti käsitellä erikseen pinon avulla. 

Käytännössä ohjelma käyttää Shunting yard algoritmia infix -notaation muunnoksessa RPN:ksi. Pinon toteutus tehdään tavallisella python -listalla ja jono deque:lla. Jono käsitellään pinolla, joka toteutetaan myös listana. Muuttujat tallenetaan hajautustauluun eli pythonin sanakirjaan.

Ohjelman aika- ja tilavaativuus on _O(n)_.

## Vaatimukset

- Ohjelma toimii komentoriviltä
- Syötteenä annetaan matemaattinen lauseke infix -muodossa
    - Ohjelma antaa yksilöidyn virheilmoituksen, jos annettu syöte on vääränlainen
    - Annettu lauseke muutetaan infix -notaatiosta Reverse Polish -notaatioksi, jonka avulla lasketaan palautettavan lausekkeen arvo
- Hyväksyttyjä laskutoimituksia ovat summa, erotus, kerto- ja jakolasku ja potenssi (+, -, *, %, ^)
    - Yhden parametrin funktioita sini, kosini, tangentti ja neliöjuuri (sin, cos, tan, sqrt)
    - Kahden parametrin funktioita min, max
- Käytettävissä olevat muuttujat ovat a-z
- Ohjelma palauttaa validin lausekkeen arvon, jonka voi tallentaa muuttujaan

## Viitteet

- [Wikipedia: Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
- [Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
- [YouTube: Shunting yard algorithm](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
- [YouTube: Postfix stack evaluator](https://www.youtube.com/watch?v=bebqXO8H4eA)
