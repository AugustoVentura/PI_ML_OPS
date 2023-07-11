from fastapi import FastAPI, Response
import pandas as pd

app = FastAPI

df = pd.read_csv('datos_completos.csv')

'''Funcion 1: Se ingresa un idioma. Debe devolver la cantidad de películas producidas en ese idioma.'''
@app.get("/movies_language/{language}")
def movies_language(language: str):
    movie_language = df[df['original_language'].str.contains(language, na=False)]
    cantidad_films = len(movie_language)

    respuesta = f"{cantidad_films} cantidad de películas fueron estrenadas en {language}"

    return respuesta

'''Funcion 2: Se ingresa una pelicula. Debe devolver la duracion y el año'''
@app.get("/duration_movies/{movie}")
def duration_movies(movie):
    movie_fill = df[df['title'].str.contains(movie, na=False)]
    respuesta = {}

    if not movie_fill.empty:
        duration = movie_fill['runtime'].values[0]
        year = movie_fill['release_year'].values[0]

        respuesta ={
            'pelicula': movie,
            'duracion': duration,
            'Anio': year
        }

    return respuesta

'''Funcion 3: Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
@app.get("/collection/{collection}")
def collection(collection):
    franquicia = df[df['belongs_to_collection'].str.contains(collection, na=False)]
    cantidad_films = len(franquicia)
    ganancia_total = franquicia['earns'].sum()
    promedio = franquicia['earns'].mean()

    respuesta = f"La franquicia {franquicia} posee {cantidad_films} peliculas, una ganancia total de {ganancia_total} y una ganancia promedio de {promedio}"

    return respuesta

'''Funcion 4: Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.'''
@app.get("/movie_country/{country}")
def movie_country(country):
    country_films = df[df['production_countries'].str.contains(country, na=False)]
    cantidad_films = len(country_films)

    respuesta = f"Se produjeron {cantidad_films} peliculas en el país {country}"

    return respuesta

'''Funcion 5: Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.'''
@app.get("/successful_producers/{producer}")
def successful_producers(producer):
    producer_films = df[df['production_companies'].str.contains(producer, na=False)]

    total_return = producer_films['return'].sum()

    respuesta = f"La productora {producer} ha tenido un revenue de {total_return}"

    return respuesta

'''Funcion 6: Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.'''
@app.get("/director/{director}")
def get_director(director):
    director_films = df[df['director'] == director]
    total_return = director_films['return'].sum()
    presupuesto = director_films['budget'].sum()
    ganancias = director_films['earns'].sum()

    respuesta = {
        'director': director,
        'titulo': director_films['title'].tolist(),
        'fecha': director_films['release_date'].tolist(),
        'retorno': round(total_return, 3),
        'presupuesto': presupuesto,
        'ganancias': ganancias
    }
    return respuesta