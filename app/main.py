# LLamando al modulo mod.py
import utils

# Solo por importar el modulo, no se quiere que empiece a ejecutar, entonces se debe modularizar 
# Una forma de hacerlo es embeber en funciones, para que solo se ejecute de manera explicita

data = [
        {
            'Country' : 'Colombia',
            'Population' : 500
        },
        {
            'Country' : 'Bolivia',
            'Population' : 500
        }
    ]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Type country: ')

    result = utils.population_by_country(data, country)
    print(result)

# Este condicional le indica al archivo que si es ejecutado desde la terminal, pues que ejecute el metodo run
# Pero si es ejecutado desde otro archivo, esto no se va a ejecutar 
if __name__ == '__main__':
    run()