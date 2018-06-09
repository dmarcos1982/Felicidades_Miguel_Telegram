# -*- coding: utf-8 -*-

# Importamos el mapa
import World.map as map

# Librería de la API del bot
import telebot
# Tipos para la API del bot
from telebot import types
# Librería para hacer que el programa que controla el bot no se acabe.
import time
# Libreria para los temporizadores
from threading import Timer
# Libreria para los numeros aleatorios
from random import randint

# Token del bot
TOKEN = 'BotToken'


# Creamos la clase del jugador
class player():
    def __init__(self):
        self.location = 'a0'
        self.gameOver = False
        self.inventory = []
        self.examenStarted = False
        self.bjPlayedRounds = 0
        self.s3PlayedRounds = 0
        self.trasteroQuestionsAnswered = 0
        self.testarrosaSung = 0
        self.diabolicHen = 0

# Instanciamos el jugador
myPlayer = player()


# Funcion para inicializar el juego
def game_initialize():
    myPlayer.location = 'a0'
    myPlayer.gameOver = False
    myPlayer.inventory = []
    myPlayer.examenStarted = False
    myPlayer.bjPlayedRounds = 0
    myPlayer.s3PlayedRounds = 0
    myPlayer.trasteroQuestionsAnswered = 0
    myPlayer.testarrosaSung = 0
    myPlayer.diabolicHen = 0


# Creamos una lista de articulos para manejar los objetos
articleList = ['el', 'la', 'los', 'las', 'un', 'una']

# Creamos el objeto de nuestro bot.
bot = telebot.TeleBot(TOKEN)



# Texto de introduccion
display_intro = """Has tenido la inmensa suerte de encontrar a tu media naranja y, además, esta chica que te comprende, que llena tus noches y tus sueños, ha accedido a casarse contigo.\n
Organizar la boda no ha sido tan fácil como te imaginabas en un principio, pero todas las dificultades ya han sido vencidas y el gran día ha llegado.\n
Esta mañana Estefanía te ha dado el 'Sí, quiero' en su resplandeciente vestido blanco, los ojos le brillaban como nunca y tú… Tú estás en una nube de la que no te quieres bajar. Estás en el salón de tu boda, ha empezado la barra libre hace un ratito y todos tus invitados bailan o, al menos, intentan mover la cabeza y los dedos de los pies al ritmo de la música mientras consumen con fruición gin-tonics, whysky-colas y vodka-naranjas.\n
Tu deslumbrante esposa está dándolo todo en la pista con sus amigas mientras las inconfundibles voces de 'Siempre Así' a todo volumen hacen casi imposible el mantener una conversación. Así, no has entendido una sola palabra de las que te ha dicho un joven, más o menos de la edad de Estefanía, al tiempo que te encasquetaba un voluminoso paquete envuelto en papel de regalo. No tienes ni idea de quién era el chico, pero bueno, te pasa con muchos de los invitados, así que das por supuesto que se trata de algún primo lejano de tu mujer.\n
Como la canción de 'Siempre Así' es larguísima y tú no tienes nada mejor que hacer en ese momento, empiezas a romper el envoltorio del regalo que acabas de recibir, mientras recuerdas la sospechosa mirada de la persona que te lo ha dado… No sabes decir el qué pero hay algo raro en ese chico… Tienes ante ti una caja de cartón normal y corriente. Levantas la tapa y…\n\n"""


# Funcion para mostrar nombre de la habitacion y descripcion
def introduce_room(m):
    bot.send_message(m.chat.id, '\n' + map.zonemap[myPlayer.location]['NAME'], parse_mode='Markdown')
    time.sleep(1)
    bot.send_message(m.chat.id, '\n' + map.zonemap[myPlayer.location]['DESCRIPTION'], parse_mode='Markdown')

