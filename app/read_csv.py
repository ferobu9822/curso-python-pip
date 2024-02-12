import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)   #obtiene el encabezado
    data = []
    for row in reader:
      iterable = zip(header, row) #une las dos listas en tuplas
      country_dict = {key: value for key, value in iterable} #crea diccionario
      data.append(country_dict) #agrega diccionario a la lista data
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  #print(data)
  print(data[10])