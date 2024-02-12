import utilidades
import read_csv
import charts
'''
data = [
  {
    'Country/Territory': 'Colombia',
    'Population': 500
  },
  {
    'Country/Territory': 'Bolivia',
    'Population': 300
  }
]

def run():
  keys, values = utilidades.get_population()
  print(keys, values)
  
  print(utilidades.A)
  
  país = input('Ingresa el País => ')
  
  resultado = utilidades.population_by_country(data, país)
  print (resultado)
'''

#ejercicio Reto: graficando la población de un país
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America',data))
  
  contries = list(map(lambda x: x['Country/Territory'], data))
  percentajes = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(contries, percentajes)
  
  country = input('Type Country => ')
  print(country)

  result = utilidades.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utilidades.get_population_dos(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
#hace que main.py se ejecute como scrip
if __name__ == '__main__':  
 run()