# Teleco
# PROBABLEMENTE MODIFIQUE EL QUE SE PUEDA RESPONDER DIRECTAMENTE CON EL VALOR, SIN TENER QUE PONER RESPONDER, CONTESTAR O ESCRIBIR ANTES
def room_examen(m):
    # Si expira el timer inicializamos el juego y muere miserablemente
    def timeout():
        if myPlayer.examenStarted is True:
            game_initialize()
            bot.send_message(m.chat.id, "El tiempo del examen ha expirado. Juan Blas va recogiendo los exámenes por los pupitres. Cuando llega a tu puesto, tú te aferras al folio porque no lo has rellenado y realmente quieres hacer ese examen y terminar la carrera de una puñetera vez. El breve tira y afloja es vencido por Juan Blas, que tira con decisión de la hoja de papel y te deja un corte horrendo en la palma de la mano. No tienes al día las dosis de recuerdo de la vacuna antitetánica. La herida se te infecta y *mueres miserablemente*.\n\nIntroduce _/start_ para iniciar de nuevo el juego.")

    # Inicializamos el timer del examen
    tExamen = Timer(300.0, timeout)

    # Solo iniciamos el timer cuando se inicia el juego
    if myPlayer.examenStarted is False:
        myPlayer.examenStarted = True
        tExamen.start()

    # Abrimos la imagen que contiene el problema del examen
    cuadripolo = open('Recursos/cuadripolo.png', 'rb')
    # Comandos que entendemos en esta habitacion
    acceptableExamenActions = ['coger', 'responder', 'contestar', 'escribir', 'decir']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    # Si la primera palabra no esta en la lista de los comandos que entendemos, no hacemos nada
    if mSplit[0] not in acceptableExamenActions:
        bot.send_message(m.chat.id, "No entiendo eso que dices")
    # Si quiere coger algo
    elif mSplit[0] == "coger":
        # Si quiere coger el boli
        if "boli" in mSplit:
            # Si aun no ha cogido el boli
            if 'boli' not in myPlayer.inventory:
                # Añadimos el boli al inventario
                myPlayer.inventory.append("boli")
                # Le mostramos la pregunta del examen
                bot.send_message(m.chat.id, "Con mano temblorosa coges el bolígrafo y lees el enunciado de la única pregunta que hay en el folio: Una instalación de telefonía está compuesta por un cuadripolo transmisor, un generador y un receptor. Determinar la potencia máxima que puede recibir el receptor.")
                bot.send_photo(m.chat.id, cuadripolo)
            else:
                bot.send_message(m.chat.id, "Ya tienes el boli")
        # Si lo que quiere coger no existe, no hacemos nada
        else:
            bot.send_message(m.chat.id, "No veo eso que dices")
    # Si quiere responder el examen
    elif ((mSplit[0] == "responder") or (mSplit[0] == "contestar") or (mSplit[0] == "escribir")):
        # Si no ha cogido el boli previamente, no puede hacerlo
        if 'boli' not in myPlayer.inventory:
            bot.send_message(m.chat.id, "No se como vas a hacer eso sin el boli")
        else:
            # Si responde correctamente, paramos el temporizador y pasamos al Tenere
            if ((mSplit[1] == '49uw') or ((mSplit[1] == '49') and (mSplit[2] == 'uw'))):
                tExamen.cancel()
                myPlayer.examenStarted = False
                bot.send_message(m.chat.id, "¡Enhorabuena, Miguel! Has terminado la carrera y sales a celebrarlo con tus amigos (bueno, sabes que tienes que intentar volver a tu boda de alguna manera, pero ¿a quién no le apetece reverdecer viejos laureles de vez en cuando?).")
                map.zonemap[myPlayer.location]['VISITED'] = True
                myPlayer.location = 'b3'
                time.sleep(2)
                introduce_room(m)

    # Si quiere hablar con Juan Blas
    elif mSplit[0] == "decir":
        # Si decide no presentar vamos al Alfonso VIII
        if ((mSplit[1] == 'no') and (mSplit[2] == 'presentar')):
            bot.send_message(m.chat.id, "Alfonso VIII")
        # Cualquier otra cosa que diga, Juan Blas le dice que solo hay una cosa que entiende
        else:
            bot.send_message(m.chat.id, "Juan Blas te mira con mala cara y te dice: _Si quieres irte y 'no presentar' no tienes mas que decirlo_", parse_mode='Markdown')


