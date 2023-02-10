import matplotlib.pyplot as plt

def bar_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values,color='teal')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['Arroz','Azucar','Lentejas']
    values = [10,55,31]
    bar_chart(labels,values)
    pie_chart(labels,values)