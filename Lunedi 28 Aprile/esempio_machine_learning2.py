# Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Caricare il dataset Iris
iris = load_iris()
X = iris.data # Caratteristiche (lunghezza e larghezza di sepali e petali)
y = iris.target # Etichette (specie di Iris)

random_states = [5, 9, 25, 42, 77]
n_neighbors_list = [1, 3, 5, 7, 9]

for random_state in random_states:
    # Suddividere il dataset con il random_state attuale
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
    
    # Ciclo interno sui diversi n_neighbors
    for n_neighbors in n_neighbors_list:
        # Definire e addestrare il modello
        model = KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(X_train, y_train)
        
        # Fare predizioni e valutare
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Print completo
        print(f"Random State: {random_state}, n_neighbors: {n_neighbors}, Accuratezza: {accuracy:.2f}")
