# Profile demo
HOST = 'localhost'
USER = 'student_OC'
PASSWORD = '123abc'
DB_NAME = 'PurBeurre'

# path file MPD.sql
PATH_FILE_DB = "resource/MPD.sql"

CATEGORY = ['Snacks', 'Boissons', 'Produits laitiers', 'Viandes',
            'Plats préparés', 'Petit-déjeuners', 'Céréales et dérivés',
            'Légumes et dérivés', 'Poissons', 'Frais']

SEARCH_TERMS_WITH_JOIN = {
    'SELECT': {'table1.col1': 'table1.col1',  # exit data
               'table1': 'table1'},  # table 1
    'INNER JOIN': {'table2': 'table2'},  # table 1
    'ON': {'table1.col2': 'table1.col2',  # join col table 1
           'table2.col1': 'table2.col1'},   # join col table 2
    'WHERE': {'table2.col2': 'table2.col2'}}  # Entry data (condition)

SEARCH_TERMS = {
    'SELECT': {'col1': 'col1',  # exit data
               'table1': 'table1'},  # table 1
    'WHERE': {'col2': 'col2'}}  # Entry data (condition)

ARRAY_LINE_REF = ["Pas de widgets text",  # 0
                  "Code OpenFoodFacts",  # 1
                  "Nom",  # 2
                  "catégorie",  # 3
                  "magasin",  # 4
                  "marques",  # 5
                  "nutriscore",  # 6
                  "url",  # 7
                  "liste d'ingredients",  # 8
                  "Présence d'huile de palme",  # 9
                  "Substances provoquant allergies ou intolérances",  # 10
                  # "Informations nutritionnelles : Valeurs pour 100g ou 100ml"   # 11
                  "Energie en kj", "Energie en cal",  # 12
                  "Matières grasses / Lipide      ",  # 13
                  "      dont acides gras saturés ",  # 14
                  "Glucides                       ",  # 15
                  "      dont sucres              ",  # 16
                  "Protéines                      ",  # 17
                  "Sel                            ",  # 18
                  "      sodium                   ",  # 19
                  "Score nutritionnel - France    ",  # 20
                  "Groupe Nova"]                     # 21