# Tenere
def room_tenere(m):
    # Comandos que entendemos en esta habitacion
    acceptableTenereActions = ['si', u'sí', 'no', 'plantarme', 'plantarse', 'pedir']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    # Bucle del blackjack
    def blackjack_loop():
        rNumber = randint(0, 9)
        print (rNumber)
        if 0 <= rNumber <= 4:
            bot.send_message(m.chat.id, 'El crupier reparte de nuevo. Tienes una buena jugada en la mesa, así que pides otra carta. Pero desde luego hoy no es tu noche y te pasas de nuevo. Pero este estúpido juego no va a poder contigo, ¿o sí? *¿Deseas jugar otra partida?*', parse_mode='Markdown')
        elif 5 <= rNumber <= 9:
            bot.send_message(m.chat.id, 'Esta vez decides ser más conservador y te quedas cerca del BlackJack. Cuando el crupier levanta su carta observas con incredulidad cómo la suma de sus cartas es 21. Encima pone una sonrisilla de suficiencia que le borrarías de la cara con un guantazo. El crupier recoge la mesa y te dice: *¿Deseas jugar otra partida? Esto al final es cuestión de estadística...*', parse_mode='Markdown')

    # Marcamos la habitacion como visitada
    map.zonemap[myPlayer.location]['VISITED'] = True    

    # Si la primera palabra no esta en la lista de los comandos que entendemos, no hacemos nada
    if mSplit[0] not in acceptableTenereActions:
        bot.send_message(m.chat.id, "No entiendo eso que dices")
    # La primera vez que responde solo puede hacerlo con pedir carta, plantarme o plantarse
    elif myPlayer.bjPlayedRounds == 0:
        # Si se planta vamos al Alfonso VIII
        if ((mSplit[0] == 'plantarme') or (mSplit[0] == 'plantarse')):
            bot.send_message(m.chat.id, "Alfonso VIII")
        elif ((mSplit[0] == 'si') or (mSplit[0] == u'sí')):
            bot.send_message(m.chat.id, '¿Sí qué?')
        elif mSplit[0] == 'no':
            bot.send_message(m.chat.id, '¿No qué?')
        elif mSplit[0] == 'pedir':
            if "carta" in mSplit:
                bot.send_message (m.chat.id, 'Parece que la suerte del exámen no te ha acompañado ahora, sacas una figura y te pasas. El crupier te desea mejor suerte la próxima vez y antes de volver a repartir te pregunta: *¿Deseas jugar otra partida?*', parse_mode='Markdown')
                myPlayer.bjPlayedRounds += 1
            else:
                bot.send_message(m.chat.id, "No veo eso que dices")
        else:
            bot.send_message(m.chat.id, "No entiendo eso que dices")

    elif 1 <= myPlayer.bjPlayedRounds <= 3:
        # Si decide jugar, iniciamos el bucle del blackjack
        if ((mSplit[0] == 'si') or (mSplit[0] == u'sí')):
            blackjack_loop()
            myPlayer.bjPlayedRounds += 1
        # Si decide no jugar vamos al Alfonso VIII
        elif mSplit[0] == 'no':
            bot.send_message(m.chat.id, "Alfonso VIII")
        else:
            bot.send_message(m.chat.id, "No entiendo eso que dices")

    # Una vez llega al numero de partidas indicado puede elegir el premio
    elif myPlayer.bjPlayedRounds == 4:
        bot.send_message(m.chat.id, 'El crupier reparte las cartas y tienes un 4 y un 6 sobre la mesa. No te queda otra que pedir carta... así que la pides ¡y sale un as! Por fin la suerte (esa perra caprichosa) ha decidido cambiar de bando. El crupier, ya cansado y con ganas de irse a su casa te da la enhorabuena y te pregunta: *¿Qué quieres pedir de premio?*', parse_mode='Markdown')
        myPlayer.bjPlayedRounds += 1

    elif myPlayer.bjPlayedRounds == 5:
        if mSplit[0] == 'pedir':
            if ((' '.join(mSplit[1::]) == 'dos botellas de bourbon') or (' '.join(mSplit[1::]) == '2 botellas de bourbon')):
                bot.send_message(m.chat.id, 'El camarero te da tus dos botellas de Bourbon. Con ellas bajo el brazo decides que es hora de cambiar de garito, así que sales a la plaza a decidir cual será tu próximo destino.')
                # Añadimos las dos botellas de Bourbon al inventario
                myPlayer.inventory.append("dos botellas de bourbon")
                # Marcamos la habitacion como resuelta
                map.zonemap[myPlayer.location]['SOLVED'] = True
                # Movemos al jugador a la plaza
                myPlayer.location = 'b0'
                time.sleep(2)
                introduce_room(m)
            else:
                bot.send_message(m.chat.id, 'De eso no tenemos, pide otra cosa')
        else:
            bot.send_message(m.chat.id, "No entiendo eso que dices")


