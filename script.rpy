# ✨ Il cuore del Cyberverse di Biagio ✨

# Dichiarazione del protagonista
default Biagio = Character('Biagio', color="#E03B8B")

# Inizio dell'avventura
label start:
    "Ehi... ci sei?"
    Biagio "Perfetto, sei arrivato nel momento giusto."
    Biagio "Mi chiamo Biagio, e questo è il mio Cyberverse: un intreccio di codice, design e visione digitale."
    Biagio "Un viaggio personale tra creatività, pixel e tanta passione per il mondo tech."

label sprites:
    "Tu" "Aspetta un attimo... ma dove ti trovi esattamente?"
    show biagio
    Biagio "Bella domanda."
    Biagio "Diciamo che mi muovo tra righe di codice, interfacce curate e idee che prendono vita su schermo."

label character:
    show biagio at left
    Biagio "Ok, parliamo di me seriamente."
    show biagio with dissolve
    Biagio "Sono uno sviluppatore front-end, con solide competenze in HTML, CSS, JavaScript, React, Vue.js e Angular."
    Biagio "Mi occupo anche di UX/UI Design, creando interfacce moderne, responsive e accessibili, sempre orientate all’utente."

    Biagio "Ho frequentato l’ITS Apulia Digital Maker, dove ho approfondito programmazione, basi di dati, sicurezza informatica, CMS, version control e molto altro."
    Biagio "Ogni progetto che realizzo punta alla performance, alla SEO e a un design che lasci il segno."

label background:
    Biagio "Seguimi, ti porto in un luogo speciale."
    scene bg cyber
    with fade
    show biagio at left
    Biagio "Benvenuto nel mio universo digitale."
    Biagio "Ogni angolo racconta una storia: un'idea trasformata in progetto, una collaborazione, un sogno codificato."

label bgm:
    play music "audio/FateExtra.mp3" fadein 1.0 volume 0.5
    Biagio "Senti questa traccia? È la soundtrack del mio percorso. Energia, ritmo, visione."
    Biagio "Ma ora, abbassiamo i BPM. Ti porto dove tutto è iniziato."

    stop music fadeout 1.0
    scene bg classroom
    with fade

label sfx:
    play sound "audio/sfx_bell.mp3"
    Biagio "Ah, la campanella... Tempo di rimettersi sui banchi!"
    Biagio "Il codice non si scrive da solo — anche se a volte mi piacerebbe!"

label choices:
    default learned = False
    Biagio "Ti è arrivato qualcosa di quello che faccio e di chi sono?"
menu:
    "Sì, è stato super interessante!":
        jump choices1_a
    "Hmm, mi servono più info.":
        jump choices1_b

label choices1_a:
    Biagio "Grande! Condividere è il primo passo per innovare."
    $ learned = True
    jump choices1_common

label choices1_b:
    Biagio "Tranquillo... ogni scoperta ha il suo ritmo."
    show biagio sad
    jump choices1_common

label choices1_common:
    Biagio "Se vuoi approfondire, trovi tutti i miei progetti, tool e risorse nei link in descrizione."
    Biagio "È tutto lì, pronto a ispirarti — o magari a collaborare!"

label flags:
    if learned:
        Biagio "Se questo viaggio nel Cyberverse ti ha colpito, fammelo sapere! È solo l'inizio."
    else:
        Biagio "Nessun problema. Ci sono tanti altri mondi da esplorare — e io ti aspetto lì."

    return
    # Fine del viaggio