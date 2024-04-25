### ZADATAK:
Napravite program koji će za ulaz primiti 2D koordinate točaka A, B, C i X. Neka se koordinate učitavaju iz datoteke. Program treba:
1. provjeriti mogu li te tri točke biti vrhovi pravokutnika. Ukoliko ne mogu, program mora kontrolirano prestati s radom te obavijestiti korisnika o pogrešci,
2. provjeriti nalazi li se točka X unutar pravokutnika ABC te obavijestiti korisnika o rezultatu,
3. izračunati dijagonalu lika.

Dodatak

- ovisno o točkama A, B i C, program treba prepoznati o kojoj se vrsti pravokutnika radi (pravokutnik ili kvadrat) te za svoje izvršavanje treba dinamički odrediti koje će se klase ili funkcije pozvati
- proširite program da moze podržavati unos točaka A, B, C, D i X od kojih svaka ima po 3 dimenzije. Neka program provjerava mogu li točke A, B, C i D biti vrhovi jednog kvadra. Neka provjeri nalazi li se točka X unutar kvadra ABCD. Neka izračuna prostornu dijagonalu.
- napravite da program radi s arbitrarnim brojem dimenzija sve iz prethodnog zadatka

<hr>



### RJEŠENJE:

Datoteka **pravokutnik.py** daje rješenje za **osnovni dio zadatka i prvu točku dodatka**.

Datoteka **kvadar.py** daje rješenje za **drugu i treću točku dodatka**.

<br>

**pravokutnik.py**
. učitava koordinate iz datoteke, te ih pohranjuje u listu Numpy nizova
- provjerava čine li zadane točke vrhove pravokutnog trokuta. U tom slučaju, zadane točke ujedno čine i vrhove pravokutnika.
- provjerava nalazi li se točka X unutar pravokutnika na način da definira koordinatne granice pravokutnika i uspoređuje ih sa koordinatama točke X
- računa duljinu dijagonale na način da prvo definira udaljenosti između svih parova zadanih točaka (drugim riječima stranice pravokutnog trokuta), te zatim definira najdulju stranicu koja je ujedno i dijagonala pravokutnika
- provjerava koju vrstu pravokutnika čine zadani vrhovi na način da prvo određuje dvije manje udaljenosti u sustavu zadanih točaka, te zatim preko klase definira vrstu pravokutnika

<br>

**kvadar.py**
- učitava koordinate iz datoteke, te ih pohranjuje u listu Numpy nizova
- provjerava čine li zadane točke vrhove pravokutnika ili tetraedar sa tri prava kuta. U tom slučaju, zadane točke ujedno čine i vrhove kvadra.
- provjerava nalazi li se točka X unutar kvadra, na isti način kao u pravokutnik.py
- računa duljinu dijagonale na načina da prvo provjerava postoji li zadana točka sa 3 međusobno okomita vektora. U tom slučaju, prostorna dijagonala se računa pomoću Pitagorina poučka za 3 dimenzije. U suprotnom, prostorna dijagonala je jednaka najvećoj udaljenosti između parova zadanih točaka.
- Numpy funkcije omogućavaju rad sa točkama arbitrarnih dimenzija
