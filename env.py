

DATA_TABLE = {
    'secondary_id': '_id',

    'belongsTo': {
        'category':['nom'],
        'vendeur' :['user_id'],
        'user' :['nom','prenom'],
    },

    'ignore':[
        'liste des tables à ignorer (nom sens s de fin comme user[s])'
    ]
}

HEADER = {
    'accept':'application/json'
}

DATA_URL = {
    "base": "http://127.0.0.1:8000/api",
    
    "attr": ["attr/{model}", "GET"],
    
    "specify": ["attr/{model}/specify", "GET"],
    
    "fillable": ["/attr/{model}/fillable", "GET"],
    
    "anyView": ["{model}", "GET"],
   
    "store": ["{model}/", "POST"],
    
    "show": ["{model}/{id}", "GET"],
    
    "update": ["{model}/{id}", "PUT"],
    
    "destroy": ["{model}/{id}", "DELETE"],
    
    "table": ["table", "GET"],
}