import streamlit as st

# Preguntas extraídas del documento PDF
questions = [
    {
        "num": 1,
        "text": "¿Cuál es tu ARQUETIPO? Cuando te diriges a las personas, utilizas palabras...",
        "options": {
            "a": "Impositivas, acusadoras, de reclamo.",
            "b": "De cortesía, educadas, simpáticas, neutras.",
            "c": "Escogidas, abstractas, complicadas, utilizas oraciones largas.",
            "d": "Jocosas, confiadas. A veces sin sentido o relación."
        }
    },
    {
        "num": 2,
        "text": "Con cuál de estas palabras te identificas más...",
        "options": {
            "a": "Independiente.",
            "b": "Disciplinado.",
            "c": "Pacífico.",
            "d": "Divertido."
        }
    },
    {
        "num": 3,
        "text": "Los contenidos más comunes en tus temas de conversación son:",
        "options": {
            "a": "Anecdotas, historias familiares, amistad.",
            "b": "Estadísticas, aspectos técnicos, tecnología, detalles y curiosidades.",
            "c": "De chistes, actividades amenas, lo que serás en el futuro, las cosas que sabes hacer.",
            "d": "De poder, influencia, control."
        }
    },
    {
        "num": 4,
        "text": "Cuando entablas una relación interpersonal, tu comunicación tiene un estilo...",
        "options": {
            "a": "Concreto y especializado, cuidadoso del estilo y confiabilidad de la información.",
            "b": "A veces vago, original, ocurrente. Orientado a ser el centro de atención.",
            "c": "Directo, concreto y orientado hacia el control. Las cosas son blancas o negras.",
            "d": "A ratos poco concreto, muy explicativo y cuidadoso, orientado a no dañar al otro."
        }
    },
    {
        "num": 5,
        "text": "Te caracterizas por ser una persona...",
        "options": {
            "a": "Mucho movimiento, gesticulaciones y expresión facial abundante.",
            "b": "Erguida, rápida y tensa, a veces rígida corporalmente.",
            "c": "Movimientos lentos y poca gesticulación, el cuerpo protege a la persona.",
            "d": "Controlas tus movimientos, quieres que sean perfectos y equilibrados. Extrema rigidez"
        }
    },
    {
        "num": 6,
        "text": "Con cuál de estas descripciones te identificas más:",
        "options": {
            "a": "Perfeccionista, todo tiene que estar en su lugar.",
            "b": "Comprensivo, comprensiva, entiendes los problemas de los demás.",
            "c": "Simpático, simpática, te invitan a fiestas y reuniones, te gusta la fiesta.",
            "d": "Osado-Osada, tomas riesgos basados en instintos. Eres impulsivo-impulsiva."
        }
    },
    {
        "num": 7,
        "text": "En conversaciones tu energía vocal es:",
        "options": {
            "a": "Bajo y monótono (poca modulación).",
            "b": "Lineal con tendencia a la pronunciación acentuada y seca.",
            "c": "Alto con modulaciones variadas. Tu ánimo la influyen a menudo.",
            "d": "Alto, intenso, avasallante a veces, duro y tenso. Algunos dicen que eres gritón."
        }
    },
    {
        "num": 8,
        "text": "Tu velocidad al hablar es...",
        "options": {
            "a": "Moderada, pausada.",
            "b": "Rápida.",
            "c": "Rápida y tajante.",
            "d": "Lenta con ritmo característico."
        }
    },
    {
        "num": 9,
        "text": "Tu expresión facial más común es...",
        "options": {
            "a": "Relajada, sonriente, muchas muecas y buen contacto visual.",
            "b": "Dura y seria, entrecejo fruncido, a veces dientes apretados y mirada fija.",
            "c": "Relajada, sonriente, muchas expresiones de empatía, cariño, etc.",
            "d": "Calmada, fija y sin expresiones evidentes. Imperturbable a veces."
        }
    },
    {
        "num": 10,
        "text": "En el escenario de ventas, su mayor fortaleza es:",
        "options": {
            "a": "Preparar la estrategia para lograr la reunión, la venta o la negociación.",
            "b": "Desarrollar relaciones, caerle bien al cliente.",
            "c": "La acción: visitar clientes, llamadas telefónicas, cerrar el negocio.",
            "d": "Descubrir nuevas formas de lograr más ventas, mantener una actitud positiva."
        }
    },
    {
        "num": 11,
        "text": "En actividades cotidianas te caracterizas por:",
        "options": {
            "a": "Ser más bien lento, no funcionas con precisión o te cuesta concentrarte.",
            "b": "Ser más bien metódico, calmado y muy ordenado.",
            "c": "Ser ansioso, muy rápido, poco ordenado y te aburres con facilidad.",
            "d": "Querer todo a la vez."
        }
    },
    {
        "num": 12,
        "text": "¿Qué actitud asumes frente a los errores de los otros?",
        "options": {
            "a": "Corriges, sufres mucho, piensas que es falta de precisión.",
            "b": "Haces frecuentemente caso omiso y tomas en cuenta a la persona y su esfuerzo personal.",
            "c": "Poco tolerante, acusas inmediatamente. Los hechos son los hechos.",
            "d": "Corriges evitando hacerlo sentir mal. Te involucras, aunque tengas que hacer sacrificios."
        }
    },
    {
        "num": 13,
        "text": "De tu participación en un grupo, por lo general te interesa obtener...",
        "options": {
            "a": "Ser conocido, reconocimiento a tus méritos. Proyectarte",
            "b": "Influencias, contactos importantes. Hay objetivos detrás de las cosas que haces.",
            "c": "Amistades y sinceridad.",
            "d": "Conocimiento y sabiduría. Una conversación intelectual."
        }
    },
    {
        "num": 14,
        "text": "Por lo general, tu estado de ánimo es...",
        "options": {
            "a": "Explosivo, ansioso, tenso, invasivo.",
            "b": "Calmado, buena disposición.",
            "c": "Calmado, tenso, imperturbable, prefieres estar solo.",
            "d": "Impulsivo, explosivo, alegre, irrelevante."
        }
    },
    {
        "num": 15,
        "text": "En tu casa o en la oficina eres...",
        "options": {
            "a": "Poco ordenado, aunque puedes mejorarlo, siempre serás despreocupado.",
            "b": "Eres extremadamente metódico, ordenado, detallista y cuidadoso.",
            "c": "Poco ordenado, creativo, te gusta pasar de un tema a otro cuando deja de ser novedoso.",
            "d": "Organizado, rápido, no te gusta perder el tiempo."
        }
    },
    {
        "num": 16,
        "text": "Tu energía, la orientas fundamentalmente en la vida a...",
        "options": {
            "a": "En lograr tus metas principalmente en el campo del conocimiento y perfección.",
            "b": "Quedar bien ante la gente, lograr ser reconocido y admirado.",
            "c": "Lograr tus metas, lo que te has propuesto. Alcanzar el poder.",
            "d": "En ser feliz, aceptado y querido."
        }
    },
    {
        "num": 17,
        "text": "¿Qué actitudes asumes en situaciones de conflicto?",
        "options": {
            "a": "Puedes estallar y por lo general si te vas por la tangente. Sin embargo, eres bueno escuchando cuando te lo propones y puedes negociar.",
            "b": "Explosivo, atacas y defiendes apasionadamente tus opiniones. Te cuesta admitir equivocaciones. Frecuentemente no dejas hablar y a veces no escuchas.",
            "c": "Evitas las confrontaciones y las situaciones tensas. Sabes ceder y quedar amigo.",
            "d": "Eres racional y calculador, escondes y manejas tus emociones. Infléxible con tus reglas"
        }
    },
    {
        "num": 18,
        "text": "En la negociación...",
        "options": {
            "a": "Presionas.",
            "b": "Concilias.",
            "c": "Analizas.",
            "d": "Enfrías situaciones."
        }
    },
    {
        "num": 19,
        "text": "Cuando tomas decisiones te motiva...",
        "options": {
            "a": "La amistad, el sentimiento.",
            "b": "La información que posees.",
            "c": "Tu olfato/intuición.",
            "d": "Lograr tu resultado final."
        }
    },
    {
        "num": 20,
        "text": "En la negociación...",
        "options": {
            "a": "Te gusta demostrar que tienes la razón.",
            "b": "Te gusta sobresalir.",
            "c": "Te gusta tener el control.",
            "d": "Te gusta sentirte bien."
        }
    }
]

