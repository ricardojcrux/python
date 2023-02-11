import matplotlib.pyplot as plt

def bar_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values,color='teal')
    plt.title(f'{name}')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def pie_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.title(f'{name}')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

if __name__ == '__main__':
    labels = ['Arroz','Azucar','Lentejas']
    values = [10,55,31]
    bar_chart(labels,values)
    pie_chart(labels,values)