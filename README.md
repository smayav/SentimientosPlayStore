# Proyecto7
Proyecto Final Ucamp

# Proyecto de Análisis de Sentimientos en Comentarios de Aplicaciones

Este proyecto se centra en el análisis de sentimientos de los comentarios de las aplicaciones móviles. Utiliza técnicas de procesamiento de lenguaje natural para comprender y clasificar los sentimientos de los comentarios dejados por los usuarios en las revisiones de aplicaciones.

## Descripción del Proyecto

El objetivo principal de este proyecto es analizar la naturaleza de los comentarios de los usuarios sobre aplicaciones móviles. Se emplea un conjunto de datos que contiene comentarios de aplicaciones de la Google Play Store, clasificados en distintos sentimientos como positivos, negativos o neutros.

Reviews de aplicaciones de la Google Play Store: https://www.kaggle.com/datasets/lava18/google-play-store-apps

## Características Principales

- Limpieza y preprocesamiento de los datos, eliminación de valores nulos y limpieza de texto.
- Análisis exploratorio de los datos para comprender la distribución de los sentimientos.
- Aplicación de técnicas de NLP para el análisis de sentimientos.
- Implementación de modelos de aprendizaje automático para la clasificación de sentimientos.
- Uso del Código

## Pasos

1. Clona el repositorio en tu máquina local.
2. Crear un entorno virtual (virtualenv)
3. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `uvicorn web.app:app --reload --port 8000`.
4. Accede a [http://localhost:8000](http://localhost:8000) desde tu navegador.