# La Ducha
def room_ducha(m):
    # Comandos que entendemos en esta habitacion
    acceptableDuchaActions = ['tirar']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    # Marcamos la habitacion como visitada
    map.zonemap[myPlayer.location]['VISITED'] = True

    # Si la primera palabra no esta en la lista de los comandos que entendemos, no hacemos nada
    if mSplit[0] not in acceptableDuchaActions:
        bot.send_message(m.chat.id, "No entiendo eso que dices")
    else:
        if 'dados' in mSplit:
            if 0 <= myPlayer.s3PlayedRounds <= 4:
                dice1Number = randint(1, 6)
                dice2Number = randint(1, 6)
                # Si la suma de los dados es multiplo de 3, bebe
                if ((dice1Number + dice2Number)%3) == 0:
                    bot.send_message(m.chat.id, '¡Has sacado un ' + str(dice1Number+dice2Number) + '! Procedes a beberte ese sol y sombra que te toca.')
                    myPlayer.s3PlayedRounds += 1
                # Si no, mostramos la suma
                else:
                    bot.send_message(m.chat.id, 'Sacas un ' + str(dice1Number+dice2Number))
            # Cuando llega a 5 partidas, pasa al baño de la ducha
            if myPlayer.s3PlayedRounds == 5:
                bot.send_message(m.chat.id, 'Ha sido divertido pero basta ya de jueguecitos por hoy. La verdad es que ya llevas un buen rato bebiendo y el señor Roca te llama a gritos, por lo que entras en el baño.')
                # Movemos al jugador al baño
                myPlayer.location = 'b4a'
                time.sleep(2)
                introduce_room(m)
        # No puede tirar otra cosa que no sean los dados
        else:
            bot.send_message(m.chat.id, "No entiendo eso que dices")


