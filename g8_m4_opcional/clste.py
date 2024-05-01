class te():
    

    def __init__(self, sabor,formato,tiempop,recomendacion):
        self.sabor = sabor
        self.formato = formato
        #self.valor=valor
        self.tiempop = tiempop
        self.recomendacion= recomendacion

    @staticmethod
    def precio(param_formato):
        if param_formato == '1':
            return 3000
        elif param_formato == '2':
            return 5000

    @staticmethod
    def objte(param_sabor):
        if param_sabor == '1':
            return te("Té Negro",None, 5,"se recomienda consumir antes del desayuno.")
        elif param_sabor == '2':
            return te("Té Verde",None, 3, "se recomienda consumir al medio dia.")
        elif param_sabor == '3':
            return te("Hierba",None,7, "se recomienda consumir al atardecer.")
        
    @staticmethod
    def objte_gr(param_sabor,param_formato):
        if param_sabor == '1' and param_formato == '1':
            return te("Té Negro",300, 5, "se recomienda consumir antes del desayuno.")
        elif param_sabor == '1' and param_formato == '2':
            return te("Té Negro", 500,5, "se recomienda consumir antes del desayuno.")
        elif param_sabor == '2' and param_formato =='1':
            return te("Té Verde",300,3, "se recomienda consumir al medio dia.")
        elif param_sabor == '2' and param_formato =='2': 
            return te("Té Verde",500,3, "se recomienda consumir al medio dia.")
        elif param_sabor == '3' and param_formato =='1':
            return te("Hierba",300,7, "se recomienda consumir al atardecer.")
        elif param_sabor == '3' and param_formato =='2':
            return te("Hierba",500,7, "se recomienda consumir al atardecer.")
        