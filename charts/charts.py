import matplotlib.pyplot as plt

def generar_pie_chart():
    etiquetas = ['A', 'B', 'C']
    valores = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(valores, labels=etiquetas)
    plt.savefig('pastel.png')
    plt.close()