# El baño de la Ducha
def room_bano_ducha(m):
    # Comandos que entendemos en esta habitacion
    acceptableBanoDuchaActions = ['subir', 'subirte', 'abrir', 'tirar']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    # Si la primera palabra no esta en la lista de los comandos que entendemos, no hacemos nada
    if mSplit[0] not in acceptableBanoDuchaActions:
        bot.send_message(m.chat.id, "No entiendo eso que dices")
    # Si decide subirse al retrete, muere miserablemente
    elif ((mSplit[0] == 'subir') or (mSplit[0] == 'subirte')):
        if 'retrete' in mSplit:
            bot.send_message(m.chat.id, 'La endeble tapa se hunde y te quedas atascado. Gritas pidiendo auxilio pero nadie puede entrar a rescatarte porque la puerta del baño está atascada. Pasa el tiempo, dejas de sentir las piernas. En cuestión de horas la gangrena te corroe y *mueres miserablemente*.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
            game_initialize()
        else:
            bot.send_message(m.chat.id, 'No veo eso que dices.')
    # Si decide tirar de la cadena, muere miserablemente
    elif mSplit[0] == 'tirar':
        if 'cadena' in mSplit:
            bot.send_message(m.chat.id, 'Como estás un poco borracho, te haces un lío con la cadena y acabas ahorcándote. *Mueres miserablemente*.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
            game_initialize()
        else:
            bot.send_message(m.chat.id, 'No veo eso que dices.')
    # Si decide abrir el grifo, resuelve el puzzle y vuelve a la Plaza
    elif mSplit[0] == 'abrir':
        if 'grifo' in mSplit:
            bot.send_message(m.chat.id, '¡Qué astuto, Miguel! Esta solución digna de dibujos animados es la que te salva la vida. El baño se va inundando poco a poco. Te mantienes a flote y, cuando el nivel del agua es lo suficientemente elevado, consigues salir por la ventana. ¡Enhorabuena! Pero ahora estás completamente calado… ni que acabaras de salir de La Ducha (LoL). Así no puedes volver a tu boda, de ninguna manera, qué dirá tu suegra. Lo mejor es que sigas de bares a ver si algún camarero amigo te puede dejar algo con lo que secarte, aunque sea el trapo de secar los vasos, que no ha visto una lavadora desde 1999.')
            myPlayer.location = 'b0'
            time.sleep(2)
            introduce_room(m)
        else:
            bot.send_message(m.chat.id, 'No veo eso que dices.')


# El Trastero
def room_trastero(m):
    # Comandos que entendemos en esta habitacion
    acceptableTrasteroActions = ['pedir', 'decir', 'hablar', 'si', u'sí', 'no', '24', 'veinticuatro', '10', 'diez', '4', 'cuatro']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    # Marcamos la habitacion como visitada
    map.zonemap[myPlayer.location]['VISITED'] = True

    # Si la primera palabra no esta en la lista de los comandos que entendemos, no hacemos nada
    if mSplit[0] not in acceptableTrasteroActions:
        bot.send_message(m.chat.id, "No entiendo eso que dices")
    # Si todavia no le ha dicho si se atreve
    elif myPlayer.trasteroQuestionsAnswered == 0:
        if ((mSplit[0] == 'si') or (mSplit[0] == u'sí')):
            bot.send_message(m.chat.id, '¿Sí qué?')
        elif mSplit[0] == 'no':
            bot.send_message(m.chat.id, '¿No qué?')
        elif ((mSplit[0] == 'pedir') and ('llaves' not in mSplit)):
            bot.send_message(m.chat.id, 'No veo eso que dices.')
        else:
            bot.send_message(m.chat.id, 'Sí, efectivamente tus amigos me han dejado tus llaves, pero me han pagado muy bien para que no te las dé a no ser que aciertes la respuesta a 3 preguntas… un poco estúpidas la verdad… pero qué le voy a hacer, no seré yo el que discuta el color del dinero… ¿Te atreves?')
            myPlayer.trasteroQuestionsAnswered += 1
    # Cuando le ha planteado el juego. Primera pregunta
    elif myPlayer.trasteroQuestionsAnswered == 1:
        if ((mSplit[0] == 'si') or (mSplit[0] == u'sí')):
            bot.send_message(m.chat.id, '_Primera pregunta:_ *¿Cuál es el record mundial, en días, de tuppers olvidados en la nevera?*', parse_mode='Markdown')
            myPlayer.trasteroQuestionsAnswered += 1
        # Si dice que no, vuelve a la Plaza - REVISAR
        elif mSplit[0] == 'no':
            bot.send_message(m.chat.id, 'Con toda la cogorza te vuelves a la plaza.')
        # Si dice cualquier otra cosa, vuelve a la Plaza - REVISAR
        else:
            bot.send_message(m.chat.id, 'A Jose se le acaba la paciencia y decide que no va a darte las llaves, así que te vuelves a la plaza.')
    # Segunda pregunta
    elif myPlayer.trasteroQuestionsAnswered == 2:
        if ((mSplit[0] == '24') or (mSplit[0] == 'veinticuatro')):
            bot.send_message(m.chat.id, '_Segunda pregunta:_ *¿Cuál es el récord mundial, en días, de ropa tendida y olvidada en el tendedero?*', parse_mode='Markdown')
            myPlayer.trasteroQuestionsAnswered += 1
        else:
            bot.send_message(m.chat.id, 'Jose te obliga a beber un chupito de Jack Daniels por haber respondido mal, pero tu cuerpo no soporta más cantidad de alcohol en sangre y *mueres miserablemente* de un coma etílico.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
            game_initialize()
    # Tercera pregunta
    elif myPlayer.trasteroQuestionsAnswered == 3:
        if ((mSplit[0] == '10') or (mSplit[0] == 'diez')):
            bot.send_message(m.chat.id, '_Tercera pregunta:_ *¿Cuál es el record mundial, en días, de ropa olvidada en el tambor de la lavadora?*', parse_mode='Markdown')
            myPlayer.trasteroQuestionsAnswered += 1
        else:
            bot.send_message(m.chat.id, 'Jose te obliga a beber un chupito de Jack Daniels por haber respondido mal, pero tu cuerpo no soporta más cantidad de alcohol en sangre y *mueres miserablemente* de un coma etílico.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
            game_initialize()
    elif myPlayer.trasteroQuestionsAnswered == 4:
        if ((mSplit[0] == '4') or (mSplit[0] == 'cuatro')):
            bot.send_message(m.chat.id, '_Toma las llaves chico, te lo has ganado. Yo no daba un duro por tí y has conseguido acertar las 3 preguntas._\nUn largo escalofrío recorre tu espalda mientras Jose saca del centro de sus pantalones las llaves de tu piso. El sudor de su entrepierna adherido al metal las hace relucir como nunca antes. Tragas saliva, extiendes la mano, las coges y con un cuidado extremo las metes en tu bolsillo mientras te convences de que no volverás nunca a este antro y vuelves a la plaza.', parse_mode='Markdown')
            map.zonemap[myPlayer.location]['SOLVED'] = True
            myPlayer.location = 'b0'
            time.sleep(2)
            introduce_room(m)
        else:
            bot.send_message(m.chat.id, 'Jose te obliga a beber un chupito de Jack Daniels por haber respondido mal, pero tu cuerpo no soporta más cantidad de alcohol en sangre y *mueres miserablemente* de un coma etílico.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
            game_initialize()


# Testarrosa
def room_testarrosa(m):
    # Comandos que entendemos en esta habitacion
    acceptableTestarrosaActions = [u'pacharán', 'pacharan', u'patxarán', 'patxaran']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    def horrible_singing_die():
        bot.send_message(m.chat.id, 'Menos mal que no te ganas la vida como vocalista, lo haces fatal. La clientela del bar, enfurecida por tu actuación, te despelleja vivo allí mismo, *muriendo miserablemente*.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
        game_initialize()

    # Marcamos la habitacion como visitada
    map.zonemap[myPlayer.location]['VISITED'] = True

    # Si la primera palabra no esta en la lista de los comandos que entendemos, no hacemos nada
    if myPlayer.testarrosaSung == 0:
        if ((mSplit[0] == u'pacharán') or (mSplit[0] == 'pacharan') or (mSplit[0] == u'patxarán') or (mSplit[0] == 'patxaran')):
            bot.send_message(m.chat.id, "Con tu tubo de pacharan en la mano, escuchas cómo el DJ pincha una canción. Todos los asistentes enardecen con ella y empiezan a sacudir violentamente sus cabezas. Cuando empieza la letra, todo el mundo corea:\n\n_Ohhhh!! De nuevo solos tú y yo. Un lago y una canción,\necho de menos oír tu voz_\n\nLa música se interrumpe bruscamente, todo el mundo calla. Todas las miradas se centran en un punto. ¡Tú! *¡Están esperando a que cantes!*", parse_mode='Markdown')
            myPlayer.testarrosaSung += 1
        else:
            bot.send_message(m.chat.id, "De eso no tenemos, pide otra cosa.")
    elif myPlayer.testarrosaSung == 1:
        if ((m.text.lower() == u'una estrella te eclipsó') or (m.text.lower() == 'una estrella te eclipso')):
            bot.send_message(m.chat.id, "_Los momentos que no volverá a sentir tu piel,\nella no deja de pensar que un día te encontrará..._\n\nDe nuevo todo el mundo calla y te mira, *es tu turno de nuevo para cantar.*", parse_mode='Markdown')
            myPlayer.testarrosaSung += 1
        else:
            # Muere miserablemente
            horrible_singing_die()
    elif myPlayer.testarrosaSung == 2:
        if ((m.text.lower() == u'acércate') or (m.text.lower() == 'acercate')):
            bot.send_message(m.chat.id, "_A veces siento al despertar como un susurro, tu calor,\nella no deja de pensar que un día te encontrará..._\n\n¡Ella! ¡Estefanía! Te estará buscando, se preguntará dónde estás… Basta de karaokes y de tragos, es hora de volver a tu boda. ¿Dónde se encontrará la salida de este bucle temporal? No tienes ni idea. De momento, intentas salir del bar, pero una montonera de objetos bloquea la salida: un *oso panda*, un *palé*, un *enano*, una *oveja*, una *gallina* y un *señor disfrazado de hitita*.", parse_mode='Markdown')
            myPlayer.testarrosaSung += 1
        else:
            # Muere miserablemente
            horrible_singing_die()
    elif myPlayer.testarrosaSung == 3:
        if (('oso' in mSplit) and ('panda' in mSplit)):
            bot.send_message(m.chat.id, '¡Pero cómo se te ocurre meterte con un oso panda, por mucho que parezca un peluche! El primer zarpazo te secciona la vena subclavia y el segundo, la yugular. *Mueres miserablemente*.\n\nIntroduce _/start_ para iniciar de nuevo el juego.', parse_mode='Markdown')
            game_initialize()
        elif 'gallina' in mSplit:
            bot.send_message(m.chat.id, 'Te has topado con un animal especialmente feroz. Esta gallina está cosiéndote a picotazos y más vale que encuentres un remedio rápido o no sabes si podrás sobrevivir. *¿Qué haces?*', parse_mode='Markdown')
            myPlayer.testarrosaSung = 10

    # Bucle de la gallina
    elif myPlayer.testarrosaSung == 10:
        if 0 <= myPlayer.diabolicHen <= 9:
            if mSplit[0] == 'darle':
                if 'bourbon' in mSplit:
                    if 'dos botellas de bourbon' in myPlayer.inventory:
                        bot.send_message(m.chat.id, 'Has emborrachado a la gallina y por fin te ha dejado de molestar, pero el resto de objetos aún bloquean la salida: un *oso panda*, un *palé*, un *enano*, una *oveja* y un *señor disfrazado de hitita*.', parse_mode='Markdown')
                        myPlayer.testarrosaSung = 4
                    else:
                        bot.send_message(m.chat.id, 'No encuentro eso que dices.')
                        bot.send_message(m.chat.id, 'La gallina continúa picoteándote.')
                else:
                    bot.send_message(m.chat.id, 'No encuentro eso que dices.')
                    bot.send_message(m.chat.id, 'La gallina continúa picoteándote.')
            else:
                bot.send_message(m.chat.id, 'La gallina continúa picoteándote.')
################################################################################


# La Plaza
def room_plaza(m):
    # Comandos que entendemos en esta habitacion
    acceptablePlazaActions = ['norte', 'sur', 'este', 'oeste']
    # Cogemos el texto que nos ha enviado y lo dividimos en palabras
    mSplit = m.text.lower().split()

    # Tenere
    if mSplit[0] == 'sur':
        bot.send_message(m.chat.id, 'Ya has estado mucho tiempo en el Teneré, casi mejor ir a otro garito, ¿no?')
    
    # La Ducha
    elif mSplit[0] == 'oeste':
        if map.zonemap['b4']['VISITED'] == True:
            bot.send_message(m.chat.id, '¿Estás seguro de que es una buena idea volver a entrar en La Ducha? Elige otro sitio.')
        else:
            myPlayer.location = 'b4'
            time.sleep(2)
            introduce_room(m)
            room_ducha(m)
    
    # Trastero
    elif mSplit[0] == 'norte':
        if ((map.zonemap['b1']['VISITED'] == True) and (map.zonemap['b1']['SOLVED'] == False)):
            bot.send_message(m.chat.id, 'Ha quedado muy claro que Jose no piensa darte las llaves, así que es mejor que elijas otro sitio.')
        elif ((map.zonemap['b1']['VISITED'] == True) and (map.zonemap['b1']['SOLVED'] == True)):
            bot.send_message(m.chat.id, 'Una vez has recuperado tus llaves, ¿no sería mejor ir a otro sitio?.')
        else:
            myPlayer.location = 'b1'
            time.sleep(2)
            introduce_room(m)
            room_trastero(m)

    # Testarrosa
    elif mSplit[0] == 'este':
        myPlayer.location = 'b2'
        time.sleep(2)
        introduce_room(m)
        room_testarrosa(m)


# Bucle principal del juego, en el que se decide en que habitacion esta
def play_rooms(m):
    if myPlayer.location == 'a0':
        room_examen(m)
    elif myPlayer.location == 'b3':
        room_tenere(m)
    elif myPlayer.location == 'b0':
        room_plaza(m)
    elif myPlayer.location == 'b4':
        room_ducha(m)
    elif myPlayer.location == 'b4a':
        room_bano_ducha(m)
    elif myPlayer.location == 'b1':
        room_trastero(m)
    elif myPlayer.location == 'b2':
        room_testarrosa(m)


# Definimos una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'
def listener(messages):
    # Por cada dato 'm' en el dato 'messages'
    for m in messages:
        # Filtramos mensajes que sean tipo texto
        if m.content_type == 'text':
            # Almacenaremos el ID de la conversación
            cid = m.chat.id
            # Y haremos que imprima algo parecido a esto -> [52033876]: /start
            print "[" + str(cid) + "]: " + m.text
        # Si se lanza el comando /start se inicia el juego
        if m.text == '/start':
            # Inicializamos el juego y le mandamos la introduccion y el texto de Teleco
            game_initialize()
            bot.send_message(cid, display_intro)
            time.sleep(2)
            introduce_room(m)
        # PARA TESTING EXCLUSIVAMENTE - HAY QUE ELIMINAR ESTOS ELIF
        elif m.text == '/tenere':
            myPlayer.location = 'b3'
            introduce_room(m)
        elif m.text == '/ducha':
            myPlayer.location = 'b4'
            introduce_room(m)
        elif m.text == '/banoducha':
            myPlayer.location = 'b4a'
            introduce_room(m)
        elif m.text == '/trastero':
            myPlayer.location = 'b1'
            introduce_room(m)
        elif m.text == '/testarrosa':
            myPlayer.location = 'b2'
            introduce_room(m)
        else:
            play_rooms(m)


# Le decimos al bot que utilice como función escuchadora nuestra función 'listener'
bot.set_update_listener(listener)

# Le decimos al bot que siga funcionando incluso si encuentra algún fallo
bot.polling(none_stop=True)
