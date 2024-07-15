from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Veri setini yükle
iris = load_iris()
X, y = iris.data, iris.target

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RandomForestClassifier modelini tanımla
rfc = RandomForestClassifier(random_state=42)

# Parametre grid'ini tanımla
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_features': [None, 'sqrt', 'log2'],
    'max_depth': [4, 6, 8, 10],
    'criterion': ['gini', 'entropy']
}

# GridSearchCV nesnesini oluştur
gs = GridSearchCV(estimator=rfc,
                  param_grid=param_grid,
                  scoring='accuracy',
                  cv=10,
                  n_jobs=-1)

# GridSearchCV'yi çalıştır (eğit)
grid_search = gs.fit(X_train, y_train)

# En iyi parametreleri ve skoru göster
eniyisonuc = grid_search.best_score_
eniyiparametreler = grid_search.best_params_

print("En iyi skor:", eniyisonuc)
print("En iyi parametreler:", eniyiparametreler)
