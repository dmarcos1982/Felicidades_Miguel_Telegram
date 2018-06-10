# -*- coding: utf-8 -*-


NAME = 'Name of the room'
DESCRIPTION = 'Initial description'
EXAMINATION = 'Description after examine'
VISITED = False
SOLVED = False
ITEMS = 'Items in the room'
UP = 'n', 'norte'
DOWN = 's', 'sur'
LEFT = 'o', 'oeste'
RIGHT = 'e', 'este'

visited_places = {'a0': False,
                  'b0': False, 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 }

zonemap = {
    'a0': {
        'NAME': '*Clase 010*',
        'DESCRIPTION': """Ante ti tienes un pupitre de color crema con remaches metálicos de color rojo burdeos. Sobre él hay un folio y un boli bic de color azul. Lees el encabezado del folio:\n
"EXAMEN DE SEÑALES RECTANGULARES (SR) – SEPTIEMBRE 2007"\n
Una voz cuyo recuerdo creías olvidado retumba: "¡Últimos cinco minutos!"\n
Miras hacia el origen de esa voz... "¿Quién ha invitado a Juan Blas a mi boda?" te preguntas.\n
Miras a tu alrededor y te das cuenta de que no estás en el salón de tu boda. ¡Estás en un aula de teleco! Un sudor frío recorre tu espalda. "¿Qué ha pasado?" se te ha debido de escapar en alto, porque un Millán once años más joven te replica a tu izquierda, al otro lado del pasillo del aula "Pues que el tiempo vuela, tío, qué va a haber pasado". Aquí y allá reconoces caras, caras que te consta que tienen más arrugas o menos pelo por encima. Caras que hasta hace un momento estaban recubiertas de maquillaje o coloradas de borrachera. Bastantes caras que no ves desde 2007.\n
Evocas de nuevo la mirada maliciosa del supuesto primo de Estefanía. "¡Qué cabrón!", piensas. Por algún motivo que desconoces, te ha entregado un artilugio que te ha hecho volver a tu último examen en la universidad… El caso es que Juan Blas ha anunciado hace un momento que se acaba el tiempo y tú tienes la hoja en blanco, ni siquiera has escrito tu nombre.\n
Puedes ver un boli y a Juan Blas.

¿QUÉ HACES?""",
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'ITEMS': 'boli',
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
        },
    'b0': {
        'NAME': '*La Plaza*',
        'DESCRIPTION': 'Hacia el _norte_ puedes ir al *TRASTERO*. Al _este_, al *TESTARROSA*. Al _oeste_, a *LA DUCHA*. Y al _sur_ al *TENERÉ*. *¿Hacia dónde te apetece ir?*',
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': 'b1',
        'DOWN': 'b3',
        'LEFT': 'b4',
        'RIGHT': 'b2',
        },
    'b1': {
        'NAME': '*El Trastero*',
        'DESCRIPTION': """En lo más profundo de tu cabeza empiezas a escuchar una voz tenue que poco a poco se hace más fuerte. Una voz que te resulta familiar…
_¡Despierta! ¡Arriba chico! ¡No entiendo cómo los peores mangurrianes tienen que acabar siempre en mi bar!… en mis tiempos ya te hubiéramos echado al pilón del pueblo para que te refrescaras._
¡Te has quedado dormido en la entrada del Trastero! Tu mirada caleidoscópica observa perpleja como la cara de José, el dueño del Trastero, se multiplica por cuatro mientras gira acompasada en el sentido de las agujas del reloj. Intentas seguir una de las caras pero del mareo te vuelves a caer al suelo.
_¡Vamos chico! ¡Arriba! ¡Que no tengo toda la noche! … ¡y vaya amigos los tuyos! Poco han tardado en dejarte aquí solo a que durmieras la mona… Si no fuera porque me han pagado un extra para que te guardara a buen recaudo las llaves de tu casa, pensaría que son un poco cabrones… jeje… bueno, realmente lo son…_
Las carcajadas de Jose resuenan en tu cabeza y tu cerebro, seco cual esponja en el desierto, sabe que no se avecina nada bueno. Sin embargo, poder volver a tu antiguo piso de estudiante te vendrá bien para recuperarte de la resaca y pensar cómo salir de esta pesadilla…""",
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b0',
        'LEFT': '',
        'RIGHT': '',
        },
    'b2': {
        'NAME': '*Testarrosa*',
        'DESCRIPTION': 'Vas directo a la barra. *¿Qué pides?*',
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': 'b0',
        'RIGHT': '',
        },
    'b3': {
        'NAME': '*Tenere*',
        'DESCRIPTION': """Es jueves y en el Teneré hay Black Jack. Después de tomarte la primera copita decides probar suerte.
Sobre la mesa hay una J y un 4 y el crupier te pregunta: *¿Pides carta o te plantas?*""",
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': 'b0',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
        },
    'b4': {
        'NAME': '*La Ducha*',
        'DESCRIPTION': '¡Cómo te gusta sentirte joven e ir a garitos donde todavía se practican juegos de beber!, ¿eh? Pero como ya tienes una edad, tampoco puedes elegir juegos que te líen mucho la cabeza. Juegas a un caballero del 3 simplificado. Eres el caballero del 3 y bebes un sol y sombra siempre que saques un múltiplo de 3. Tienes los dados en la mano, así que llegados a este punto, sólo puedes hacer una cosa...',
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'b0',
        },
    'b4a': {
        'NAME': '*En el baño de la Ducha*',
        'DESCRIPTION': '¡Qué alivio! Ya puedes seguir de fiesta mucho más relajado. Quieres volver al bar pero… ¡oh, cielos! ¡La puerta se ha atascado! No hay forma de moverla. Hay una ventana abierta en la pared que tienes enfrente, pero está como metro y medio por encima de tu cabeza. Hay un retrete justo debajo de la ventana, con una cadena de las antiguas suspendida del techo, y a la derecha, el lavabo. No hay papel higiénico.',
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': '',
        },
    'z0': {
        'NAME': '*Residencia Universitaria Alfonso VIII*',
        'DESCRIPTION': 'La Residencia Universitaria Alfonso VIII siempre es un buen refugio para hombres como tú en tus circunstancias. Aspiras el aroma a comida de hospital que se difunde sin escapatoria por sus pasillos cuando te topas de frente con el director.\n\n_Pero... ¡Señor Tutor de Planta! ¿Qué hace ahí con las manos en los bolsillos? ¿Ha terminado la tarea que le encomendé?_\n\nTe quedas perplejo ante tal pregunta... *¿Qué tarea te había encomendado el director?*',
        'EXAMINATION': 'Description after examine',
        'VISITED': False,
        'SOLVED': False,
        'UP': '',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': ''
    }
}