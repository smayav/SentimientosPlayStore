import joblib
import re
import string
import unidecode
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Descargar recursos necesarios desde NLTK
nltk.download('punkt')
nltk.download('stopwords')

stop_words_en = set(stopwords.words('english'))

extra_stopwords = {'quot', 'lol', 'amp', 'today'}
stop_words_en.update(extra_stopwords)

model = joblib.load("modelo.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def get_prediction(text):
    text = clean_text(text)
    vectorized_text = vectorizer.transform([text])
    result = model.predict(vectorized_text)[0]
    if result == "Positive":
       result = "El comentario tiene un sentimiento Positivo"
    elif result == "Neutral":
       result = "El comentario tiene un sentimiento Neutro"
    elif result == "Negative":
       result = "El comentario tiene un sentimiento Negativo"
    else:
       result = "El comentario tiene un sentimiento no identificado"
    return result

def clean_text(text):
  # Convertimos a minúsculas
  text = text.lower()

  # Removemos tags HTML
  text = re.sub(re.compile('<.*?>'), '', text)

  # Tomamos solo las palabras
  text = re.sub('[^A-Za-z0-9]+', ' ', text)

  #Remover puntuación
  #text = re.sub('[^a-zA-Z]', ' ', text)
  text = text.translate(str.maketrans('', '', string.punctuation))

  #Remover símbolos
  text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)

  #Remover dígitos y carácteres especiales
  text=re.sub("(\\d|\\W)+"," ",text)
  #texto_limpio.append(desc)

  #Quitar acentos
  text = unidecode.unidecode(text)

  # Tokenización
  tokens = nltk.word_tokenize(text)

  # Removemos las palabras de parada
  text = [word for word in tokens if word not in stop_words_en]

  # Unimos las palabras
  text = ' '.join(text)

  return text
