
Site - ATVShop

Descriere site:
Site-ul are o pagină principală (base.html), cu un fundal care se schimbă treptat. Pe site apare un mesaj de bun venit și un
buton care duce utilizatorul pe pagina cu produse (products.html), acest lucru putând fi realizat și din bara de navigare.

Bara de navigare are următoarele opțiuni: vizualizare coș (am adăugat un efect prin care se observă numărul de produse curent
aflate în coș), buton către produse și un buton către pagina de contact. 
Pe pagina de contact am adăgat câteva date fictive, alături de redirecționări pe paginile de socializare/mail.
Pagina produse este pagina unde se regăsesc ATV-urile propuse pentru vânzare. Fiecare produs are propriul chenar, în care am
încadrat o imagine sugestivă, detalii tehnice. Sub fiecare produs apare o zonă unde se poate selecta cantitatea dorită 
(cel puțin un produs) și butonul de adaugă în coș. Acest buton actualizează automat coșul și redirecționează automat pe pagina
coșului. Acolo, utilizatorul poate vedea ce produse are în coș, în ce cantitate, cât are de plată. De asemenea, are opțiunea de a
șterge produse din coș, costul total și cantitatea de produse se actualizează automat. De pe pagina cu coșul, utilizatorul poate 
merge direct la checkout, prin butonul de finalizare comandă. De menționat că acel buton apare doar dacă există produse în coș, 
în caz contrar apare un mesaj (Coșul este gol!). Pe pagina de checkout, utilizatorul are de completat un formular cu datele sale:
nume, număr de telefon, email, adresă, cât și modalitatea de plată (card, numerar, rate, leasing). 
De asemenea, pe pagina de checkout, utilizatorul vede descrierea produsului pe care-l comandă (nume, cantitate) cât și suma pe care
va trebui s-o achite.

Datele furnizate de acesta se salvează automat înt-un document de tip .json, care va avea denumirea dată de data în care se află. Aceste
documente se vor regăsi în directorul submitted-data, în care am lăsat câteva exemple.
Un exemplu este de forma:
{
    "timestamp": "2025-05-20T22:38:21.371752",
    "full_name": "maria ioana",
    "email": "maria@gmail.com",
    "phone": "07542123",
    "address": "comuna voinesti, judetul teleorman",
    "payment_method": "leasing",
    "items": [
        {
            "id": 2,
            "name": "CFMOTO 600L OVERLAND",
            "price": 7900,
            "quantity": 1
        }
    ],
    "total_price": 7900
}

Formularul verifică dacă formatul este unul corect, mai ales la email (trebuie să conțină @, . etc), și verifică și dacă fiecare 
câmp a fost completat sau nu. 
După plasarea comenzii, apare un mesaj de mulțumire pentru comandă, cât și numele utilizatorului trecut în formular. De asemenea, 
cantitatea coșului devine automat 0. Adresa site-ului va fi de forma:
/thank_you?name=nume+nume+....

În colțul din dreapta sus se poate observa logo-ul site-ului, care duce la pagina principală atunci când este apăsat.

Am adăgat câteva efecte/animații pentru butoanele din navbar, pentru anumite zone de text, pentru chenarele produselor. Un astfel
de efect constă în mărirea, extinderea zonei în momentul în care cursorul se află în acea zonă. Am încercat să creez un fundal dinamic, 
cu mai multe imagini interesante cu ATV-uri care rulează în fundal. 


Implementare:

Am folosit html pentru a crea paginile (base.html, products.html, checkout.html, cart.html, thank_you.html), am folosit flask pentru a
crea server.py, de unde și rulez site-ul folosind python3 server.py. Acolo creeez rutele, se pleacă de la / (base.html), cât și meniul
cu produse din checkout, posibilitatea de a calcula automat prețul total, actualizare număr produse aflate în coș etc. Practic, tot ce
se află în spatele site-ului are la bază scriptul de python, ce folosește flask. Menționez că rulez flask întru-un mediu virtual (venv).

Am folosit template Jinja2 pentru aspectul site-ului în timpul rulării folosind flask pe localhost, port 5000. Acest aspect se poate observa
și în fișierele .html. Cu excepția paginii products.html (care are stilul propriu extras din style1.css), celelate pagini moștenesc stilul
dat de pagina principală base.html (stilul din style.css), moștenit folosind comanda extends din Jinja2. Deci, style.css stilizează toate 
paginile cu excepția products.html. 

Am creat și fișierul requirements.txt, folosind comanda pip freeze > requirements.txt. 

IMPORTANT: 
Am creat și un dockerfile, dar nu am reușit să-l testez, întrucât folosesc WSL1, iar dockerfile nu este suportat de un astfel de format.
Eu testez site-ul în modul următor:
-folosesc: python3 server.py și iau adresa dată de script (http://localhost:5000/ sau adresa care-mi este returnată de script în terminal). 
Rulez python3 server.py după ce trec în mediul virtual, anume venv. Dau comanda source venv/bin/activate, pentru a nu a avea erori cauzate de
flask.
Dacă apar probleme cu rularea dockerfile-ului, vă rog să încercați cu rularea scriptului de python, care folosește flask.

Pe http://localhost:5000/, după comanda python3 server.py, site-ul arată în mod corespunzător, cu template-ul de Jinja2 și cu aspectul dat de
fișierele .css.

Imaginile au fost preluate de pe Internet, de la adresele:

https://www.cfmoto.ro/
https://www.atvrom.ro/

Timp de implementare: aproximativ 20 ore
Probleme întâmpinate pe parcursul construirii site-ului: Implementarea completă a server.py, respectiv a metodelor de actualizare automată
a coșului, de trimitere a datelor din formularul de pe pagina checkout.html. 

Voi atașa în arhivă și câteva screen-shoturi cu principalele pagini/funcții ale site-ului.