# Mapeos de opciones a arquetipos basados en la tabla de SOLUCION
mappings = [
    {"a": "G", "b": "A", "c": "SR", "d": "M"},  # 1
    {"a": "G", "b": "SR", "c": "A", "d": "M"},  # 2
    {"a": "A", "b": "SR", "c": "M", "d": "G"},  # 3
    {"a": "SR", "b": "M", "c": "G", "d": "A"},  # 4
    {"a": "M", "b": "G", "c": "A", "d": "SR"},  # 5
    {"a": "SR", "b": "A", "c": "M", "d": "G"},  # 6
    {"a": "A", "b": "SR", "c": "M", "d": "G"},  # 7
    {"a": "SR", "b": "M", "c": "G", "d": "A"},  # 8
    {"a": "M", "b": "G", "c": "A", "d": "SR"},  # 9
    {"a": "SR", "b": "A", "c": "G", "d": "M"},  # 10
    {"a": "A", "b": "SR", "c": "M", "d": "G"},  # 11
    {"a": "SR", "b": "M", "c": "G", "d": "A"},  # 12
    {"a": "M", "b": "G", "c": "A", "d": "SR"},  # 13
    {"a": "G", "b": "A", "c": "SR", "d": "M"},  # 14
    {"a": "A", "b": "SR", "c": "M", "d": "G"},  # 15
    {"a": "SR", "b": "M", "c": "G", "d": "A"},  # 16
    {"a": "M", "b": "G", "c": "A", "d": "SR"},  # 17
    {"a": "G", "b": "A", "c": "SR", "d": "M"},  # 18
    {"a": "A", "b": "SR", "c": "M", "d": "G"},  # 19
    {"a": "SR", "b": "M", "c": "G", "d": "A"}   # 20
]

archetypes = {
    "G": "El Guerrero",
    "A": "El Amante",
    "SR": "El Sabio Rey",
    "M": "El Mago"
}

st.title("Test de Arquetipos de Personalidad")
st.write("Responde las preguntas para descubrir tu arquetipo dominante. Ideal para conocer más de ti mismo. Gracias por hacer parte de nuestra Familia GlamourCam STUDIOS.")

scores = {"G": 0, "A": 0, "SR": 0, "M": 0}
answers = {}

with st.form(key="quiz_form"):
    for i, q in enumerate(questions):
        st.subheader(f"Pregunta {q['num']}: {q['text']}")
        answer = st.radio("Elige una opción:", list(q['options'].keys()), format_func=lambda x: f"{x}) {q['options'][x]}", key=f"q{i}")
        answers[i] = answer
    submit = st.form_submit_button("Calcular Resultados")

if submit:
    for i, ans in answers.items():
        archetype = mappings[i][ans]
        scores[archetype] += 1
    
    max_score = max(scores.values())
    dominants = [archetypes[key] for key, value in scores.items() if value == max_score]
    
    st.success(f"Tu arquetipo dominante es: {', '.join(dominants)}")
    for key, value in scores.items():

        st.write(f"{archetypes[key]}: {value} puntos")

