import matplotlib.pyplot as plt

def loss_plot(history):
    acc = history.history['acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc)+1)
    plt.clf()
    plt.plot(epochs, loss, 'b', color="blue", label="Training loss")
    plt.plot(epochs, val_loss, 'b', color="green", label="Validation loss")
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def acc_plot(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(1, len(acc)+1)
    plt.clf()
    plt.plot(epochs, acc, 'b', color="blue", label="Training accuracy")
    plt.plot(epochs, val_acc, 'b', color="green", label="Validation accuracy")
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()